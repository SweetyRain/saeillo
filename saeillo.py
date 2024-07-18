from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from DB import get_data
from datetime import datetime
import requests

app = Flask(__name__)

#마감일 포멧 변경
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
def paginate_data(data, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    total = len(data)
    paginated_data = data[start:end]
    has_next = end < total
    has_prev = start > 0
    total_pages = (total + per_page - 1) // per_page
    return paginated_data, has_prev, has_next, total_pages

@app.route('/')
@app.route('/<name>')
def renework(name = None):
    return render_template('main.html', name=name)

@app.route('/full')
def full_page():
    page = request.args.get('page', type=int, default=1)
    per_page = 20  # 페이지당 보여줄 항목 수

    full_sql = "SELECT job_index, job_title, job_link, job_region, job_deadline, job_workType, job_pay FROM announcement"
    data = get_data(full_sql)

    for row in data:
        row['formatted_deadline'] = format_deadline(row['job_deadline'])
        row['formatted_pay'] = format_pay(row['job_pay'])

    # # 데이터 페이징 처리
    # paginated_data, has_prev, has_next, total_pages = paginate_data(data, page, per_page)
    #
    # # 페이지 번호 목록 생성
    # page_numbers = list(range(max(1, page - 2), min(total_pages, page + 2) + 1))
    #
    # return render_template('full.html', data=paginated_data, has_prev=has_prev, has_next=has_next, page=page, page_numbers=page_numbers, total_pages=total_pages)

    data = data.paginate(page=page, per_page=10)
    return render_template('full.html', data = data)
@app.route('/category')
def category_page():
    page = request.args.get('page', type=int, default=1)
    per_page = 20  # 페이지당 보여줄 항목 수

    value = request.args.get('value', default='조리', type=str)

    category_sql = f"SELECT job_index, job_title, job_link, job_region, job_deadline, job_worktype, job_pay FROM announcement WHERE job_categorie = '{value}'"

    data = get_data(category_sql)

    for row in data:
        row['formatted_deadline'] = format_deadline(row['job_deadline'])
        row['formatted_pay'] = format_pay(row['job_pay'])

    paginated_data, has_prev, has_next, total_pages = paginate_data(data, page, per_page)

    # 페이지 번호 목록 생성
    page_numbers = list(range(max(1, page - 2), min(total_pages, page + 2) + 1))

    return render_template('category.html', data=paginated_data, has_prev=has_prev, has_next=has_next, page=page,
                           page_numbers=page_numbers, total_pages=total_pages)


@app.route('/region')
def region_page():
    return render_template('region.html')

@app.route('/personal')
def personal_page():
    return render_template('personal.html')

if __name__ == "__main__":
    app.run()