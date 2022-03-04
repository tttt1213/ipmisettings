from distutils.log import error
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


#WEBドライバのパスを通す
PATH = ("C:\driver\chromedriver.exe")

#ドライバ、オプション設定
op = Options()
op.add_argument('--ignore-certificate-errors')
op.add_argument('--ignore-ssl-errors')
op.add_argument('--start-maximized') 
#op.add_experimental_option("debuggerAddress", "127.0.0.1:80")
driver = webdriver.Chrome(executable_path=PATH,options=op)


#置き換え
#ログイン情報(IPMIアドレス、ユーザー名、パスワード)を変数に入れる


address = "http://192.168.20.72"
target_name = "ADMIN"
target_password = "ADMIN"


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
time.sleep(1)


"""

import time
time.sleep(10)


#マウスオーバー
xpath = '//*[@id="yui-gen2"]'
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.move_to_element(driver.find_element_by_xpath(xpath)).perform()
driver.find_element_by_xpath(xpath).click()

webdriver.ActionChains(driver).context_click(driver.find_element_by_xpath(xpath)).perform()

xpath = '//*[@id="configuration"]'
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.move_to_element(driver.find_element_by_xpath(xpath)).perform()
driver.find_element_by_xpath(xpath).click()

webdriver.ActionChains(driver).context_click(driver.find_element_by_xpath(xpath)).perform()

xpath = '//*[@id="config"]'
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.move_to_element(driver.find_element_by_xpath(xpath)).perform()
driver.find_element_by_xpath(xpath).click()

webdriver.ActionChains(driver).context_click(driver.find_element_by_xpath(xpath)).perform()
"""
