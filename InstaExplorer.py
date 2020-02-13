from selenium import webdriver
from time import sleep

class InstaExplorer:
  def __init__(self, username, password):
    self.driver = webdriver.Chrome()
    self.driver.get("https://instagram.com")

    # Sleep for the initial page load
    sleep(2)

    self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()

    # Wait for the login page
    sleep(2)

    self.driver.find_element_by_xpath("//input[@name= \"username\"]").send_keys(username)
    self.driver.find_element_by_xpath("//input[@name= \"password\"]").send_keys(password)

    # Just wait for the fuck of it
    sleep(1)

    self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()

    # Wait for home to load
    sleep(3)

    self.driver.find_element_by_xpath("//button[contains(text(), \"Not Now\")]").click()

    sleep(1)

    self.driver.find_element_by_xpath(f"//a[contains(text(), {username})]").click()

    sleep(2)

    # /amin.ahrabian/followers/
    self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()

    #suggestions = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
    #self.driver.execute_script('arguments[0].scrollIntoView()', suggestions)

    sleep(1)

    scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
    last_ht, ht = 0, 1
    while last_ht != ht:
      last_ht = ht

      sleep(1)

      ht = self.driver.execute_script("""
          arguments[0].scrollTo(0, arguments[0].scrollHeight); 
          return arguments[0].scrollHeight;
          """, scroll_box)

    links = scroll_box.find_elements_by_tag_name('a')
    names = [name.text for name in links if name.text != '']

    print("Doing stuff is finished")
    print(len(names))
    print(names)   



InstaExplorer('amin.ahrabian','64232550')