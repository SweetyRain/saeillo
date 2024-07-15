from flask import Flask, render_template
from DB import get_data_full
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def renework(name = None):
    return render_template('main.html', name=name)

@app.route('/full')
def full_page():
    full_sql = 'SELECT job_index, job_title, job_link, job_region, job_deadline, job_employmentType FROM announcement'
    data = get_data_full(full_sql)
    return render_template('full.html', data=data)

if __name__ == "__main__":
    app.run()