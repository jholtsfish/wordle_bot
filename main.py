from init import WORDS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# install webdriver service manager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.nytimes.com/games/wordle")

# use js script to access shadow elements
js = open("./access_elements.js")
print(
    driver.execute_script(js.read())
)
js.close()

input()