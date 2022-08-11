from selenium import webdriver
from selenium_stealth import stealth
from decouple import config


class Driver_setup:
    def __init__(self, path, headless):
        self.path = path
        self.headless = headless
        self.driver = ''

    def create_driver(self, appdata):
        try:
            print('appdata')
            PATH = self.path
            options = webdriver.ChromeOptions()
            options.add_argument(f"--user-data-dir={appdata}")
            options.add_argument("start-maximized")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                "like Gecko) Chrome/90.0.4430.212 Safari/537.36")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            if self.headless: options.add_argument('--headless')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(PATH, options=options)
            stealth(driver,
                    languages=["en-US", "en"],
                    vendor="Google Inc.",
                    platform="Win64",
                    webgl_vendor="Intel Inc.",
                    renderer="Intel Iris OpenGL Engine",
                    fix_hairline=True,
                    )
            self.driver = driver
            return driver
        except Exception as e:
            return 'error' + str(e)

    @staticmethod
    def configure_driver(**args):
        appdata = config('USERDATA')+f'{args["platform"]}\\{args["userdata"]}'
        print(config('CHROMEDRIVER'))
        create_driver = Driver_setup(config('CHROMEDRIVER'), False)
        driver = create_driver.create_driver(appdata)
        return driver
