import os
import time
import json
import time_compare
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy import selector
from Setup import get_time

options = webdriver.ChromeOptions()
options.add_argument('lang=en')
caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  complete
caps["pageLoadStrategy"] = "eager"  #  interactive
# caps["pageLoadStrategy"] = "none"   #  undefined
br = webdriver.Chrome("C:\\Users\\USER\\source\\repos\\Get_Toy\\chromedriver.exe", options=options, desired_capabilities=caps)

def login(url):
    br.get(url["start_up"])
    while True:
        print("---開始登入{}---".format(url["start_up"]))
        try:
            time.sleep(3)
            if br.find_element_by_xpath("//div[@class='site-nav-sign']/a[1]"):
                br.find_element_by_xpath("//div[@class='site-nav-sign']/a[1]").click()
                time.sleep(3)
                if br.find_element_by_xpath("//i[@class='iconfont icon-qrcode']"):
                    br.find_element_by_xpath("//i[@class='iconfont icon-qrcode']").click()
                    print("請請掃碼登入")
            while True:
                try:
                    time.sleep(3)
                    logged_user = br.find_element_by_class_name('site-nav-login-info-nick').text
                    if str(logged_user) == "honglk1220":
                        print("登入成功")
                        login_status = True
                        return login_status

                except Exception as e:
                    time.sleep(5)
                    print("登入進行中....")
            else:
                return "找不到登入鈕"
        except Exception as e:
            time.sleep(0.4)
            print(e)
            print("重新嘗試")

def get_good_prop(data):
    now_time = get_time()
    print(now_time)
    try:
        for item in data:
            br.execute_script("window.open('{}')".format(item["url"]))
            item["tab_id"] = br.window_handles[-1]
            br.switch_to_window(item["tab_id"])
            #br.refresh()
            good_prop = br.find_elements_by_xpath("//ul[@id='J_AttrUL']/li")
            print(len(good_prop))
            item["brand"] = (str(good_prop[0].text)[3:]).replace("\n","").strip(" ")
            item["name"] = (str(good_prop[1].text)[3:]).replace("\n","").strip(" ")
            item["category"] = (str(good_prop[2].text)[5:]).replace("\n","").strip(" ")
            item["status"] = (str(good_prop[3].text)[5:]).replace("\n","").strip(" ")
            item["size"] = (str(good_prop[4].text)[3:]).replace("\n","").strip(" ")
            print("{}-{} 商品參數獲取完成".format(item["id"],item["name"]))

            while True:
                try:
                    print("---請在網站選取品項、數量，以及確認寄送地址---\n---設定完畢請輸入y---")
                    address_check = str(input())
                    if address_check == "y" or "Y":
                        time_compare_result = time_compare.tc(data)
                        if time_compare_result:
                            br.refresh()
                            start_order()
                    else:
                        raise ValueError
                    
                    #寄送地址確認
                    address = br.find_elements_by_xpath("//div[@class='addr-item-wrapper TwoRow addr-selected addr-default']/div[@class='inner-infos']/div")
                    for add in address:
                        print(add.text)
                    go_btn = br.find_element_by_xpath("/div[@class='wrapper']/a[@class='go-btn']")
                    

                except ValueError:
                    print("type error")
                except Exception as e:
                    print(e)
        print("共啟動{}個Tab".format(len(br.window_handles)))
        return data
            #br.get(item)    
    except Exception as e:
        print(e)


def start_order():
    #尋找並點選下單按鈕
    print("---下單中---")
    order_btn = br.find_element_by_xpath(".//div[@class='tb-btn-buy tb-btn-sku']/a[@id='J_LinkBuy']")
    order_btn.click()
    #payment_btn = br.find_element_by_link_text("提交订单")
    #payment_btn.click()
    return