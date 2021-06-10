# 題目1:http://www.joyglobal.cc/joyday1.asp
# from selenium import webdriver
# import requests
# import time

# from selenium.webdriver.support.ui import Select
# from selenium.webdriver import ActionChains
# import pyautogui
# from datetime import datetime as d
# import os
# import shutil
# import smtplib
# from email.mime.multipart import MIMEMultipart #email內容載體
# from email.mime.text import MIMEText #用於製作文字內文
# from email.mime.image import MIMEImage
# from email.mime.base import MIMEBase #用於承載附檔
# from email import encoders #用於附檔編碼
# import schedule
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
# from urllib.request import urlretrieve
# import re

def search_my_fortune():
    from selenium import webdriver
    import time
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver import ActionChains
    import pyautogui

    driver = webdriver.Chrome("chromedriver")
    driver.get("http://www.joyglobal.cc/joyday1.asp")
    time.sleep(1)

    name = driver.find_element_by_name("Name_1")
    name.send_keys("王大明")
    time.sleep(1)

    gender = driver.find_element_by_css_selector('input[type="radio"][value="1"]')
    gender.click()
    time.sleep(1)

    calender = driver.find_elements_by_name("Option1_1")[0]
    calender.click()
    time.sleep(1)

    # https://jzchangmark.wordpress.com/2015/03/05/%E9%80%8F%E9%81%8E-selenium-%E6%93%8D%E4%BD%9C%E4%B8%8B%E6%8B%89%E5%BC%8F%E9%81%B8%E5%96%AE-select/
    select_year = Select(driver.find_element_by_name("IYear_1"))
    year = select_year.select_by_visible_text("1991")

    time.sleep(1)

    select_month = Select(driver.find_element_by_name("IMonth_1"))
    month = select_month.select_by_index(5)

    time.sleep(1)

    select_date = Select(driver.find_element_by_name("IDay_1"))
    date = select_date.select_by_visible_text("21")

    time.sleep(1)

    select_hour = Select(driver.find_element_by_name("IHour_1"))
    hour = select_hour.select_by_index(4)

    time.sleep(2)

    submit = driver.find_element_by_name("M10a")
    submit.click()

    time.sleep(2)

    imgs = driver.find_elements_by_css_selector(".s2 img")
    pic_1 = imgs[0]

    action = ActionChains(driver).move_to_element(pic_1)
    action.context_click(pic_1).perform()
    time.sleep(2)

    # pyautogui
    pyautogui.typewrite(['down', 'enter'], interval=1)

    # https://ithelp.ithome.com.tw/articles/10230717
    driver.switch_to.window(driver.window_handles[1])
    # driver.switch_to.window(driver.window_handles[0])

    url = driver.current_url
    print(url)
    driver.quit()
    return url


def save_my_pic(url):
    import requests
    from datetime import datetime as d
    import os
    import shutil

    # https://www.itread01.com/content/1545450012.html
    my_dir = f"my_{(d.today().month)}_month_fortune"
    my_pic_dir = f"./{my_dir}/my_day_{d.date(d.today())}.jpg"

    if not os.path.exists(my_dir):
        os.mkdir(my_dir)
    # urlretrieve(url, f"./{my_dir}/my_day_{d.date(d.today())}.jpg")

    response = requests.get(url, stream=True, verify=False)
    with open(my_pic_dir, "wb") as f:
        # f.write(response.raw.read())
        shutil.copyfileobj(response.raw, f)
    return my_pic_dir


# https://medium.com/jeasee%E9%9A%A8%E7%AD%86/python-email%E5%AF%84%E4%BF%A1-ba2b5eb05d6b
# https://www.itread01.com/content/1550010974.html


def send_mail(my_pic_dir):
    import os
    from datetime import datetime as d
    import smtplib
    from email.mime.multipart import MIMEMultipart  # email內容載體
    from email.mime.text import MIMEText  # 用於製作文字內文
    from email.mime.image import MIMEImage

    account = "raspertest@gmail.com"

    # 環境變量設定https://cuiqingcai.com/8947.html
    # https://www.youtube.com/watch?v=IolxqkL7cD8
    password = os.environ.get("password")
    recepeint = "raspertest@gmail.com"

    mine = MIMEMultipart()
    mine["Content-Type"] = "image/jpeg"
    mine["Content-Disposition"] = f'attachment; filename="{my_pic_dir}"'  # 寫你的檔案名讓他可以找到
    mine["Subject"] = f"這是{d.date(d.today())}的運勢"  # 撰寫郵件標題
    mine["From"] = f"Rasper[{account}]"  # 撰寫你的暱稱或是信箱
    mine["To"] = f"Rasper[{recepeint}]"  # 撰寫你要寄的人
    # mime["Cc"] = "@gmail.com, @gmail.com"  # 副本收件人
    image = MIMEImage(open(rf'{my_pic_dir}', 'rb').read(), _subtype="application")
    image.add_header('Content-Disposition', 'attachment', filename='img.jpg')
    mine.attach(image)
    # 撰寫內文內容，以及指定格式為plain，語言為中文
    mine.attach(MIMEText("這是今日的運勢圖，請查看", "plain", "utf-8"))
    msg = mine.as_string()  # 將msg將text轉成str
    print(msg)

    smtp = smtplib.SMTP("smtp.gmail.com")  # googl的ping
    smtp.ehlo()  # 申請身分
    smtp.starttls()  # 加密文件，避免私密信息被截取
    smtp.login(account, password)
    status = smtp.sendmail(from_addr=account, to_addrs=recepeint, msg=msg)

    if status == {}:
        print("郵件傳送成功!")
    else:
        print("郵件傳送失敗!")
    smtp.quit()

















