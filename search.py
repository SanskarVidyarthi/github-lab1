import json

def search_json(json_data, search_string):
    results = []
    for d in json_data:
        user_dict = {}
        
        for key, value in d.items():
            if search_string in key or search_string in value:
                user_dict["User"] = d.get("User")
                user_dict[key] = value

        if user_dict:
            results.append(user_dict)
    return results