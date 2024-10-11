from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This is the main Page..!"

@app.route('/about')
def about():
    return "This is the about Page..!"
# 복사할 코드 드래그 -> Alt + Shift + 화살표 위/아래 => 드래그된 부분 아래로 복사됨

# 동적으로 URL 파라미터 값을 받아서 처리해준다.
# URL 입력 시 꺽새("< >") 위치에 입력하면 매개변수처럼 사용할 수 있는듯!
# http://127.0.0.1:5000/user/abc    <- 이런식으로
@app.route('/user/<username>')
def user_profile(username):
    return f'UserName : {username}'

# 만약 매개변수를 숫자로만 받고싶다면?
@app.route('/number/<int:number>')
def number(number):
    return f'Number : {number}'

# POST 요청 날리는 법
# (1) postman
# (2) requests
import requests

@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)
    
    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == "GET":
        pritn("GET method")
    
    if request.method == "POST":
        print("**POST method**", request.data)
    return Response("Successfully submitted", status=200)

if __name__ == "__main__":
    app.run(port=5000)