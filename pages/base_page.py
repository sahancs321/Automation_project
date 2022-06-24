from selenium.common.exceptions import NoSuchElementException
class BasePage():
    def __init__(self, browser, url, timeout=6):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def string_in_url(self,string):
        url = self.browser.current_url
        if string in url:
          return True
        else:
            return False



