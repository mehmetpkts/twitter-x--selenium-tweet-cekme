from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from users import username,password,arama
import time


# sleep işlemleri fazla tutuldu çünkü internetten hızına göre sayfaların yüklenmesinde değişiklikler olacaktır.


class Twitter:
    
    def __init__(self,username,password,arama):
        self.username = username
        self.password = password
        self.arama = arama
        self.browser = webdriver.Chrome()
        
    def signInUsername(self):
        self.browser.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoidHIifQ%3D%3D%22%7D")
        time.sleep(5)
        
        usernameInput = self.browser.find_element(By.TAG_NAME,"input")
        
        
        usernameInput.send_keys(username)
        usernameInput.send_keys(Keys.ENTER)
        
        time.sleep(10)
    
        
    def signInPassword(self):
        time.sleep(5)
        passwordInput = self.browser.find_element(By.NAME,"password")
        
        passwordInput.send_keys(password)
        
        time.sleep(5)
        
        passwordInput.send_keys(Keys.ENTER)
        
        time.sleep(15)
        
    def clickExplore(self):
        self.browser.get("https://x.com/explore")   # https://x.com/explore ,  https://twitter.com/explore
        time.sleep(7)
    
    def clickMehmetPektas(self):
        time.sleep(3)
        mehmetInput = self.browser.find_element(By.TAG_NAME,"input")
        
        mehmetInput.send_keys(arama)
        time.sleep(5)
        
        mehmetInput.send_keys(Keys.ENTER)
        
        time.sleep(7)
        
    def countDiv(self):
        name=self.browser.find_elements(By.XPATH,"(//*[contains(@class, 'css-175oi2r r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l')])")   # css-175oi2r r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l

        for value in name:
            print(value.text + "\n")    

        time.sleep(10)
        

# fonksiyonları çağırma

        
app = Twitter(username,password,arama)

app.signInUsername()

app.signInPassword()

app.clickExplore()

app.clickMehmetPektas()

app.countDiv()