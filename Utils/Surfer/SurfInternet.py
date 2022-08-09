from SurferHelpers.Drivers import Driver_setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class Login():
    def __init__(self,**args):
        self.insta_login = args['insta_login']

    def Login_instagram(self):
        driver = Driver_setup.configure_driver('Instagram',self.insta_login['username'])
        driver.get('https://www.instagram.com/')
        try:
            WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID,'loginForm')))
            go_ahead=True
        except:
            go_ahead=False
        if go_ahead:
            loginform = driver.find_element(By.ID, 'loginForm')
            loginform.find_elements(By.TAG_NAME, 'input')[0].send_keys(self.insta_login['username'])
            loginform.find_elements(By.TAG_NAME, 'input')[1].send_keys(self.insta_login['password'])
            loginform.find_elements(By.TAG_NAME,'button')[1].click()
            WebDriverWait(driver,15).until(EC.presence_of_element_located((By.TAG_NAME,'nav')))
        driver.quit()
        return


login = Login(insta_login={'username': 'kedar_animate', 'password': 'kedar#23@1998'})
login2 = Login(insta_login={'username': 'kedar_animate', 'password': 'kedar#23@1998'})

login.Login_instagram()



