def load_from_json_file(file_path = "backup.json"):
    from json import load
    try:
        with open (file_path, "r", encoding="utf-8") as file_obj:
            return load(file_obj)
    except:
        pass

def save_to_json_file(json_data, file_path = "backup.json"):
    from json import dump
    try:
        with open (file_path, "w", encoding="utf-8") as file_obj:    
            dump(json_data, file_obj)
    except:
        pass