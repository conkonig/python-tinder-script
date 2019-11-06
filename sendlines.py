from selenium import webdriver as driver
from selenium.webdriver.support import ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys

facebookEmail = ''
facebookPassword = ''
swipes = 50
# These should get from a file in ./passwords as this folder will be ignored by git

def selectOption(select,texttoselect):
    options = select.find_elements_by_tag_name("option")
    if options:
        for o in options:
            if o.text == texttoselect:
                o.click()

def getPickupLine(i):
    j = 0
    with open('pickuplines.txt') as f:
        for line in f:
            if i == j:
                return line
            j += 1

browser = driver.Chrome()
browser.get('https://tinder.com/app/recs')
browser.implicitly_wait(10)
loginBtn = browser.find_element_by_xpath('//*[@id="modal-manager"]//button[@aria-label="Log in with Facebook"]')
loginBtn.click()

Whandles = browser.window_handles
window_before = Whandles[0]
window_after = Whandles[1]
browser.switch_to_window(window_after)

emailInput = browser.find_element_by_xpath('//*[@id="email"]')
emailInput.send_keys(facebookEmail)
browser.implicitly_wait(2)
pwInput = browser.find_element_by_xpath('//*[@id="pass"]')
pwInput.send_keys(Keys.BACK_SPACE + facebookPassword)
browser.implicitly_wait(2)
submit = browser.find_element_by_xpath('//*[@id="u_0_0"]')
submit.click()

browser.implicitly_wait(2)
browser.switch_to_window(window_before)

browser.implicitly_wait(5)
nextBtn = browser.find_element_by_xpath('//*[@id="content"]//button/span/span[contains(.,"Next")]')
nextBtn.click()
browser.implicitly_wait(2)
nextBtn = browser.find_element_by_xpath('//*[@id="content"]//button/span/span[contains(.,"Next")]')
nextBtn.click()
browser.implicitly_wait(2)
nextBtn = browser.find_element_by_xpath('//*[@id="content"]//button/span/span[contains(.,"Allow")]')
nextBtn.click()
browser.implicitly_wait(2)
nextBtn = browser.find_element_by_xpath('//*[@id="content"]//button/span/span[contains(.,"Not")]')
nextBtn.click()
browser.implicitly_wait(2)

matches = browser.find_elements_by_css_selector('h3.messageListItem__name')
msgBox = browser.find_elements_by_css_selector('textarea.sendMessageForm__input')

count = 0
for match in matches:
    match.click()
    browser.implicitly_wait(4)
    messages = browser.find_elements_by_css_selector('.msg > span.text')
    if len(messages) == 0:
        msgBox = browser.find_element_by_css_selector('textarea.sendMessageForm__input')
        msgBox.send_keys(getPickupLine(count))
    count =+ 1
 
f.close()



