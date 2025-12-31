from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__) # Створюємо веб–додаток Flask
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'mysecretkey')

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
                    SELECT tours.*, countries.country_name, countries.capital, countries.image AS country_image, countries_in_tours.*
                    FROM tours
                    JOIN countries_in_tours ON tours.id = countries_in_tours.tour_id
                    JOIN countries ON countries_in_tours.country_id = countries.id
                    """)
    countries_in_tours = cursor.fetchall()
    conn.close()
    return countries_in_tours

def get_tours_by_country(country_id):
    conn = sqlite3.connect('templates/ture.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            tours.*,
            countries.country_name,
            countries.capital
        FROM tours
        JOIN countries_in_tours 
            ON tours.id = countries_in_tours.tour_id
        JOIN countries 
            ON countries.id = countries_in_tours.country_id
        WHERE countries.id = ?
    """, (country_id,))

    tours = cursor.fetchall()
    conn.close()
    return tours

def get_reviews_by_tour(tour_id):
    conn = sqlite3.connect('templates/ture.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_name, rating, comment, review_date
        FROM reviews
        WHERE tour_id = ?
        ORDER BY review_date DESC
    """, (tour_id,))

    reviews = cursor.fetchall()
    conn.close()
    return reviews

def get_cities_by_tour(tour_id):
    conn = sqlite3.connect('templates/ture.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            cities.city_name,
            cities.description,
            cities.duration_days,
            cities.image,
            cities_in_tour.day_order
        FROM cities_in_tour
        JOIN cities ON cities.id = cities_in_tour.city_id
        WHERE cities_in_tour.tour_id = ?
        ORDER BY cities_in_tour.day_order
    """, (tour_id,))

    cities = cursor.fetchall()
    conn.close()
    return cities





@app.route("/") # Вказуємо url-адресу для виклику функції
def index():
    countries = get_all_countries()
    tours = get_all_tours()
    countries_in_tours = get_all_countries_in_tours()
    return render_template("index.html", countries_in_tours=countries_in_tours, countries=countries, tours=tours, ) #Результат, що повертається у браузер

@app.route("/countries/<int:country_id>") # Вказуємо url-адресу для виклику функції
def countries_details(country_id):
    conn = sqlite3.connect('templates/ture.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM countries WHERE id = ? ''', (country_id,))
    country = cursor.fetchone()
    conn.close()

    tours = get_tours_by_country(country_id)

    return render_template("countries_details.html", country=country, tours=tours) #Результат, що повертається у браузер

@app.route("/tours/<int:tour_id>") # Вказуємо url-адресу для виклику функції
def tour_details(tour_id):
    conn = sqlite3.connect('templates/ture.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM tours WHERE id = ? ''', (tour_id,))
    tour = cursor.fetchone()
    reviews = get_reviews_by_tour(tour_id)
    cities = get_cities_by_tour(tour_id)
    conn.close()
    return render_template("tour_details.html", tour=tour, reviews=reviews, cities=cities) #Результат, що повертається у браузер



if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True # Вмикаємо режим налагодження
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу
