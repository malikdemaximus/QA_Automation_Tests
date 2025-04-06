# 📌 Этап 2 — Фикстуры и параметризация

## ✅ Что такое фикстура (`@pytest.fixture`)
- Это функция, которая запускается до и после теста.
- Пример: создаёт браузер (WebDriver), закрывает его после теста.
- `yield` — всё ДО него запускается перед тестом, всё ПОСЛЕ — после.

```python
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
