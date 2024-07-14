import schedule
import time
from jobCollection import insert_data
from DB import delete_db

def message():
    print("데이터 수집")

schedule.every().day.at("00:00").do(delete_db)
schedule.every().day.at("00:01").do(insert_data)

while True:
    schedule.run_pending()
    time.sleep(1)