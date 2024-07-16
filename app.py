from flask import Flask, render_template, request, redirect, url_for, session
import yaml
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

with open('data.yaml', 'r') as file:
    data = yaml.safe_load(file)
documents = data['documents']
questions = data['questions']
tags = data['tags']

@app.before_request
def initialize_session():
    if 'current_index' not in session:
        session['current_index'] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        selected_tag = request.form['tag']
        document_id = documents[current_index]['id']
        question = questions[current_index % len(questions)]
        result = {
            'document_id': document_id,
            'question': question,
            'tag': selected_tag
        }
        with open('results.yaml', 'r') as file:
            existing_results = yaml.safe_load(file) or []
        existing_results.append(result)
        with open('results.yaml', 'w') as file:
            yaml.dump(existing_results, file)
        session['current_index'] += 1
        if session['current_index'] >= len(documents) * len(questions):
            return redirect(url_for('index'))
        return redirect(url_for('review'))
    document = documents[session['current_index'] // len(questions)]
    question = questions[session['current_index'] % len(questions)]
    return render_template('review.html', document=document, question=question, tags=tags)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)