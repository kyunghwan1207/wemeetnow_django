from http import HTTPStatus
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import os

# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from .models import User;
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


@csrf_exempt
def wemeet_1(request):
    print('Enter/wemeet_1/request: ', request)
    if request.method == 'POST':
        print('wemeet_1/req.body: ', request.body)
        data = json.loads(request.body)
        name = data.get('name', None)
        print('wemeet_1/POST.get(name): ', name)
        start_address = data.get('startAddress', None)
        print('request.body.startAddress: ', start_address)
        end_address = data.get('endAddress', None)
        print('request.body.endAddress: ', end_address)
        result = scrap(start_address, end_address)
        new_user = User(name=name, start_address=start_address, end_address=end_address, time=result)
        new_user.save()
        print('wemmet-1/save success')
    return HttpResponse(HTTPStatus.ACCEPTED)
    

@csrf_exempt
def wemeet_2(request):
    print('Enter/wemeet_22/request: ', request)
    if request.method == 'POST':
        print('wemeet_2/req.body: ', request.body)
        data = json.loads(request.body)
        name = data.get('name', None)
        print('wemeet_2/POST.get(name): ', name)
        start_address = data.get('startAddress', None)
        print('request.body.startAddress: ', start_address)
        end_address = data.get('endAddress', None)
        print('request.body.endAddress: ', end_address)
        result = scrap(start_address, end_address)
        new_user = User(name=name, start_address=start_address, end_address=end_address, time=result)
        new_user.save()
        print('wemmet-2/save success')
    return HttpResponse(HTTPStatus.ACCEPTED)

@csrf_exempt
def wemeet_3(request):
    print('Enter/wemeet_333/request: ', request)
    if request.method == 'POST':
        print('wemeet_3/req.body: ', request.body)
        data = json.loads(request.body)
        name = data.get('name', None)
        print('wemeet_3/POST.get(name): ', name)
        start_address = data.get('startAddress', None)
        print('request.body.startAddress: ', start_address)
        end_address = data.get('endAddress', None)
        print('request.body.endAddress: ', end_address)
        result = scrap(start_address, end_address)
        new_user = User(name=name, start_address = start_address, end_address=end_address, time=result)
        new_user.save()
        print('wemmet-3/save success')
    return HttpResponse(HTTPStatus.ACCEPTED)

@csrf_exempt
def finalResult(request):
    time.sleep(10)
    user_list = User.objects.all()
    print('finalResult/user_list: ', user_list)
    final_list = []
    for user in user_list:
        print('user: ', user)
        obj = {}
        print('user.name: ', user.name)
        obj['name'] = user.name
        obj['startAddress'] = user.start_address
        obj['finalTime'] = user.time
        final_list.append(obj)
    User.objects.all().delete()
    final_obj = {}
    final_obj['data'] = final_list
    print('JsonResponse(final_obj): ', JsonResponse(final_obj))
    return JsonResponse(final_obj)
'''
{
    "data": 
    [{
        "name": "?????????",
        "startAddress": "????????? ????????? ???????????? ????????? 595",
        "finalTime": "52???"
    }, {
        "name": "?????????",
        "startAddress": "????????? ???????????? ????????? 525",
        "finalTime": "1??? 7???"
    }, {
        "name": "?????????",
        "startAddress": "??????????????? ????????? ???????????? 49",
        "finalTime": "36???"
    }]  
}

'''

# ????????? ?????? ???????????? ?????? ?????????
def scrap(start_addr, end_addr):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')        # Head-less ??????
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(executable_path='C:\\Users\\kyung\\Downloads\\chromedriver_win32\\chromedriver.exe', options=options)

    url = 'https://map.naver.com/v5/directions/-/-/-/transit?c=14137976.2256279,4513751.5354669,13,0,0,0,dh'
    driver.get(url)
    driver.set_window_size(900, 900)
    print('====success====')

    # ???????????? input?????????
    start_addr_element = driver.find_element("xpath", '//*[@ng-version="11.2.14"]/layout/div[3]/div[2]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/directions-search/div[1]/directions-search-box[1]/div/div/div[1]/input')
    time.sleep(0.05)
    start_addr_element.click()
    time.sleep(1.1)
    start_addr_element.send_keys(start_addr) # ???????????? ??????
    time.sleep(1.1)
    # ?????? ?????? fix
    start_fix = driver.find_element("xpath", '//*[@ng-version="11.2.14"]/layout/div[3]/div[2]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/directions-search/div[1]/directions-search-box[1]/div/directions-search-box-instant-search/div/instant-search-list/div/div/nm-list-container[2]/div/nm-list/ul/li/a')
    time.sleep(0.05)
    start_fix.click()
    time.sleep(1.1)
    # ???????????? input ?????????
    end_addr_element = driver.find_element("xpath", '//*[@ng-version="11.2.14"]/layout/div[3]/div[2]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/directions-search/div[1]/directions-search-box[2]/div/div/div[1]/input')
    time.sleep(0.05)
    end_addr_element.click()
    time.sleep(1.1)
    end_addr_element.send_keys(end_addr) # ???????????? ??????
    time.sleep(1.1)
    # ?????? ?????? fix
    end_fix = driver.find_element("xpath", '//*[@ng-version="11.2.14"]/layout/div[3]/div[2]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/directions-search/div[1]/directions-search-box[2]/div/directions-search-box-instant-search/div/instant-search-list/div/div/nm-list-container[2]/div/nm-list/ul/li/a')
    time.sleep(0.05)
    end_fix.click()
    time.sleep(1.1)
    # ?????? ???????????? ?????? ??????
    result = ''
    try:
        time_list = driver.find_elements(By.CSS_SELECTOR, '.value.ng-star-inserted')
        time_hour = time_list[0].text
        time_min = None
        if(int(time_hour) < 5):
            time_min = time_list[1].text
        if(time_min == None):
            result = time_hour + '???'
        else:
            result = time_hour + '??? ' + time_min + '???'
    
    except:
        result = '????????? ?????? ??? ????????????.'
    return result



    # ???????????? input className
    # .directions-search-input-el.input_search.ng-pristine.ng-valid.ng-touched 
    # ????????????
    # .directions-search-input-el.input_search ng-pristine.ng-valid.ng-touched
    # place holder ClassName
    # .input_label.blind
