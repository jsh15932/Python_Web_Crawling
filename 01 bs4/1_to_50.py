from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.co/1to50')
driver.implicity_wait(300)

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
print(len(btns))
print(btns[0].text)
print()