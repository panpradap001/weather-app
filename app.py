from dotenv import load_dotenv
import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# โหลดข้อมูลจากไฟล์ .env
load_dotenv()
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("API_KEY")
# ตรวจสอบว่า API_KEY ถูกโหลดหรือไม่
load_dotenv()
API_KEY = os.getenv("API_KEY")


@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            params = {"q": city, "appid": API_KEY, "units": "metric"}
            response = requests.get(BASE_URL, params=params)
            
            if response.status_code == 200:
                weather_data = response.json()
                if "weather" not in weather_data:
                    weather_data = None  # ถ้าไม่มีข้อมูล ก็ให้กำหนดให้เป็น None
            else:
                print(f"Error {response.status_code}: {response.text}")  # พิมพ์ข้อความผิดพลาดจาก API


    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
