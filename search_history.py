from search_result import SearchResult

class SearchHistory():
    
    def __init__(self):
        self.searches_json = []
        
    def import_from_json_file(self):
        from json_helper import load_from_json_file
        tmp_searches = load_from_json_file()
        if tmp_searches is None:
            pass
        else:
            self.searches_json = tmp_searches
    
    def export_to_json_file(self):
        from json_helper import save_to_json_file
        save_to_json_file(self.searches_json)
                
    def add_to_history(self, json_data, search_term):
        if self.term_in_list(search_term):
            return
        json_data["SearchTerm"] = search_term
        self.searches_json.insert(0, json_data)
        
    def get_search_terms(self):
        search_terms = [item["SearchTerm"] for item in self.searches_json]
        if len(search_terms) == 0:
            return [""]
        return search_terms
        
    def get(self, search_term):
        for item in self.searches_json:
            if item["SearchTerm"] == search_term:
                return SearchResult(item)
    
    def term_in_list(self, search_term):
        for item in self.searches_json:
            if item["SearchTerm"] == search_term:
                return True
        return False