from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def get_browserstack_driver(browser_name, os_name):
    desired_caps = {
        'bstack:options': {
            'os': os_name,
            'osVersion': 'latest',
            'local': 'false',
            'seleniumVersion': '4.14.0',  # Or whichever you're using
            'userName': 'khirabdhitanayap_ynNFVR',
            'accessKey': '6NF85P2UBE1DcxUkoJgb'
        },
        'browserName': browser_name,
        'browserVersion': 'latest'
    }

    # Use appropriate browser options
    if browser_name.lower() == "chrome":
        options = ChromeOptions()
    else:
        options = FirefoxOptions()

    # Set capabilities
    for key, value in desired_caps.items():
        options.set_capability(key, value)

    return webdriver.Remote(
        options=options
    )
