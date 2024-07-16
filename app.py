from flask import Flask, render_template, request, redirect, url_for
import yaml

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        # Handle form submission and save to YAML
        pass
    return render_template('review.html')

if __name__ == '__main__':
    app.run(debug=True)