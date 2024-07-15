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
    insert_sql = ("INSERT INTO announcement (job_title, job_link, job_categorie, job_region, job_startline, job_deadline, "
                  "job_career, job_education, job_pay, job_employmentType, job_worktype, job_welfare) "
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(insert_sql, (jobData['name'], jobData['href'], jobData['categorie'], jobData['region'], jobData['startday'], jobData['dday'], jobData['career'],
                                jobData['Education'], jobData['pay'], jobData['employmentType'], jobData['workType'], jobData['welfare']))
    db.commit()

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

def get_data_full(full_sql):
    try:
        cursor.execute(full_sql)
        data = cursor.fetchall()
        print(data)
        return data
    finally:
        db.close()


if __name__ == "__main__":
    get_data_full()
