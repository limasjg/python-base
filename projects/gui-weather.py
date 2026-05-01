import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App')

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: Calibri;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: segoe ui emoji;
            }
            QLabel#description_label {
                font-size: 50px;
            }
        """)
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        city = self.city_input.text()
        api_key = "f29d4e370bd0f4ddb1f8b91e17c17c00"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            print(data)

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Error 400: Bad Request \n The request was invalid.")
                case 401:
                    self.display_error("Error 401: Unauthorized \n API key is missing or invalid.")
                case 403:
                    self.display_error("Error 403: Forbidden \n You do not have permission to access this resource.")
                case 404:
                    self.display_error("Error 404: Not Found \n The city name could not be found.")
                case 500:
                    self.display_error("Error 500: Internal Server Error \n An error occurred on the server.")
                case 502:   
                    self.display_error("Error 502: Bad Gateway \n The server received an invalid response from the upstream server.")
                case 503:
                    self.display_error("Error 503: Service Unavailable \n The server is currently unable to handle the request.")
                case 504:
                    self.display_error("Error 504: Gateway Timeout \n The server did not receive a timely response from the upstream server.")
                case _:
                    self.display_error(f"HTTP error occurred: {http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Error: Failed to connect to the weather service. Please check your internet connection.")

        except requests.exceptions.Timeout:
            self.display_error("Error: The request to the weather service timed out. Please try again later.")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Error: Too many redirects. The URL may be incorrect.")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"An error occurred: {req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 20px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        weather_id = data['weather'][0]['id']

        self.temperature_label.setText(f"{data['main']['temp']:.0f}°C")
        self.emoji_label.setText(self.get_emoji(weather_id))
        self.description_label.setText(data['weather'][0]['description'].capitalize())

    @staticmethod
    def get_emoji(weather_id):
        if 200 <= weather_id < 300:
            return "⛈️"  # Thunderstorm
        elif 300 <= weather_id < 400:
            return "🌧️"  # Drizzle
        elif 500 <= weather_id < 600:
            return "🌧️"  # Rain
        elif 600 <= weather_id < 700:
            return "❄️"  # Snow
        elif 700 <= weather_id < 800:
            return "🌫️"  # Fog
        elif weather_id == 800:
            return "☀️"  # Clear
        elif 801 <= weather_id < 900:
            return "☁️"  # Cloudy
        else:
            return ""  # Unknown

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())