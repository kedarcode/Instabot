from SurferHelpers.Drivers import Driver_setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from decouple import config


class Insta_Scraper:
    def __init__(self, **args):
        self.insta_login = args['insta_login']
        self.niche = args['niche']
        self.niche_tag = args['tags']

    def Login_instagram(self):
        driver = Driver_setup.configure_driver(platform='Instagram', userdata=self.insta_login['username'])
        driver.get(config('INSTA_LOGIN'))
        try:
            try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'loginForm')))
                go_ahead = True
            except:
                go_ahead = False
            if go_ahead:
                loginform = driver.find_element(By.ID, 'loginForm')
                loginform.find_elements(By.TAG_NAME, 'input')[0].send_keys(self.insta_login['username'])
                loginform.find_elements(By.TAG_NAME, 'input')[1].send_keys(self.insta_login['password'])
                loginform.find_elements(By.TAG_NAME, 'button')[1].click()
                WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, 'nav')))
        finally:
            driver.quit()
            return

    def start_scraping(self):
        driver = Driver_setup.configure_driver(platform='Instagram', userdata=self.insta_login['username'])
        try:
            for tag in self.niche_tag:
                images = []
                driver.get(f"{config('INSTA_SEARCH')}/explore/tags/{tag['label']}/")
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'article')))
                while len(images) < tag['count']:
                    imgs = driver.find_elements(By.CLASS_NAME, '_aagt')
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    for src in imgs:
                        try:
                            src = src.get_attribute('src')
                            if src not in images:
                                images.append(src)
                            else:
                                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        finally:
                            continue

                print(len(images))
        finally:
            driver.quit()


obj = Insta_Scraper(insta_login={'username': 'kedar_animate', 'password': 'kedar#23@1998'}, niche='fashion',
                    tags=[{'label': 'fashion', 'count': 100}])

obj.start_scraping()
