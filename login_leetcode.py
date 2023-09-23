import logging
import time
import json
import argparse
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "-log-level", dest="log_level", default="INFO")
    parser.add_argument("-o", "-output-path", dest="output_path", default="leetcode_cookies_csrftoken.json")
    parser.add_argument("-u", "-username", dest="username", default="")
    parser.add_argument("-p", "-password", dest="password", default="")
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)

    username = args.username
    password = args.password

    options = webdriver.FirefoxOptions()
    options.headless = False
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    logging.basicConfig(level=logging.INFO)

    driver.get("https://leetcode.com/accounts/login/")

    timeout = 30
    while timeout >= 0:
        logging.info('timeout cnt=' + str(timeout))
        try:
            un = driver.find_element(By.ID, 'id_login')
            un.clear()
            un.send_keys(username)
            pw = driver.find_element(By.ID, 'id_password')
            pw.clear()
            pw.send_keys(password)
            btn = driver.find_element(By.ID, 'signin_btn')
            btn.click()
            break
        except Exception as ex:
            logging.error('Generated an exception: {ex}'.format(ex=ex))
        timeout = timeout - 1
        time.sleep(1)

    time.sleep(5)
    timeout = 30
    while timeout >= 0:
        logging.info('timeout cnt=' + str(timeout))
        cookies_list = []
        csrf_token = ""
        leetcode_session = ""
        for cookie in driver.get_cookies():
            if cookie['name'] != 'messages':  # skip messages cookie
                cookies_list.append(cookie['name'] + "=" + cookie['value'])

            if cookie['name'] == 'csrftoken':
                csrf_token = cookie['value']
            elif cookie['name'] == 'LEETCODE_SESSION':
                leetcode_session = cookie['value']

        if csrf_token != "" and leetcode_session != "":
            cookies_str = ";".join(cookies_list)
            output = {
                "cookies": cookies_str,
                "csrf_token": csrf_token
            }
            logging.info(cookies_str)
            with open(args.output_path, 'w', encoding='utf-8') as fo:
                fo.write(json.dumps(output, separators=(',', ':')))
            break
        timeout = timeout - 1
        time.sleep(1)

    driver.quit()
