from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__) # Створюємо веб–додаток Flask

@app.route("/") # Вказуємо url-адресу для виклику функції
def index():
    return render_template("index.html") #Результат, що повертається у браузер

@app.route("/countries") # Вказуємо url-адресу для виклику функції
def countries():
    return render_template("countries.html") #Результат, що повертається у браузер

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True # Вмикаємо режим налагодження
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу
