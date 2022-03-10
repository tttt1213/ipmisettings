#! /usr/bin/env python
# encoding:utf-8

from concurrent.futures.process import _chain_from_iterable_of_lists
from distutils.log import error
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def chrome_login(IPADDRESS,PASSWORD):

    #WEBドライバのパスを通す
    PATH = ("/home/defaultuser/work/ipmisettings/chromedriver")

    #ドライバ、オプション設定
    op = Options()
    op.add_argument('--ignore-certificate-errors')
    op.add_argument('--ignore-ssl-errors')
    op.add_argument('--start-maximized') 
    driver = webdriver.Chrome(executable_path=PATH,options=op)

    #ログイン情報(IPMIアドレス、ユーザー名、パスワード)を変数に入れる
    address = "http://" + IPADDRESS 
    target_name = "ADMIN"
    target_password = PASSWORD

    #IPMIのwebページ開く
    driver.get(address)
    #driver.execute_script("window.open('address');")

    #詳細表示クリック(ボタンがない場合は止まってしまうので、例外処理)
    try :
        driver.find_element_by_id("details-button").click()
        #進むクリック
        driver.find_element_by_id("proceed-link").click()
    except :
            print ("errorrrrrrrrrrrrrrrrrrrrrrrrrrrrr")

    #webページにユーザ名入力
    element_target_name = driver.find_element_by_name("name")
    element_target_name.send_keys(target_name)
    time.sleep(1)

    #webページにパスワード入力
    element_target_password = driver.find_element_by_name("pwd")
    element_target_password.send_keys(target_password)
    time.sleep(1)

    #ログインボタンをクリック
    driver.find_element_by_id("login_word").click()
    time.sleep(100)