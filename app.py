from flask import Flask, render_template, request, redirect, url_for
import yaml

app = Flask(__name__)

with open('data.yaml', 'r') as file:
    data = yaml.safe_load(file)
documents = data['documents']
questions = data['questions']
tags = data['tags']
current_index = 0

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
        with open('results.yaml', 'a') as file:
            yaml.dump([result], file)
        global current_index
        current_index += 1
        if current_index >= len(documents) * len(questions):
            return redirect(url_for('index'))
        return redirect(url_for('review'))
    document = documents[current_index // len(questions)]
    question = questions[current_index % len(questions)]
    return render_template('review.html', document=document, question=question, tags=tags)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)