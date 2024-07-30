def before_all(context):
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service

    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)

def after_all(context):
    context.driver.quit()
