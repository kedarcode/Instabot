from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Instabot.Utils.Drivers import Driver_setup
from decouple import config


class Scraper:
    def __init__(self, **args):
        self.tree = args['tree']

    def unpack(self, driver):
        if self.tree.has_key('inside'):
            self.unpack(self.tree['inside'])
        else:
            if self.tree.has_key('many'):
                source = driver.find_elements(self.tree['type'], self.tree['name'])
                node = []
                for sin in source:
                    node.append(self.categorize_get(sin))
                return node
            else:
                node = driver.find_element(self.tree['type'], self.tree['name'])
                if self.tree.has_key('fetch'):
                    return self.categorize_get(node)

    def categorize_get(self, node):
        if self.tree['fetch'] == 'text':
            return node.text
        elif self.tree['fetch'] == 'text':
            return node.get_attribute(self.tree['attr'])

driver = Driver_setup.configure_driver(platform='Instagram', userdata=self.insta_login['username'])
driver.get(config('INSTA_LOGIN'))