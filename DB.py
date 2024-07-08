import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='!@rain1215@!',
                     db='saeillo_db',
                     charset='utf8')

cursor = db.cursor()

def input_db(jobData):
    insert_sql = ("INSERT INTO announcement (job_title, job_link, job_categorie, job_region, job_deadline, "
                  "job_career, job_education, job_pay, job_employmentType, job_worktype, job_welfare) "
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(insert_sql, (jobData['name'], jobData['href'], jobData['categorie'], jobData['region'], jobData['dday'], jobData['career'],
                                jobData['Education'], jobData['pay'], jobData['employmentType'], jobData['workType'], jobData['welfare']))
    db.commit()
