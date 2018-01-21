# nutritionix.py
import nutritionix_api_key
import requests
import json


def do_nutri(food):
    r = requests.post("https://trackapi.nutritionix.com/v2/natural/nutrients",
        headers = {"x-app-id": nutritionix_api_key.my_api_id, "x-app-key": nutritionix_api_key.my_api_key, "Content-Type": "application/json"},
        data = json.dumps({"query":food, "timezone":"US/Eastern"})
    )
    print(r.json())
    r_json = r.json()
    
    """json['foods'][0]['nf_calories']
    json['foods'][0]['nf_sodium']
    json['foods'][0]['nf_potassium']"""

    return {'calories': int(r_json['foods'][0]['nf_calories']), 'sodium': int(r_json['foods'][0]['nf_sodium']), 'potassium': int(r_json['foods'][0]['nf_potassium'])}
