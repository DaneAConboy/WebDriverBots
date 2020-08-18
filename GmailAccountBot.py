import random
import time
import math
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select

class CreateBot:
    def __init__(self):
        chromedriver = "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/chromedriver"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.bot = webdriver.Chrome(executable_path=chromedriver,options=chrome_options)
        self.bot.get('https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgoogle%26oq%3Dgoogle%26aqs%3Dchrome..69i57j69i60l5.104j0j4%26sourceid%3Dchrome%26ie%3DUTF-8&hl=en&dsh=S335653717%3A1570854873041302&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')
        #FIRST NAME GENERATOR
        gender = random.randrange(1,2)
        returnVal = ""
        if(gender == 1):
            filesize = 4275         
            offset = random.randrange(1,filesize)
            f = open("data-files/female-first-names.txt", "r")
            f.seek(offset)
            f.readline()
            self.rfirstName = f.readline().lower()
            self.gender = "female"
        else:
            filesize = 4162         
            offset = random.randrange(1,filesize)
            f = open("data-files/male-first-names.txt", "r")
            f.seek(offset)
            f.readline()
            self.rfirstName = f.readline().lower()
            self.gender = "male"

        #LAST NAME GENERATOR
        filesize = 88600         
        offset = random.randrange(1,filesize)
        f = open("data-files/last-names.txt", "r")
        f.seek(offset)
        f.readline()
        self.rlastName = f.readline().lower()

        #PASSWORD GENERATOR
        randomInt = random.randrange(1,100)
        pass1 = ""
        pass2 = ""
        if(randomInt >= 90):
            filesize = 998         
            offset = random.randrange(1,filesize)
            f = open("data-files/random-passwords-2.txt", "r")
            f.seek(offset)
            f.readline()
            pass2 = f.readline()
            offset = random.randrange(1,filesize)
            f.seek(offset)
            f.readline()
            pass1 = f.readline()
        elif(randomInt < 30):
            filesize = 42438         
            offset = random.randrange(1,filesize)
            f = open("data-files/random-passwords.txt", "r")
            f.seek(offset)
            f.readline()
            pass2 = f.readline()             
            pass1 = self.rfirstName
        elif(randomInt < 40):
            filesize = 42438         
            offset = random.randrange(1,filesize)
            f = open("data-files/random-passwords.txt", "r")
            f.seek(offset)
            f.readline()
            pass2 = f.readline()             
            pass1 = self.rlastName 
        else:
            filesize = 42438         
            offset = random.randrange(1,filesize)
            f = open("data-files/random-passwords.txt", "r")
            f.seek(offset)
            f.readline()
            pass2 = f.readline()
            offset = random.randrange(1,filesize)
            f.seek(offset)
            f.readline()
            pass1 = f.readline()
        if(randomInt % 2 == 0):
            self.password = (pass1+pass2).replace("\n","",2)
        else:
            self.password = (pass2+pass1).replace("\n","",2)

        #EMAIL GENERATOR
        filesize = 30000         
        offset = random.randrange(1,filesize)
        f = open("data-files/random-passwords.txt", "r")
        f.seek(offset)
        f.readline()
        firstHalf = f.readline()
        offset = random.randrange(1,filesize)
        f.seek(offset)
        f.readline()
        secondHalf = f.readline()
        self.username = firstHalf[0:(len(firstHalf)-2)] + secondHalf[0:3]
        
    def randomHigherLess(self,minNum,maxNum):
        dist = abs(random.randrange(0,1) - random.randrange(0,1))
        return math.floor(dist * (1 + maxNum - minNum) + minNum)
    
    def type_first_name(self):
        firstName = self.bot.find_element_by_id("firstName")
        sleepTime = bot.randomHigherLess(0.1, 5.5)
        for i in range( len(self.rfirstName)-1 ):
            if(i == 0):
                letter = self.rfirstName[i].upper()
            else:
                letter = self.rfirstName[i]
            firstName.send_keys(letter)
            time.sleep(sleepTime + random.uniform(0.1, 0.2)) #random sleep for typing
            
    def type_last_name(self):
        lastName = self.bot.find_element_by_id("lastName")
        sleepTime = bot.randomHigherLess(0.1, 5.5)
        for i in range( len(self.rlastName)-1 ):
            if(i == 0):
                letter = self.rlastName[i].upper()
            else:
                letter = self.rlastName[i]
            lastName.send_keys(letter)
            time.sleep(sleepTime + random.uniform(0.1, 0.2)) #random sleep for typing

    def type_get_username(self):
        username = self.bot.find_element_by_id("username")
        randomInt = random.randrange(1,4)
        if(randomInt > 6):
            givenName = username.get_attribute('data-initial-value')
            self.username=givenName
        else:
            username.clear()
            sleepTime = bot.randomHigherLess(0.1, 5.5)
            for i in range( len(self.username)):
                letter = self.username[i]
                username.send_keys(letter)
                time.sleep(sleepTime + random.uniform(0.1, 0.2)) #random sleep for typing
            username.send_keys("\n")
            
    def type_password(self):
        password = self.bot.find_element_by_name("Passwd")
        password.clear()
        sleepTime = bot.randomHigherLess(0.1, 5.5)
        for i in range(2):
            for i in range( len(self.password)):
                letter = self.password[i]
                password.send_keys(letter)
                time.sleep(sleepTime + random.uniform(0.1, 0.2)) #random sleep for typing
            password.send_keys("\t")
            time.sleep(sleepTime + random.uniform(0.4, 1))
            password = self.bot.find_element_by_name("ConfirmPasswd")
        password.send_keys("\n")
        
    def username_with_numbers(self):
        username = self.bot.find_element_by_id("username")
        randomInt = random.randrange(1,4)
        print(randomInt)
        if(randomInt > 2):
            givenName = username.get_attribute('data-initial-value')
            self.username=givenName
        else:
            username.clear()
            sleepTime = bot.randomHigherLess(0.1, 5.5)
            self.username += str(random.randrange(0,9))
            for i in range( len(self.username)):
                letter = self.username[i]
                username.send_keys(letter)
                time.sleep(sleepTime + random.uniform(0.1, 0.2)) #random sleep for typing
            username.send_keys("\n")
        
#MAIN
bot = CreateBot()
time.sleep(bot.randomHigherLess(1.0, 5.0))
bot.type_first_name()
time.sleep(bot.randomHigherLess(1.0, 5.0))
bot.type_last_name()
time.sleep(bot.randomHigherLess(3.0, 4.0))
bot.type_get_username()
time.sleep(bot.randomHigherLess(1.0, 2.0))
bot.type_password()
time.sleep(bot.randomHigherLess(3.0, 4.0))

madeToPhone = False
while(not madeToPhone):
    try:
        bot.bot.find_element_by_id("phoneNumberId")
        madeToPhone = True
    except:
        bot.username_with_numbers()
        time.sleep(bot.randomHigherLess(1.0, 2.0))
        bot.type_password()
time.sleep(bot.randomHigherLess(1.0, 2.0))


    
print("FIRST NAME: " + bot.rfirstName)
print("LAST NAME: " + bot.rlastName)
print("PASSWORD: " + bot.password)
print("USERNAME: " + bot.username)
print('DONE')
