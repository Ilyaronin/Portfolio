#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

@app.route('/submit', methods=['POST'])
def submit_form():
    email = request.form['email']
    text = request.form['text']
    with open('form.txt', 'a',) as f:
            f.write(f"email: {email}/n")
            f.write(f"text: {text}/n")
    return render_template('form_result.html', 
                           email=email,
                           text=text)

if __name__ == "__main__":
    app.run(debug=True)