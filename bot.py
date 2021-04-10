from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(10)

browser.get('https://www.instagram.com/')
sleep(2)
# accepting cookies
cookie_button = browser.find_element_by_xpath("//button[text()='Accept']")
cookie_button.click()

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

#your username input goes here
username_input.send_keys("")
#your password input goes here
password_input.send_keys("")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(3)
# accepting not now button
save_login_info_button = browser.find_element_by_xpath("//button[text()='Not Now']")
save_login_info_button.click()
sleep(3)
notification_button = browser.find_element_by_xpath("//button[text()='Not Now']")
notification_button.click()

#hastag list can be updated, this is just an example of 2 hashtags that I happen to like
hashtag_list = ['inktober', 'drawthisinyourstyle']


tag = -1
followed = 0
likes = 0
comments = 0
try:
    for hashtag in hashtag_list:
        tag += 1
        browser.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
        sleep(5)
        first_thumbnail = browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

        first_thumbnail.click()
        sleep(randint(1, 2))
except Exception as e:
    print(e)
try:
    for x in range(1, 200):
        # username = browser.find_element_by_xpath(
        # '//*[@id="react-root"]/section/main/article/div[2]/div[1]/header/div[2]/div[1]/div[1]/span/a').text

        # if username not in prev_user_list:
        #     # If we already follow, do not unfollow
        if browser.find_element_by_xpath(
                '/html/body/div[5]/div/div/article/div[2]/div[1]/header/div[2]/div[1]/div[2]/button').text == 'Follow':

            browser.find_element_by_xpath(
            '/html/body/div[5]/div/div/article/div[2]/div[1]/header/div[2]/div[1]/div[2]/button').click()
        sleep(5)
        # new_followed.append(username)
        followed += 1

        # Liking the picture
        button_like = browser.find_element_by_xpath(
            '/html/body/div[5]/div/div/article/div[2]/div[2]/div/section[3]/span[1]/button')

        button_like.click()
        likes += 1
        sleep(randint(18, 25))

        comment_box = browser.find_element_by_xpath(
            '/html/body/div[5]/div/div/article/div[2]/div[2]/div/section[2]/div/form/textarea')
        comment_box.send_keys('Really cool!')
        sleep(5)
        comment_box.send_keys(Keys.ENTER)

except Exception as e:
    print(e)

print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))
