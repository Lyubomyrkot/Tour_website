from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__) # Створюємо веб–додаток Flask

def get_all_countries():
    conn = sqlite3.connect('templates/ture.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM countries ''')
    countries = cursor.fetchall()
    conn.close()
    return countries

def get_all_tours():
    conn = sqlite3.connect('templates/ture.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM tours ''')
    countries = cursor.fetchall()
    conn.close()
    return countries

# mongoDB максим рекомандував до вивчання

def get_all_countries_in_tours():
    conn = sqlite3.connect('templates/ture.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT tours.*, countries.country_name, countries.image AS country_image
                    FROM tours
                    JOIN countries_in_tours ON tours.id = countries_in_tours.tour_id
                    JOIN countries ON countries_in_tours.country_id = countries.id
                    """)
    countries_in_tours = cursor.fetchall()
    conn.close()
    return countries_in_tours

@app.route("/") # Вказуємо url-адресу для виклику функції
def index():
    countries = get_all_countries()
    tours = get_all_tours()
    countries_in_tours = get_all_countries_in_tours()
    return render_template("index.html", countries_in_tours=countries_in_tours, countries=countries, tours=tours, ) #Результат, що повертається у браузер

@app.route("/countries") # Вказуємо url-адресу для виклику функції
def countries():
    return render_template("countries.html") #Результат, що повертається у браузер

@app.route("/tours/<int:tour_id>") # Вказуємо url-адресу для виклику функції
def tour_details(tour_id):
    conn = sqlite3.connect('templates/ture.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM tours WHERE id = ? ''', (tour_id,))
    tour = cursor.fetchone()
    conn.close()
    return render_template("tour_details.html", tour=tour) #Результат, що повертається у браузер


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True # Вмикаємо режим налагодження
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу
