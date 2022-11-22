from flask import Flask, render_template

# 웹 서버 역할 Flask APP
app = Flask(__name__)

# 라우터 설정
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page')
def page():
    return render_template('page.html')    


# 가동(run)
if __name__ == "__main__":
    app.run(debug=True)