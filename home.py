import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/jcrns/Downloads/chromedriver")

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

class InstagramScript:
    def __init__(self):
        print("*** RUNNING INSTAGRAM BOT *** \n\n")
        self.browser = webdriver.Chrome(executable_path=DRIVER_BIN)

        self.browser.get('http://www.instagram.com')

    def login(self, username, password):
        print("Logging in... \n\n")

        time.sleep(2)
        usernameInput = self.browser.find_element_by_name('username')  # Find the search box
        usernameInput.send_keys(username)

        time.sleep(2)
        passwordInput = self.browser.find_element_by_name('password')  # Find the search box
        passwordInput.send_keys(password)

        submitButton = self.browser.find_element_by_xpath("//button[@type='submit']")
        submitButton.click()

        time.sleep(5)
    
    def saveInfoPopUp(self):
        print("Attempting to remove popup \n\n")
        try:
            #save your login info?
            time.sleep(5)
            notnow = self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        except Exception as e:
            print(e)

        try:
            #save your login info?
            time.sleep(5)
            notnow = self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        except Exception as e:
            print(e)

    def searchTags(self, query):
        print("Searching up " + query + "\n\n")
        self.browser.get('http://www.instagram.com/explore/tags/' + query)
        time.sleep(1)

    def scroll(self, n=3):
        for i in range(1, n):
            print(i)
            #scroll
            scrolldown=self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
            match=False
            while(match==False):
                last_count = scrolldown
                time.sleep(3)
                scrolldown = self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
                if last_count==scrolldown:
                    match=True

    def getPosts(self):
        posts = []
        links = self.browser.find_elements_by_tag_name('a')
        for link in links:
            post = link.get_attribute('href')
            if '/p/' in post:
                posts.append(post)
        return posts

    def getUsername(self):
        print("Getting username \n\n")
        username = self.browser.find_element_by_tag_name('h2')
        print(username.text)
        return username

    def getPostProfile(self):
        print("Getting profile from post \n\n")
        newUsername = self.getUsername()
        newUsername.click()
        return newUsername.text
        
    def goToPosts(self, posts, limit=0):
        print("Looping through links \n\n")
        # Collecting usernames of posts with specific hastags
        usernames = []
        
        # Creating counter variable
        counter = 0

        # Looping through posts
        for post in posts:
            self.browser.get(post)
            time.sleep(2)
            usernames.append(bot.getUsername().text)
            time.sleep(2)

            if limit != 0:
                if counter > limit:
                    break
                counter+=1

        return usernames

    def close(self):
        self.browser.quit()


if __name__ == "__main__":

    # Initializing bot
    bot = InstagramScript()

    # Logging in
    bot.login(username, password)

    # Clicking off popup
    bot.saveInfoPopUp()

    # Searching tag
    bot.searchTags("bayareabusiness")

    # Scrolling page
    bot.scroll(1)

    # Getting posts
    posts = bot.getPosts()

    # Scrapping usernames from posts
    usernames = bot.goToPosts(posts)

    
    print("Number of usernames: " + len(usernames))
    print(usernames)

    # Quiting
    bot.close()


# elem = browser.find_element_by_name(By.NAME, 'p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)

# browser.quit()