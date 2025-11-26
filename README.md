# 🌦️ Django Weather App with Glassmorphism & HTMX

![Project Banner](screenshots/banner.png)
A modern, responsive weather forecast application built with **Django** and **HTMX**. This project demonstrates how to create a Single Page Application (SPA) feel without using complex frontend frameworks like React or Vue, while maintaining a stunning **Glassmorphism UI** using Tailwind CSS.

## ✨ Key Features

- **Real-time Weather Data:** Fetches data from the OpenWeatherMap API.
- **Dynamic Backgrounds:** The background gradient changes automatically based on weather conditions (Clear, Rain, Clouds) and temperature (Hot/Cold).
- **Seamless Interaction (HTMX):** Updates weather information without reloading the page (AJAX), providing a smooth user experience.
- **Glassmorphism UI:** Modern, transparent card design using Tailwind CSS.
- **Context-Aware Suggestions:** Provides outfit and mood recommendations based on the current weather.
- **Thai Font Support:** Integrated 'Kanit' font for a clean and modern typography.

## 🛠️ Tech Stack

* **Backend:** Python 3.11+, Django 5.x
* **Frontend:** HTML5, CSS3 (Tailwind CSS via CDN)
* **Interactivity:** HTMX
* **API:** OpenWeatherMap
* **Font:** Google Fonts (Kanit)

## 🚀 Installation & Setup

Follow these steps to run the project locally:

1.  **Clone the repository**
    ```bash
    git clone https://github.com/kengkla77/weather_website_api.git
    cd django-weather-app
    ```

2.  **Create a Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install django requests
    ```

4.  **Configure API Key**
    * Open `wea_app/views.py`.
    * Replace the placeholder with your OpenWeatherMap API key:
        ```python
        api_key = 'YOUR_API_KEY_HERE'
        ```

5.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

6.  **Access the App**
    * Open your browser and go to `http://127.0.0.1:8000/`.

## 📂 Project Structure

```text
weather_project/
├── db.sqlite3
├── manage.py
├── wea_app/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── wea_app/
│   │       ├── base.html        # Main layout with Glass UI
│   │       └── partials/
│   │           └── weather_card.html  # HTMX swapped component
│   ├── urls.py
│   └── views.py                 # Logic for API & Dynamic Backgrounds
└── weather_project/
    ├── settings.py
    └── urls.py
