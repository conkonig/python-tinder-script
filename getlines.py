from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)

browser.get('https://twitter.com/pickupIines')
elements = browser.find_elements_by_css_selector(
    'p:not(.ProfileHeaderCard-bio)')

f = open('pickuplines.txt', 'w')
# f.write( str(datetime.now().date() ) )
# f.write("\n")

for x in elements:
    if x.text != "":
        print("got line ", x.text, " printing to pickuplines.txt")
        f.write(x.text)
        f.write("\n")

f.close()
browser.close()
# print(element.text)
 