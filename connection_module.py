from requests import get as rget
import requests.exceptions
#key 79f18d48

def error_dict():
    return {"Error": True}

def movie_search_query(search_term):
    for i in range (5):
        try:
            response = rget(f"https://www.omdbapi.com/?s={search_term}&apikey=79f18d48")
            return response.json()
        except requests.exceptions.Timeout:
            continue
        except:
            continue
    return error_dict()

def detailed_movie_query(movie_id):
    for i in range (5):
        try:
            response = rget(f"https://www.omdbapi.com/?i={movie_id}&apikey=79f18d48")
            return response.json()
        except requests.exceptions.Timeout:
            continue
        except:
            continue
    return error_dict()
        
def get_image(url):
    from image_converter import bytes_to_image, default_image
    try:
        return bytes_to_image(rget(url).content)
    except:
        return default_image()
    

