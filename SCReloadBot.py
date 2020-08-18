import random
import time
import math
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

#MAIN
LINKTOSONG = 'https://soundcloud.com/gasoiid/s0-n2u'
NUMBERPLAYS = 1000


for i in range(0,NUMBERPLAYS):
    
    PROXY = "74.113.169.129:47208" # IP:PORT or HOST:PORT 

    chromedriver = "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/chromedriver"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    
    bot = webdriver.Chrome(executable_path=chromedriver,options=chrome_options)  
    bot.get(LINKTOSONG)
    
    time.sleep(random.uniform(3.0, 5.0))
    playButton = bot.find_element_by_class_name('playButton')
    if(random.randrange(1,2)==1):
        playButton.click()
    else:
        playButton.send_keys(" ")
    time.sleep(random.uniform(10.0, 150.0))
    bot.close()
    time.sleep(random.uniform(10.0, 30.0))
    print("NUMBER IN LOOP: " + i)
    print("PROXY NUMBER: " + PROXY)
