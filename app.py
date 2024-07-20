from flask import Flask, request, render_template
import re

app = Flask(__name__)

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return s == s[::-1]

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == 'POST':
        text = request.form['text']
        if is_palindrome(text):
            result = f'"{text}" is a palindrome!'
        else:
            result = f'"{text}" is not a palindrome.'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
