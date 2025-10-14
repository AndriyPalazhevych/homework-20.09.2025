from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/countries')
def countries():
    places = [
        "Берлін, Німеччина",
        "Лондон, Англія",
        "Київ, Україна",
        "Каліфорнія, Сполучені Штати Америки",
        "Банкок, Таїланд"
    ]
    return render_template('countries.html', places=places)

@app.route('/contact')
def contact():
    contacts = [
        ("Рон'я", "+4909647291"),
        ("Чарли", "+44020141"),
        ("Микита", "+380963043123"),
        ("Джордан", "+15552221234"),
        ("Док Май", "+661234567")
    ]
    return render_template('contact.html', contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True)