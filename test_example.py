
from selenium import webdriver
import unittest

class GoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # or webdriver.Firefox() based on your setup
        self.driver.implicitly_wait(10)

    def test_open_google(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
