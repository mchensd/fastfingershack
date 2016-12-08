from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://10fastfingers.com/typing-test/english")
'''elem = browser.find_element_by_id('row1')
words = elem.text
words = words.split(' ')

inp = browser.find_element_by_id('inputfield')

for word in words:
    inp.send_keys(word + ' ')
    time.sleep(0.1)'''


finished = False
inp = browser.find_element_by_id('inputfield')
t = time.time()
while True:
    word = browser.find_element_by_class_name('highlight').text
    inp.send_keys(word + ' ')

    if time.time() - t >= 60:
        break
