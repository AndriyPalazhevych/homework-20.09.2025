from flask import Flask, request, redirect, url_for

app = Flask(__name__)
participants = []

@app.route('/')
def form():
    return '''
        <h2>Реєстрація на вебінар</h2>
        <form method="post" action="/register">
            Ім'я: <input name="name"><br>
            Email: <input name="email" type="email"><br>
            Час:
            <select name="time">
                <option value="">Оберіть</option>
                <option>ранок</option>
                <option>день</option>
                <option>вечір</option>
            </select><br><br>
            <button type="submit">Зареєструватися</button>
        </form>
    '''

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    time = request.form['time']

    if not name or not email or not time:
        return 'Всі поля обов’язкові. <a href="/">Назад</a>'

    participants.append({'name': name, 'email': email, 'time': time})
    return redirect(url_for('show_participants'))

@app.route('/participants')
def show_participants():
    output = '<h2>Список учасників</h2><ul>'
    for p in participants:
        output += f"<li>{p['name']} ({p['email']}) — {p['time']}</li>"
    output += '</ul><a href="/">Назад до форми</a>'
    return output

if __name__ == '__main__':
    app.run(debug=True)
