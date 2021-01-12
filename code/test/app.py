from flask import Flask, render_template, request
import deal

def deal_data(form):
    print(form)
    return form

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index.html',
            message='无')

@app.route('/',methods = ['POST', 'GET'])
def resend():
    if request.method == 'POST':
        result = request.form
        result = deal_data(result)
        return render_template('index.html',
            message=result)
    
if __name__ == '__main__':
    app.run(debug=True)