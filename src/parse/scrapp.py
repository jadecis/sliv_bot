import requests
from bs4 import BeautifulSoup
from loader import api
import undetected_chromedriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

headers_tg={
        "user-agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "sec-ch-ua-platform" : "Windows",
        'sec-ch-ua' : '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"'
    }

def get_inf_tg(link, user_id=None):
    try:
        response= requests.get(url=link, headers=headers_tg)
        if response.status_code >= 200 and response.status_code <= 299:
            soup= BeautifulSoup(response.text, 'lxml')
            name= soup.find('div', class_='tgme_page_title').find('span').text
            if user_id:
                photo_link= soup.find('img', class_="tgme_page_photo_image")
                if photo_link != None:
                    img= requests.get(photo_link.get('src'))
                    with open(f'src/change/avatar/{user_id}.jpg', 'wb') as file:
                        file.write(img.content)
            if name != None:
                return name
            else:
                raise Exception
    except Exception as ex:
        print(ex)
        return None
    
async def get_inf_vk(link, user_id=None):
    id= link.split('/')[-1]
    try:
        res= await api.users.get(user_ids=id,              
                    fields=
                    ['sex',
                    'photo_50'])
        photo_link=res[0].photo_50
        sex= res[0].sex
        if sex == sex.female:
            sex= 'w'
        elif sex ==  sex.male:
            sex = 'm'
        else:
            sex = None
        name= f"{res[0].first_name} {res[0].last_name}"
        id_vk= res[0].id
        if user_id:
            img= requests.get(photo_link)
            with open(f'src/change/avatar/{user_id}.jpg', 'wb') as file:
                file.write(img.content)
        print(name, sex, id_vk)
        return [name, sex, id_vk]
    except Exception as ex:
        print(ex)
        return None
    
async def get_inf_inst(link, user_id=None):
    options = undetected_chromedriver.ChromeOptions()
    options.headless=True
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    options.add_argument('--no-sandbox')
    executable_path = os.path.join(os.getcwd(), 'chromedriver.exe')
    print(executable_path)
    driver = undetected_chromedriver.Chrome(options=options, executable_path=executable_path)
    try:
        driver.get('https://frominsta.net/ru/profile-picture.html')
        time.sleep(1)
        link_s=  driver.find_element(By.XPATH, '//input[@class="form-control"]')
        print(link)
        link_s.send_keys(f'{link}')
        time.sleep(1)
        link_s.send_keys(Keys.ENTER)
        time.sleep(10)
        name= driver.find_element(By.XPATH, '//span[@class="profile_name"]')
        if user_id:
            img= driver.find_element(By.XPATH, '//div[@class="profile_picture_block"]/a/img')
            res= requests.get(img.get_attribute('src'))
            with open(f'src/change/avatar/{user_id}.jpg', 'wb') as f:
                f.write(res.content)
        return name.text            
    except Exception as ex:
        print(ex)
        return None
    finally:
        driver.close()
        driver.quit()