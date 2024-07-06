import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='!@rain1215@!',
                     db='saeillo_db',
                     charset='utf8')

cursor = db.cursor()
cursor.execute("INSERT INTO announcement(job_index, job_title, job_link, job_deadline, job_region, job_pay) "
               "VALUES (0, 'a', 'b', 0, 'c', 0)")

sql = 'SELECT * from announcement'

# 쿼리 실행
cursor = db.cursor()  # default 튜플 타입으로 받기
# cursor = db.cursor(pymysql.cursors.DictCursor)  # Dictionary 타입으로 받기
cursor.execute(sql)

# 결과 받고 컨트롤하기
data = cursor.fetchall()
print(data)

db.commit()
db.close()