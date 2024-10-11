from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 템플릿에 전달할 데이터
    users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]

    # render_template을 사용하여 템플릿 파일을 렌더링
    # (1) rendering할 html 파일명 입력
    # (2) html로 넘겨줄 데이터 입력
    return render_template('index.html', data=users)

if __name__ == '__main__':
    app.run(debug=True)