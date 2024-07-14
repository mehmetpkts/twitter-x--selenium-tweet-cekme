from users import username,password,arama
import time
##selenium libraries
import seleniumwire.undetected_chromedriver.v2 as seleniumWireWebdriver
import undetected_chromedriver as webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select



# sleep işlemleri fazla tutuldu çünkü internetten hızına göre sayfaların yüklenmesinde değişiklikler olacaktır.


class Twitter:
    
    def __init__(self,username,password,arama):
        self.username = username
        self.password = password
        self.arama = arama
        self.browser = webdriver.Chrome()
        
    def signInUsername(self):
        self.browser.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoidHIifQ%3D%3D%22%7D")
        usernameInput = self.wait_element(self.browser,By.TAG_NAME,"input",sleep=30)
        if not usernameInput: print("username input bulunamadi"); return False
        
        usernameInput.send_keys(username)
        usernameInput.send_keys(Keys.ENTER)

    def signInPassword(self):
        time.sleep(0.5)
        passwordInput = self.wait_element(self.browser,By.NAME,"password",sleep=30)
        passwordInput.send_keys(password)
        
        time.sleep(.5)
        
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)
        
    def clickExplore(self):
        self.browser.get("https://x.com/explore")   # https://x.com/explore ,  https://twitter.com/explore
    
    def clickArama(self):
        girInput = self.wait_element(self.browser,By.TAG_NAME,"input",sleep=30)
        girInput.send_keys(arama)
        time.sleep(1.2)
        girInput.send_keys(Keys.ENTER)
        
    def countDiv(self):
        tweet_list = []
        while True:
            self.wait_element(self.browser,By.XPATH,"(//*[contains(@class, 'css-175oi2r r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l')])")
            tweets = self.browser.find_elements(By.XPATH,"(//*[contains(@class, 'css-175oi2r r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l')])")
            
            tweet_count = len(tweets)
            for tweet in tweets:
                if tweet.text not in tweet_list:
                    tweet_list.append(tweet.text)
                    print(tweet.text)

            while not tweet_count < len(tweets):
                self.scrollDown(self.browser,500)
                time.sleep(1)
                tweets = self.browser.find_elements(By.XPATH,"(//*[contains(@class, 'css-175oi2r r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l')])")

    @staticmethod
    def wait_element(driver: webdriver,element_type,element:str,click: bool = False,trys: int = 1,sleep: int = 20,print_: bool = True):
        while trys>0:
            try:
                if click:
                    WebDriverWait(driver, sleep).until(EC.element_to_be_clickable((element_type,element))).click()
                else:
                    WebDriverWait(driver, sleep).until(EC.element_to_be_clickable((element_type, element)))

                return driver.find_element(element_type, element)
            except:
                    trys-=1
        if print_:
            print(f"Element {element} could not be clicked.")
        return False

    @staticmethod
    def scrollDown(driver, pixels): currentScroll = driver.execute_script(
        'return  window.pageYOffset'); driver.execute_script('window.scrollTo(0, {})'.format(currentScroll + pixels))
# fonksiyonları çağırma

        
app = Twitter(username,password,arama)

app.signInUsername()

app.signInPassword()

app.clickExplore()

app.clickArama()

app.countDiv()