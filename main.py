from info import NUTRITIONIX_ID, NUTRITIONIX_API_KEY, GENDER, AGE, WEIGHT_KG, HEIGHT_CM, SHEETS_API, BEARER_TOKEN
import requests
from datetime import datetime
today_date = datetime.today().strftime("%Y""%m""%d")
today_time = datetime.now().strftime("%H:""%M:""%S")


headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
}
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/"
nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}
response = requests.post(url=nutritionix_exercise_endpoint, json=exercise_params, headers=headers)
returned_exercise_data = response.json()
data_list = [value for (key, value) in returned_exercise_data.items()]
user_input = returned_exercise_data["exercises"][0]["user_input"]
user_duration = returned_exercise_data["exercises"][0]["duration_min"]
user_calories_burned = returned_exercise_data["exercises"][0]["nf_calories"]

upload_params = {
    "sheet1": {
    "date": today_date,
    "time": today_time,
    "exercise": user_input,
    "duration": user_duration,
    "calories": user_calories_burned
}
}
sheets_headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
sheets_endpoint = f"https://api.sheety.co/{SHEETS_API}/workoutSpreadsheet/sheet1"
sheets_response = requests.post(url=sheets_endpoint, json=upload_params, headers=sheets_headers)
print(sheets_response.text)

