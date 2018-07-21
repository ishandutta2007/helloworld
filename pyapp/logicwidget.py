import os, time
from PyQt4.QtGui import QWidget
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
CHROME_DRIVER_PATH = '/Users/ishandutta2007/Downloads/chromedriver'

class LogicWidget(QWidget):
    def __init__(self, parent=None):
        isComplete = False
        while(not isComplete):
            try:
                isComplete = self.visit_zagl()
            except Exception:
                pass

    def visit_zagl(self):
        #Core logic goes here
        return True