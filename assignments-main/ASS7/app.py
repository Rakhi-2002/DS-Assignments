from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    total = num1 + num2
    return f'The sum of {num1} and {num2} is {total}'

if __name__ == '__main__':
    app.run(debug=True)