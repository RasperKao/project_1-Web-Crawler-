def find_my_fortune():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
    from selenium.webdriver.support.ui import Select
    import requests

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome("chromedriver", options=options)

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

    post_1 = {
        'buy': '1',
        'joyday': 'DAYgbrwoth4',
        'Name_1': '王大明',
        'OptGdr_1': '1',
        'Option1_1': '3',
        'IYear_1': '1991',
        'IMonth_1': '6',
        'IDay_1': '21',
        'IHour_1': '辰時(07:00~08:59)',
        'M10a': '資料正確，送出',
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '235',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'ASPSESSIONIDQARSDCRR=CBNDLGKDNMIJHMIBEDJNDHAE;  gads=ID=18d236e627e6739c-2272f3ae6dc60077:T=1615868890:RT=1615868890:S=ALNI_MavgjY8bhr3p1fRcFCptsAJ8AysHg',
        'Host': 'www.joyglobal.cc',
        'Origin': 'http://www.joyglobal.cc',
        'Referer': 'http://www.joyglobal.cc/joyday1.asp',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    imgs = driver.find_elements_by_css_selector(".s2 img")

    pic_1 = imgs[0].get_attribute("src")
    print(pic_1)
    response = requests.get(pic_1, headers=headers, stream=True, verify=False)
    print(response.raw.read())

    driver.quit()

    return pic_1
