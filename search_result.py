class SearchResult():
       
    def __init__(self, json_data):
        self.json_data = json_data
        
    def create_search_result(self, search_term, json_data):
        new_search = SearchResult(json_data)
        new_search["SearchTerm"] = search_term
        return new_search
    
    def get_title(self, index):
        return json_data["Search"][index]["Title"]
    
    def get_titles(self):
        return [item["Title"] for item in self.json_data["Search"]]
    
    def get_id(self, index):
        return self.json_data["Search"][index]["imdbID"]
    
    def get_poster_link(self, index):
        return self.json_data["Search"][index]["Poster"]

    def get_search_term(self):
        return self.json_data["SearchTerm"]
    
    def is_empty(self):
        if self.json_data is None:
            return True
        elif len(self.json_data) == 0:
            return True
        else:
            return False
    
        