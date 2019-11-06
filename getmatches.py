import secrets as me
from selenium import webdriver as driver
from selenium.webdriver.support import ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--auto-open-devtools-for-tabs")
chrome_options.add_argument("--load-extension=" + me.favoriteExtension)
chrome_options.add_argument("--kiosk")

chrome_options.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
})
# chrome_options.add_argument("--headless")
browser = driver.Chrome(options=chrome_options)
browser.get('https://tinder.com/')
continueSwipes = 'y'
actions = ActionChains(browser)
actions.send_keys(Keys.RIGHT)


def login():
    browser.implicitly_wait(10)
    loginBtn = browser.find_element_by_xpath(
        '//*[@id="modal-manager"]//button[@aria-label="Log in with Facebook"]')
    loginBtn.click()
    Whandles = browser.window_handles
    window_before = Whandles[0]
    window_after = Whandles[1]
    browser.switch_to_window(window_after)
    emailInput = browser.find_element_by_xpath('//*[@id="email"]')
    emailInput.send_keys(me.fbUser)
    browser.implicitly_wait(2)
    pwInput = browser.find_element_by_xpath('//*[@id="pass"]')
    pwInput.send_keys(Keys.BACK_SPACE + me.fbPassword)
    browser.implicitly_wait(2)
    submit = browser.find_element_by_xpath('//*[@id="u_0_0"]')
    submit.click()
    browser.implicitly_wait(2)
    browser.switch_to_window(window_before)
    browser.implicitly_wait(5)


def dismissNotifications():
    try:
        allowBtn = browser.find_element_by_xpath(
            '//*[@id="content"]//button/span[contains(.,"Allow")]')
        allowBtn.click()
        browser.implicitly_wait(2)
    except:
        print("allowBtn element not found")
    try:
        stopNotifyBtn = browser.find_element_by_xpath(
            '//*[@id="content"]//button/span[contains(.,"Not interested")]')
        stopNotifyBtn.click()
        browser.implicitly_wait(2)
    except:
        print("'not interested in notifications' element not found")
    try:
        nextBtn = browser.find_element_by_xpath(
            '//*[@id="content"]//button/span[contains(.,"Allow")]')
        nextBtn.click()
        browser.implicitly_wait(2)
    except:
        print("'Allow location' element not found")


def roboThumbs(swipes):
    swiped = 0
    matches = 0
    while swiped < swipes:
        browser.implicitly_wait(1)
        actions.perform()
        swiped += 1
        print("Swiping " + str(swiped) + " / " +
              str(swipes) + " matched with " + str(matches))
        try:
            noHomeBtn = browser.find_element_by_xpath(
                '//*[@id="modal-manager"]//button/span[contains(.,"Not interested")]')
            noHomeBtn.click()
            browser.implicitly_wait(1)
        except:
            print(".")
        try:
            nextBtn = browser.find_element_by_xpath(
                '//*[@id="modal-manager"]//*[contains(text(),"Keep Swiping")]')
            nextBtn.click()
            matches += 1
            print("Caught one!")
            browser.implicitly_wait(1)
        except:
            print("Not a match")


login()
dismissNotifications()
browser.implicitly_wait(3)
roboThumbs(99)
while(str(continueSwipes) == 'y'):
    continueSwipes = input("Keep swiping?")
    if(str(continueSwipes) != 'y'):
        break
    else:
        numSwipes = input("How many times?")
        roboThumbs(int(numSwipes))

browser.quit()
 