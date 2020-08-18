import random
import time
import math
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select

#MAIN
LINKTOVID = 'https://www.youtube.com/watch?v=IG6u8Zw4zTI' #CHANGE TO CHANGE VIDEO
NUMBERPLAYS = 1000


for i in range(0,NUMBERPLAYS):
    chromedriver = "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/chromedriver"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    bot = webdriver.Chrome(executable_path=chromedriver,options=chrome_options)
    bot.get(LINKTOVID)
    time.sleep(random.uniform(3.0, 5.0))
    #playButton = bot.find_element_by_id('guide-icon')
    #if(random.randrange(1,2)==1):
        #playButton.click()
    #else:
        #playButton.send_keys(" ")
    time.sleep(random.uniform(60.0, 120.0))
    bot.close()
    time.sleep(random.uniform(10.0, 30.0))
