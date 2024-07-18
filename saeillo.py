from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from DB import get_data
from datetime import datetime
import requests

app = Flask(__name__)

#마감일 포맷 변경
def format_deadline(deadline):
    if deadline == 30000000:
        return "채용시까지"
    else:
        return datetime.strptime(str(deadline), '%Y%m%d').strftime('%Y년 %m월 %d일')

def format_pay(pay):
    pay = str(pay)[:-4]
    format_pay = f'월 {pay} 만원'
    return format_pay

# 페이지네이션을 위한 함수
# def paginate_data(data, page, per_page):
#     total_items = len(data)
#     total_pages = (total_items + per_page - 1) // per_page  # 총 페이지 수 계산
#
#     if page < 1:
#         page = 1
#     elif page > total_pages:
#         page = total_pages
#
#     start = (page - 1) * per_page
#     end = start + per_page
#     paginated_data = data[start:end]
#
#     has_prev = page > 1
#     has_next = page < total_pages
#
#     return paginated_data, has_prev, has_next, total_pages
@app.route('/')
@app.route('/<name>')
def renework(name = None):
    return render_template('main.html', name=name)

@app.route('/full')
def full_page():
    full_sql = "SELECT job_index, job_title, job_link, job_region, job_deadline, job_workType, job_pay FROM announcement"
    data = get_data(full_sql)

    for row in data:
        row['formatted_deadline'] = format_deadline(row['job_deadline'])
        row['formatted_pay'] = format_pay(row['job_pay'])

    return render_template('full.html', data=data)
@app.route('/category')
def category_page():
    value = request.args.get('value', default='조리', type=str)
    print(value)
    category_sql = (f"SELECT job_index, job_title, job_link, job_region, job_deadline, job_worktype, job_pay FROM announcement WHERE job_categorie = '{value}'")

    data = get_data(category_sql)

    for row in data:
        row['formatted_deadline'] = format_deadline(row['job_deadline'])
        row['formatted_pay'] = format_pay(row['job_pay'])

    #count_sql = f"SELECT COUNT(*) FROM announcement WHERE job_categorie = '{value}'"

    return render_template('category.html', data=data)

@app.route('/region')
def region_page():
    value = request.args.get('value', default='서울 강남구', type=str)
    print(value)
    address1, address2 = value.split()
    region_sql = (
        f"SELECT job_index, job_title, job_link, job_region, job_deadline, job_worktype, job_pay FROM announcement WHERE job_fullregion = '%{address2}%'")

    data = get_data(region_sql)

    for row in data:
        row['formatted_deadline'] = format_deadline(row['job_deadline'])
        row['formatted_pay'] = format_pay(row['job_pay'])

    # count_sql = f"SELECT COUNT(*) FROM announcement WHERE job_categorie = '{value}'"

    return render_template('region.html', data=data)

@app.route('/personal')
def personal_page():
    return render_template('personal.html')

if __name__ == "__main__":
    app.run()