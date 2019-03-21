from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.0.0.1:62001'

desired_caps['app'] = r'C:\Users\liuzhiqiang\Desktop\danke-preview-1.0-0312-18-09-27.apk'

desired_caps['appPackage'] = 'com.axhs.danke'
desired_caps['appActivity'] = 'com.axhs.danke.activity.IndexActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)