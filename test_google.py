from selenium import webdriver

# Запускаем браузер
driver = webdriver.Chrome()

# Открываем Google
driver.get("https://www.google.com")

# Проверяем заголовок
assert "Google" in driver.title

# Закрываем браузер
driver.quit()
