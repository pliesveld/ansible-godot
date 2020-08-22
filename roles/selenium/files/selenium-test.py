from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(1024, 768))
display.start()

driver = webdriver.Firefox()
driver.get('http://www.erogol.com/')
driver.save_screenshot("screenshot.png")
driver.quit()

display.stop()
