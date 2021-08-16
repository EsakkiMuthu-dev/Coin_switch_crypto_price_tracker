from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.chrome.webdriver.WebDriver(executable_path='/usr/local/bin/chromedriver')
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'https://coinswitch.co/' 
driver.get(url)

while True:
        # fecthing crypto names
    labels = driver.find_elements_by_css_selector(".ticker .ticker__asset-name") 
    ls =[]
    for label in labels:
        b = label.text
        ls.append(b)
    crypto =ls

    #fetching their prices
    labels1 = driver.find_elements_by_css_selector(".ticker .ticker__price") 
    lf =[]
    for label in labels1:
        a = label.text
        a = a[1:]
        lf.append(a)
        
    price = lf

    scrap = dict(zip(crypto,price))
    print(' maara jaichitom!!!🤩')
    print(scrap)

    bitcoin = float(lf[0])
    deal_price = 350000.00 # you can change the deal price




    #checking whether it is our deal price or not

    if bitcoin <= deal_price:
        print('inga enna pakkuura 🧐 buy pannu da pakki..oduuuu🏃..💰price of bitcoin : ₹'+''+str(bitcoin))
    else:
        print('ippo buy panna venam🙅🏻‍♂.. innum price kammi aagala😤... 💰price of bitcoin:₹'+''+str(bitcoin))
    time.sleep(600)