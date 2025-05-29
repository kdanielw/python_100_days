import requests
import json

END_POINT = "https://opentdb.com/api.php"
PARAMETERS = {
    "amount": 10,
    "type": "boolean",
    "category": 31,
}

def get_questions():
    
    response = requests.get(url=END_POINT, params=PARAMETERS)
    response.raise_for_status()
    data = response.json()
    return data["results"]


question_data = get_questions()
