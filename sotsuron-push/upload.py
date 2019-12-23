#!/usr/bin/python3
# -*- coding:utf8 -*-
import os
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Browser:

    def __init__(self):
        self.url = 'https://vu.sfc.keio.ac.jp/sfc-sfs'
        self.u_login = os.environ['LOGIN_ID']
        self.u_pass = os.environ['LOGIN_PASS']
        self.file_title = os.environ['FILE_TITLE'] or 'thesis'
        self.file_path = '/src/paper/thesis.pdf'
        print("loading browser")
        self.browser = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        self.go_top()

    def go_top(self):
        self.browser.get(self.url)

    def login(self):
        print("login as: ", self.u_login)
        self.browser.find_element_by_name('u_login') \
            .send_keys(self.u_login)
        self.browser.find_element_by_name('u_pass') \
            .send_keys(self.u_pass)
        self.browser.find_element_by_xpath(
            '/html/body/table[2]/tbody/tr/td[2]/table'
            '/tbody/tr/td[2]/table/tbody/tr/td[1]/table[1]'
            '/tbody/tr/td/table[2]/tbody/tr/td/table'
            '/tbody/tr[3]/td/input').click()

    def go_upload_page(self):
        print("go upload page")
        time.sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/table[3]/tbody/tr/td[1]'
            '/table/tbody/tr[7]/td/a/img').click()
        time.sleep(1)
        self.browser.find_element_by_xpath(
            '//*[@id="navigation"]/div[4]/a').click()
        time.sleep(1)
        self.iframe = self.browser.find_element_by_xpath(
            '//*[@id="frame_set"]')
        print("switch driver")
        self.browser.switch_to_frame(self.iframe)
        try:
            self.browser.find_element_by_xpath(
                '/html/body/table[1]/tbody/tr[7]/td[3]/a[2]').click()
        except Exception as e:
            print(e)
            print(
                'You have to upload a file yourself'
                ' when it is the first time to upload.')

    def delete_old_file(self):
        print("delete old file")
        time.sleep(8)
        print(self.browser.page_source)
        self.browser.find_element_by_xpath(
            '/html/body/table[1]/tbody/tr[7]/td[3]/a[2]') \
            .click()
        time.sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/form/p[1]/table/tbody/tr[6]/td[3]/a[2]') \
            .click()

    def file_upload(self):
        print("file upload")
        time.sleep(1)
        self.browser.find_element_by_name('file_title') \
            .send_keys(self.file_title)
        self.browser.find_element_by_name('upload_file') \
            .send_keys(self.file_path)
        time.sleep(1)
        self.browser.find_element_by_xpath(
            '/html/body/form/p[1]/table/tbody'
            '/tr[7]/td[3]/input[7]').click()

    def post(self):
        self.login()
        self.go_upload_page()
        self.file_upload()
        self.delete_old_file()


def main():
    print("waiting for chrome...")
    time.sleep(10)
    browser = Browser()
    browser.post()
    print("login as: ", browser.u_login)
    browser.browser.quit()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
