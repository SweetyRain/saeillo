from flask import Flask, request, render_template, flash, redirect, url_for
from DB import get_data, insert_notice
from datetime import datetime
import requests

app = Flask(__name__)
app.secret_key = '1234'

#마감일 포맷 변경
def format_deadline(deadline):
    if deadline == 30000000:
        return "채용시까지"
    else:
        return datetime.strptime(str(deadline), '%Y%m%d').strftime('%Y년 %m월 %d일')

def format_worktype(worktype):
    format_worktype = f'주 {worktype}일 근무'
    return format_worktype

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
def saeillo(name = None):
    return render_template('main.html', name=name)

@app.route('/full')
def full_page():
    full_sql = "SELECT job_index, job_title, job_link, job_region, job_deadline, job_worktype, job_pay FROM announcement"
    data = get_data(full_sql)

    for row in data:
        row['formatted_deadline'] = format_deadline(row['job_deadline'])

        row['formatted_worktype'] = format_worktype(row['job_worktype'])

    return render_template('full.html', data=data)
@app.route('/category')
def category_page():
    value = request.args.get('value', default='조리', type=str)
    print(value)
    category_sql = (f"SELECT job_index, job_title, job_link, job_region, job_deadline, job_worktype, job_pay FROM announcement WHERE job_categorie = '{value}'")

    data = get_data(category_sql)

    for row in data:
        row['formatted_deadline'] = format_deadline(row['job_deadline'])
        row['formatted_worktype'] = format_worktype(row['job_worktype'])

    #count_sql = f"SELECT COUNT(*) FROM announcement WHERE job_categorie = '{value}'"

    return render_template('category.html', data=data)

@app.route('/region')
def region_page():
    value = request.args.get('value', default='서울 강남구', type=str)
    print(value)
    address = list(value.split())
    if len(address) == 1:
        region_sql = (
            f"SELECT job_index, job_title, job_link, job_region, job_deadline, job_worktype, job_pay FROM announcement "
            f"WHERE job_fullregion LIKE '%{address[0]}%''")

    elif len(address) == 2:
        region_sql = (
            f"SELECT job_index, job_title, job_link, job_region, job_deadline, job_worktype, job_pay FROM announcement "
            f"WHERE job_fullregion LIKE '%{address[0]}%' AND job_fullregion LIKE '%{address[1]}%'")

    else:
        region_sql = (
            f"SELECT job_index, job_title, job_link, job_region, job_deadline, job_worktype, job_pay FROM announcement "
            f"WHERE job_fullregion LIKE '%{address[0]}%' AND job_fullregion LIKE '%{address[1]}%' AND job_fullregion LIKE '%{address[2]}%'")

    data = get_data(region_sql)
    print(data)
    for row in data:
        row['formatted_deadline'] = format_deadline(row['job_deadline'])
        row['formatted_worktype'] = format_worktype(row['job_worktype'])

    # count_sql = f"SELECT COUNT(*) FROM announcement WHERE job_categorie = '{value}'"

    return render_template('region.html', data=data)

@app.route('/personal', methods = ['GET', 'POST'])
def personal_page():
    values = request.form.get('value', default='서울 강남구', type=str)
    regions = values.split() if values else []
    holidays = request.form.getlist('holiday-checkbox', type=int)

    personal_sql = (
        "SELECT job_index, job_title, job_link, job_region, job_deadline, job_worktype, job_pay "
        "FROM announcement "
        "WHERE"
    )

    # 지역 조건 추가
    params = []
    if regions:
        region_conditions = " AND ".join([f"job_fullregion LIKE '%{r}%'" for r in regions])
        personal_sql += f" ({region_conditions})"
        params.extend([f"%{r}%" for r in regions])

    # 근무일수 조건 추가
    if holidays:
        if regions:
            personal_sql += " AND"
        holiday_conditions = " OR ".join([f"job_worktype = {h}" for h in holidays])
        personal_sql += f" ({holiday_conditions})"
        params.extend(holidays)

    print(personal_sql)
    data = get_data(personal_sql)
    for row in data:
        row['formatted_deadline'] = format_deadline(row['job_deadline'])
        row['formatted_worktype'] = format_worktype(row['job_worktype'])

    return render_template('personal.html', data=data)

@app.route('/detail/<int:index>')
def detail_page(index):
    detail_sql = (f"SELECT * FROM announcement WHERE job_index = '{index}'")

    data = get_data(detail_sql)
    print(data)
    for row in data:
        row['formatted_deadline'] = format_deadline(row['job_deadline'])
        row['formatted_worktype'] = format_worktype(row['job_worktype'])

    print(data)
    return render_template('detail.html', data=data)

@app.route('/notice')
def notice_page():
    notice_sql = (f'SELECT notice_index, notice_title, notice_manager, notice_content, notice_registration FROM notice')
    data = get_data(notice_sql)

    for row in data:
        row['formatted_date'] = format_deadline(row['notice_registration'])

    return render_template('notice.html', data=data)

@app.route('/notice/<int:index>')
def notice_contents_page(index):
    detail_sql = (f"SELECT * FROM notice WHERE notice_index = '{index}'")
    data = get_data(detail_sql)

    for row in data:
        row['formatted_date'] = format_deadline(row['notice_registration'])

    return render_template('noticeContents.html', data=data)

@app.route('/writenotice', methods = ['GET', 'POST'])
def writenotice_page():
    checking_password = "1234"
    now = datetime.today()
    today = int(now.strftime('%Y%m%d'))
    error = None

    if request.method == 'POST':
        title = request.form['title']
        manager = request.form['manager']
        password = request.form['password']
        content = request.form['content']
        registration_date = today
        notice_data = {'title': title, 'manager': manager, 'password': password, 'content': content,
                       'registration_date': registration_date}
        if password != checking_password:
            error = "올바르지 않은 비밀번호입니다. \n 관리자만 공지 등록이 가능합니다."
        else:
            insert_notice(notice_data)
            return redirect(url_for('notice_page'))
    return render_template('writeNotice.html', error = error)


if __name__ == "__main__":
    app.run(debug=True)