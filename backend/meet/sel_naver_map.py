# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import os

# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
'''
이름
시작주소
도착장소

User
이름 시작주소 도착장소
'''
def scrap(start_addr, end_addr):
    url = 'https://map.naver.com/v5/directions/-/-/-/transit?c=14137976.2256279,4513751.5354669,13,0,0,0,dh'
    driver.get(url)
    driver.set_window_size(900, 900)
    print('====success====')

    # 출발주소 input창가기
    start_addr_element = driver.find_element("xpath", '//*[@ng-version="11.2.14"]/layout/div[3]/div[2]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/directions-search/div[1]/directions-search-box[1]/div/div/div[1]/input')
    time.sleep(0.05)
    start_addr_element.click()
    time.sleep(1.1)
    start_addr_element.send_keys(start_addr) # 출발주소 입력
    time.sleep(1.1)
    # 출발 주소 fix
    start_fix = driver.find_element("xpath", '//*[@ng-version="11.2.14"]/layout/div[3]/div[2]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/directions-search/div[1]/directions-search-box[1]/div/directions-search-box-instant-search/div/instant-search-list/div/div/nm-list-container[2]/div/nm-list/ul/li/a')
    time.sleep(0.05)
    start_fix.click()
    time.sleep(1.1)
    # 도착주소 input 창가기
    end_addr_element = driver.find_element("xpath", '//*[@ng-version="11.2.14"]/layout/div[3]/div[2]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/directions-search/div[1]/directions-search-box[2]/div/div/div[1]/input')
    time.sleep(0.05)
    end_addr_element.click()
    time.sleep(1.1)
    end_addr_element.send_keys(end_addr) # 도착주소 입력
    time.sleep(1.1)
    # 도착 주소 fix
    end_fix = driver.find_element("xpath", '//*[@ng-version="11.2.14"]/layout/div[3]/div[2]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/directions-search/div[1]/directions-search-box[2]/div/directions-search-box-instant-search/div/instant-search-list/div/div/nm-list-container[2]/div/nm-list/ul/li/a')
    time.sleep(0.05)
    end_fix.click()
    time.sleep(1.1)
    # 최단 대중교통 시간 출력
    result = ''
    try:
        time_list = driver.find_elements(By.CSS_SELECTOR, '.value.ng-star-inserted')
        time_hour = time_list[0].text
        time_min = None
        if(int(time_hour) < 5):
            time_min = time_list[1].text
        if(time_min == None):
            result = time_hour + ' 분'
        else:
            result = time_hour + ' 시 ' + time_min + ' 분'
    
    except:
        result = '시간을 측정할 수 없습니다.'
    print(result)



    # 출발주소 input className
    # .directions-search-input-el.input_search.ng-pristine.ng-valid.ng-touched 
    # 도착주소
    # .directions-search-input-el.input_search ng-pristine.ng-valid.ng-touched
    # place holder ClassName
    # .input_label.blind

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')        # Head-less 설정
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(executable_path='C:\\Users\\kyung\\Downloads\\chromedriver_win32\\chromedriver.exe', options=options)

    # start_addr = "서울특별시 용산구 대사관로 49" # 36 분
    # start_addr = "경기도 고양시 일산동구 호수로 595" # 52분
    # start_addr = "경기도 의정부시 평화로 525" # 1 시 7 분
    start_addr_list = ["서울특별시 용산구 대사관로 49", "경기도 고양시 일산동구 호수로 595", "경기도 의정부시 평화로 525"]
    end_addr = "서울특별시 강남구 역삼로 180"
    for start_addr in start_addr_list:
        scrap(start_addr, end_addr)
