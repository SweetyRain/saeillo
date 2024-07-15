from flask import Flask, render_template, request
from DB import get_data
from datetime import datetime
import requests

app = Flask(__name__)

def format_deadline(deadline):
    if deadline == 30000000:
        return "채용시까지"
    else:
        return datetime.strptime(str(deadline), '%Y%m%d').strftime('%Y년 %m월 %d일')
@app.route('/')
@app.route('/<name>')
def renework(name = None):
    return render_template('main.html', name=name)

@app.route('/full')
def full_page():
    full_sql = 'SELECT job_index, job_title, job_link, job_region, job_deadline, job_employmentType FROM announcement'
    data = get_data(full_sql)

    for row in data:
        row['formatted_deadline'] = format_deadline(row['job_deadline'])

    return render_template('full.html', data=data)

@app.route('/category')
def category_page():

    value = request.args.get('value', default='조리', type=str)

    category_sql = f"SELECT job_index, job_title, job_link, job_region, job_deadline, job_employmentType FROM announcement WHERE job_categorie = '{value}'"

    data = get_data(category_sql)

    for row in data:
        row['formatted_deadline'] = format_deadline(row['job_deadline'])

    return render_template('category.html', data=data)

if __name__ == "__main__":
    app.run()