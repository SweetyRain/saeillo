import pymysql
import datetime
from dateutil.relativedelta import relativedelta

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='!@rain1215@!',
                     db='saeillo_db',
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor )

cursor = db.cursor()

def input_db(jobData):
    #DB 수용 길이 넘어가는 공고 삽입하지 않음
    if len(jobData['href']) <= 400:
        insert_sql = ("INSERT INTO announcement (job_title, job_link, job_categorie, job_region, job_startline, job_deadline, "
                      "job_career, job_education, job_pay, job_employmentType, job_worktype, job_welfare) "
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(insert_sql, (jobData['name'], jobData['href'], jobData['categorie'], jobData['region'], jobData['startday'], jobData['dday'], jobData['career'],
                                    jobData['Education'], jobData['pay'], jobData['employmentType'], jobData['workType'], jobData['welfare']))
        db.commit()
    else:
        print(jobData['name'], "DB 삽입 실패\n", jobData['href'])

#데이터 삭제를 위한 오늘 날짜 구하기
now = datetime.datetime.today()
today = int(now.strftime('%Y%m%d'))

#데이터 삭제를 위한 6개월 전 구하기
month_6 = now - relativedelta(months=6)
month_6 = int(month_6.strftime('%Y%m%d'))

print(today, month_6)

def delete_db():
    delete_sql = (f'DELETE FROM announcement WHERE {today} > job_deadline OR job_startline = {month_6}')
    cursor.execute(delete_sql)
    db.commit()

def get_data(sql):
    try:
        with db.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(f"Error fetching data from database: {e}")
        return []

