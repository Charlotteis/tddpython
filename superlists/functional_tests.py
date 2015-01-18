from selenium import webdriver

# Check that the Django app exists and is running
browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert "Django" in browser.title
