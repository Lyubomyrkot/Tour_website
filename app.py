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

@app.route("/") # Вказуємо url-адресу для виклику функції
def index():
    countries = get_all_countries()
    return render_template("index.html", countries=countries) #Результат, що повертається у браузер

@app.route("/countries") # Вказуємо url-адресу для виклику функції
def countries():
    return render_template("countries.html") #Результат, що повертається у браузер

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True # Вмикаємо режим налагодження
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу
