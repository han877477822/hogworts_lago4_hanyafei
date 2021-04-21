# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://tptbrtctest.life.cntaiping.com/tptb/h5/tbadmin/#/rsm/exc-proj-contract")
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.find_element(By.ID, "tab-account").click()
# driver.find_element(By.CSS_SELECTOR,
#                     "#pane-account > div > div.comp-account-login > form > div:nth-child(1) > div > div > input").send_keys(
#     "13564390347")
# driver.find_element(By.CSS_SELECTOR, ".comp-smscode_send-btn").click()
# driver.find_element(By.CSS_SELECTOR,
#                     "#pane-account > div > div.comp-account-login > form > div:nth-child(2) > div > div > input").send_keys(
#     "111111")
# driver.find_element(By.CSS_SELECTOR, ".btn-submit").click()
# driver.find_element(By.XPATH, "//*[@id='master-container']/div[1]/div[2]/div/div[2]/div[2]/div[10]/div[1]/img").click()
# cookies = driver.get_cookies()
# print(cookies)
cookies = [{'domain': '.cntaiping.com', 'expiry': 7926167373, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross',
              'path': '/', 'secure': False,
              'value': '%7B%22distinct_id%22%3A%221001549993%22%2C%22first_id%22%3A%22178f1f99866ffb-0a3b66e1aff777-3f356b-1327104-178f1f99867e69%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%22178f1f99866ffb-0a3b66e1aff777-3f356b-1327104-178f1f99867e69%22%7D'}, {
                 'domain': '.cntaiping.com', 'expiry': 1619020799, 'httpOnly': False,
                 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'}]
driver.get("https://tptbrtctest.life.cntaiping.com/tptb/h5/tbadmin/#/rsm/exc-proj-contract")
sleep(2)
driver.maximize_window()
for cookie in cookies:
    driver.add_cookie(cookie)
    driver.refresh()
    sleep(3)
    print(cookie)
# driver.quit()
