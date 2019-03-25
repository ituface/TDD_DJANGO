from selenium import webdriver

brower=webdriver.Chrome('/Users/finup/Desktop/chromedriver')
brower.get('http://127.0.0.1:8000/')
assert 'Django' in brower.title