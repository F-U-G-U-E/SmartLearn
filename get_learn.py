# please change the username and password at line 68~70
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re


# In[2]:


def print_title():
    # title
    print("\033[1m%-10s%-10s%-10scoursename\033[0m" % ("notice", "file", "homework"))


# In[3]:


def print_course(name = "default", notice = -1, file = -1, homework = -1):

    # notice
    if notice:
        print("\033[1;31m", end = '') # red
    else:
        print("\033[0m", end = '') # default
    print("%-10s" % notice, end = '')
    
    # file
    if file:
        print("\033[1;31m", end = '') # red
    else:
        print("\033[0m", end = '') # default
    print("%-10s" % file, end = '')
    
    # homework
    if homework:
        print("\033[1;31m", end = '') # red
    else:
        print("\033[0m", end = '') # default
    print("%-10s" % homework, end = '')
    
    print("\033[0m", end = '') # default form
    
    # name
    print(name)
    


# In[4]:


# Open browser
option = webdriver.ChromeOptions()
option.add_argument("headless")
#browser = webdriver.Safari()
browser = webdriver.Chrome("/Users/baowenxuan/Downloads/chromedriver", chrome_options = option)
browser.get("http://learn.tsinghua.edu.cn")


# In[5]:


# Login
username = "bwx16"
password = "FakePassword"

# Input Username
browser.find_element_by_name('i_user').clear()
browser.find_element_by_name('i_user').send_keys(username)

# Input Password
browser.find_element_by_name('i_pass').clear()
browser.find_element_by_name('i_pass').send_keys(password)

# Click
browser.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)


# In[6]:


# Get Info
time.sleep(5)
# Get amount of courses
course_amount = len(browser.find_elements_by_xpath('//*[@id="suoxuecourse"]/*'))
print_title()
for i in range(course_amount):
    # kechengming
    nm = browser.find_element_by_xpath('//*[@id="suoxuecourse"]/dd['+str(i+1)+']/div[2]/div[1]/a').text
    # gonggao
    nt = browser.find_element_by_xpath('//*[@id="suoxuecourse"]/dd['+str(i+1)+']/div[2]/div[2]/ul/li[2]/a/span[2]').text
    nt = int(re.sub("\D", "", nt))
    # wenjian
    fl = browser.find_element_by_xpath('//*[@id="suoxuecourse"]/dd['+str(i+1)+']/div[2]/div[2]/ul/li[3]/a/span[2]').text
    fl = int(re.sub("\D", "", fl))
    # zuoye
    hw = browser.find_element_by_xpath('//*[@id="suoxuecourse"]/dd['+str(i+1)+']/div[2]/div[2]/ul/li[4]/a/span[2]').text
    hw = int(re.sub("\D", "", hw))
    
    # Print the information
    print_course(nm, nt, fl, hw)


# In[7]:


# It is important to quit after using
browser.quit()

