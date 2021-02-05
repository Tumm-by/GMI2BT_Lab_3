from tkinter import *
from search_result import SearchResult
from search_history import SearchHistory

class MovieMenu():
    
    def __init__(self):
        
        self.main_window = self.create_main_window()                #Main window
        self.search_result = SearchResult("")                                     #Current search result 1 instance of SearchResult
        self.search_result_box = self.create_listbox()              #List of all the titles in the SearchResult
        self.search_history = SearchHistory()                       #Contains the result of all previous Searches
        self.search_history.import_from_json_file()
        self.search_history_help_var = StringVar(self.main_window)  #StringVar used by the Optionmenu
        self.search_history_tab = self.create_history_tab()         #OptionMenu of previus searches
        self.search_bar = self.create_search_bar()
        self.search_button = self.create_button("Search", self.search_for, 2, 0)
        self.exit_button = self.create_button("Exit", self.main_window.destroy, 3, 0)
        self.poster = self.create_poster()                          #Displays a poster of a movie we clicked
        self.description = self.create_description()                #Surface containing a movie description
        self.main_window.mainloop()
        self.search_history.export_to_json_file()
     
    #Placing widgets  
    def create_main_window(self):
        new_main_window = Tk()
        new_main_window.title("MovieSeeker")
        return new_main_window
    
    def create_search_bar(self):
        new_search_bar = Entry(self.main_window)
        new_search_bar.bind("<Return>", self.search_for)
        new_search_bar.grid(row = 0, column = 0)
        return new_search_bar
    
    def create_button(self, button_text, button_function, button_row, button_column):
        new_button = Button(self.main_window, text = button_text, command = button_function)
        new_button.grid(row = button_row, column = button_column, sticky = N)
        return new_button
    
    def create_poster(self):
        new_poster = Canvas(self.main_window, width = 300, height = 444) #Movie poster proportions
        new_poster.grid(row = 3, column = 3, sticky = NW)
        return new_poster
    
    def create_listbox(self): #Exportselection false prevents the event from triggering outside the box
        new_listbox = Listbox(self.main_window, selectmode = BROWSE, exportselection = FALSE)
        new_listbox.bind("<<ListboxSelect>>", self.update_infopanels) #Triggers whenever we change selection
        new_listbox.grid(row = 3, column = 0)
        return new_listbox
    
    def create_description(self): #State disabled prevents modification of the text by the user
        new_description = Text(self.main_window, state = DISABLED)
        new_description.grid(row = 3, column = 1, sticky = S)
        return new_description
    
    def create_history_tab(self):
        new_history_tab = OptionMenu(self.main_window, self.search_history_help_var, *self.search_history.get_search_terms(), command = self.load_old_search)
        new_history_tab.grid(row = 1, column = 0)
        return new_history_tab
    
    #Methods
    def search_for(self, event = ""): #Optional argument need for sending search for as a callable function
        from connection_module import movie_search_query
        search_term = self.search_bar.get()
        query_response = movie_search_query(search_term)
        if query_response == None:
            return
        if "Search" in query_response:
            self.search_history.add_to_history(query_response, search_term)
            self.search_result = self.search_history.get(search_term)
            self.update_search_result_box()
            self.update_history_tab()
            
    def load_old_search(self, event):#Looks up and loads the SearchResult for the selected search term in the OptionMenu
        if self.search_history_help_var.get() != "": #If nothing has been loaded yet.
            self.search_result = self.search_history.get(self.search_history_help_var.get())
            self.update_search_result_box()
        
    def update_search_result_box(self): #Updates the search result box using the search result
        self.search_result_box.delete(0, END)
        for item in self.search_result.get_titles():
            self.search_result_box.insert(END, item)
            
    def update_history_tab(self):
        self.search_history_tab = self.create_history_tab()
        self.main_window.mainloop()

    def update_infopanels(self, event): #Updates the content for the description and poster
        from connection_module import get_image, detailed_movie_query
        if self.search_result.is_empty():
            return
        self.description.configure(state = NORMAL) #To allow modification
        self.description.delete("1.0", END) # For text it's 1.0 and not 0
        active_index = int(self.search_result_box.curselection()[0]) #Get the index of the selected movie title
        movie_info = detailed_movie_query(self.search_result.get_id(active_index))
        if "Title" in movie_info:
            self.description.insert(END,f'Title: {movie_info["Title"]}\nType: {movie_info["Type"]}\nReleased: {movie_info["Released"]}\tRuntime: {movie_info["Runtime"]}\n\n{movie_info["Plot"]}\n\nDirector: {movie_info["Director"]}\nActors: {movie_info["Actors"]}')
        self.description.configure(state = DISABLED)
        
        self.update_canvas(get_image(self.search_result.get_poster_link(active_index)))
               
    def update_canvas(self, new_image): #Updates the poster
        self.poster.delete("all")
        self.poster.create_image(0, 0, image = new_image, anchor = NW)
        self.main_window.mainloop()