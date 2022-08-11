from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Scraper:
    def __init__(self, **args):
        self.tree = args['tree']

    def unpack(self, driver, node):
        if self.tree.has_key('fetch'):
            if self.tree['type']== 'text':
                return node.text
            elif self.tree['attr']:
                return node.get_attribute(se)

