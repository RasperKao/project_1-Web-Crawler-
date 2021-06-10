import time
import schedule
from My_function import search_my_fortune,save_my_pic, send_mail
from another_way_1 import find_my_fortune

#https://schedule.readthedocs.io/en/stable/examples.html

def job():
    my_url = search_my_fortune()
    my_url = find_my_fortune()

    path = save_my_pic(my_url)

    send_mail(path)

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(5)
