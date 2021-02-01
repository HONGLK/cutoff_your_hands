import os
import time
import json
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

url = "https://detail.tmall.com/item.htm?spm=a312a.7700824.w4011-15691211890.24.41945742dYJIMW&id=602412483343&rn=fc058cd0d627f99c2350c0e5ae086c58&abbucket=4&sku_properties=134942334:28316"

options = webdriver.ChromeOptions()
options.add_argument('lang=en')
caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  complete
caps["pageLoadStrategy"] = "eager"  #  interactive
# caps["pageLoadStrategy"] = "none"   #  undefined
try:
    br = webdriver.Chrome("C:\\Users\\USER\\source\\repos\\Get_Toy\\chromedriver.exe", options=options, desired_capabilities=caps)

    br.get(url)
    time.sleep(15)
    print("ready to click")
    btn = br.find_element_by_xpath(".//div[@class='tb-btn-buy tb-btn-sku']/a[@id='J_LinkBuy']")
    btn.click()
    
except Exception as e:
    print(e)