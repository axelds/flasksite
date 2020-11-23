from flask import * 
app = Flask(__name__)
@app.route('/')
def index():
    user = "Александр"
    return render_template('index.html', username = user, title='Домашняя страница')
@app.route('/news')
def news():
    with open("templates/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('news.html', news=news_list, title='Новости')

@app.route('/photo')
def first():
    photo = url_for('static', filename='images/picture.png')
    return render_template('picture.html', photo = photo, title='Картинка') 

@app.route('/register', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('register.html', title='Регистрация')
    elif request.method == 'POST':
        print(request.form.get('email'))
        print(request.form.get('password'))
        print(request.form.get('file'))
        print(request.form.get('about'))
        print(request.form.get('accept'))
        print(request.form.get('sex'))
        return render_template('thankyou.html', title='Регистрация')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)