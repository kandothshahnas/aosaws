import datetime
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import aos_locators as locators
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
def setup():
    print('-------------------------------*set up*----------------------')
    print(f'-----------Test started @{datetime.datetime.now()}------------------')
    #maximise window
    driver.maximize_window()
    driver.implicitly_wait(30)
    #navigate to advantageshoppingonline webpage
    driver.get(locators.aos_url)
    aos_title =driver.title
    if driver.current_url == locators.aos_url and driver.title == aos_title:
        print(f'We are at the correct web page {driver.current_url}')
        print(f'We are seeing the title of web page as : {driver.title}')
    else:
        print(f'We are not at the correct web page!! check your code')
        driver.close()  # close the current tab
        driver.quit()  # close the browser completely

def teardown():
    if driver is not None:
        print('-----------------*tear down*------------------')
        print(f'Test completed at:{datetime.datetime.now()}')
        driver.close()
        driver.quit()

def create_new_account():#create new account for fake user in AOS app
    print('-------------------*create new account*--------------')
    driver.implicitly_wait(3)
    assert driver.find_element(By.ID,'menuUser').is_displayed()
    #driver.implicitly_wait(3)
    driver.find_element(By.ID,'menuUser').click()
    sleep(3)
    driver.find_element(By.XPATH, "//a[@class = 'create-new-account ng-scope']").click()
    sleep(1)
    driver.find_element(By.XPATH,"//input[@name = 'usernameRegisterPage']").send_keys(locators.aos_username)
    sleep(1)
    driver.find_element(By.XPATH,"//input[@name = 'emailRegisterPage']").send_keys(locators.aos_email)
    sleep(1)
    driver.find_element(By.XPATH,"//input[@name = 'passwordRegisterPage']").send_keys(locators.aos_password)
    sleep(1)
    driver.find_element(By.XPATH,"//input[@name = 'confirm_passwordRegisterPage']").send_keys(locators.aos_password)
    driver.find_element(By.XPATH, "//input[@name = 'first_nameRegisterPage']").send_keys(locators.first_name)
    driver.find_element(By.XPATH, "//input[@name = 'last_nameRegisterPage']").send_keys(locators.last_name)
    driver.find_element(By.XPATH, "//input[@name = 'phone_numberRegisterPage']").send_keys(locators.phone)
    Select(driver.find_element(By.XPATH,"//select")).select_by_visible_text('Canada')
    sleep(1)
    #driver.find_element(By.XPATH,"//select/option[@label='Canada']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//input[@name = 'cityRegisterPage']").send_keys(locators.city)
    driver.find_element(By.XPATH, "//input[@name = 'addressRegisterPage']").send_keys(locators.address)
    driver.find_element(By.XPATH, "//input[@name = 'state_/_province_/_regionRegisterPage']").send_keys(locators.province)
    driver.find_element(By.XPATH, "//input[@name = 'postal_codeRegisterPage']").send_keys(locators.postal_code)
    sleep(1)
    driver.find_element(By.XPATH,"//input[@name = 'i_agree']").click()
    sleep(1)
    driver.find_element(By.ID,"register_btnundefined").click()
    sleep(1)
    print(f'account for user {locators.full_name} is created successfully  '
          f'with username: {locators.aos_username} at:{datetime.datetime.now()}')


def check_username_display():#check usename is displayed
    print('----------*check username displayed*----------')
    sleep(1)
    if driver.find_element(By.XPATH,f"//a[@id = 'menuUserLink']/span[contains(., {locators.aos_username}) ]").is_displayed():
        path_username=driver.find_element(By.XPATH,f"//a[@id = 'menuUserLink']/span[contains(., {locators.aos_username}) ]")
        # username is captutured as logged_in_username
        logged_in_username = path_username.text
        sleep(1)
        if logged_in_username == locators.aos_username:
            print(f'username {logged_in_username} is displayed at the top menu')
    else:
        print('username is not displayed')
    sleep(1)


def logout():#log out user from AOS app
    sleep(1)
    print('----------------*log out*-----------------')
    driver.find_element(By.XPATH, "//a[@id='hrefUserIcon']").click()
    driver.find_element(By.XPATH, "// div[ @ id = 'loginMiniTitle'] / label[3]").click()
    # breakpoint()
    print(f'user  logged out successfuly at :{datetime.datetime.now()}')
    sleep(1)


def login():# log in user to AOS app
    sleep(1)
    print("----------------*log in*-------------------")
    driver.get(locators.aos_url)
    driver.implicitly_wait(3)
    driver.find_element(By.ID, 'menuUserLink').click()
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys(locators.aos_username)
    sleep(1)
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys(locators.aos_password)
    sleep(1)
    driver.find_element(By.XPATH,"//button[@id='sign_in_btnundefined']").click()
    sleep(1)
    print(f'user {locators.full_name} is logged in successfully at:{datetime.datetime.now()}')

#Validate main page of AOS app
def validate_dash_board():
    print('--------------*validate dashboard*-------------')
    # check the advantageDEMO logo is present
    sleep(2)
    display = driver.find_element(By.XPATH, "//div[@class='logo']/a").is_displayed()
    sleep(0.25)
    if display:
        print('--dashborad logo for AOS is displayed--')
    else:
        print('--dashborad logo for AOS is not displayed--')
    # check SPEAKERS text is diplayed
    display = driver.find_element(By.ID, 'speakersTxt').text
    sleep(0.25)
    if display == 'SPEAKERS':
        print('--SPEAKERS text  is displayed--')
    else:
        print('--SPEAKERS text is not displayed--')
    # check TABLETS text is displayed
    if driver.current_url == locators.aos_url:
        display = driver.find_element(By.ID, 'tabletsTxt').text
        sleep(0.25)
        if display == 'TABLETS':
            print('-- TABLETS text  is displayed--')
        else:
            print('--TABLETS text is not displayed--')
    # check  LAPTOPS text is displayed
    display = driver.find_element(By.ID, "laptopsTxt").text
    sleep(1)
    if display == 'LAPTOPS':
        print('--  LAPTOPS text  is displayed--')
    else:
        print('-- LAPTOPS text is not displayed--')
    # check  MICE text is displayed
    display = driver.find_element(By.ID, "miceTxt").text
    sleep(1)
    if display == 'MICE':
        print('--  MICE text  is displayed--')
    else:
        print('-- MICE text is not displayed--')
    # check  HEADPHONES text is displayed
    display = driver.find_element(By.ID, "headphonesTxt").text
    sleep(0.25)
    if display == 'HEADPHONES':
        print('--  HEADPHONES text  is displayed--')
    else:
        print('-- HEADPHONES text is not displayed--')
    # check top menu OUR PRODUCTS is clickable
    driver.find_element(By.XPATH, "//a[contains(text(),'OUR PRODUCTS')]").click()
    sleep(1)
    if driver.find_element(By.ID, "speakersImg").is_displayed() and driver.current_url == locators.aos_url:
        print("--top menu OUR PRODUCTS link is clicked")
    else:
        print("--top menu OUR PRODUCTS  link is not clicked")

    # check top menu SPECIAL OFFER is clickable
    driver.find_element(By.XPATH, "//a[contains(text(),'SPECIAL OFFER')]").click()
    sleep(1)
    if driver.find_element(By.XPATH, "//h3[contains(.,'SPECIAL OFFER')]").is_displayed():
        sleep(1)
        print('--top menu SPECIAL OFFER link is clicked')
        driver.find_element(By.XPATH, "//a[contains(text(),'SPECIAL OFFER')]").send_keys(Keys.PAGE_DOWN)
    else:
        print('--top menu SPECIAL OFFER link is not clicked')
    # check ALL YOU WANT FROM A TABLET text is displayed
    if driver.find_element(By.XPATH,"//h2[contains(.,'ALL YOU WANT FROM A TABLET')]").text == 'ALL YOU WANT FROM A TABLET':
        print('--ALL YOU WANT FROM A TABLET text is displayed')
    else:
        print('--ALL YOU WANT FROM A TABLET text is not displayed')
    # check top menu POPULAR ITEMS is clickable
    if driver.current_url == locators.aos_url:
        driver.find_element(By.XPATH, "//a[contains(text(),'POPULAR ITEMS')]").click()
        sleep(1)
        if driver.find_element(By.XPATH, "//h3[contains(.,'POPULAR ITEMS')]").text == 'POPULAR ITEMS':
            sleep(1)
            print(f'--top menu POPULAR ITEMS link is clicked ')
        else:
            print('--top menu POPULAR ITEMS link is not clicked')
    else:
        driver.get(locators.aos_url)
        driver.find_element(By.XPATH, "//a[contains(text(),'POPULAR ITEMS')]").click()
        sleep(1)
        if driver.find_element(By.XPATH, "//h3[contains(.,'POPULAR ITEMS')]").text == 'POPULAR ITEMS':
            sleep(1)
            print(f'--top menu POPULAR ITEMS link is clicked ')
        else:
            print('--top menu POPULAR ITEMS link is not clicked')
            sleep(1)
    # check POPULAR ITEMS text is displayed
    if driver.find_element(By.XPATH, "//h3[contains(.,'POPULAR ITEMS')]").text == 'POPULAR ITEMS':
        print('--POPULAR ITEMS text is displayed')
    else:
        print('--POPULAR ITEMS text is  not displayed')
    # check top menu CONTACT_US is clickable
    driver.find_element(By.XPATH, "//a[contains(text(),'CONTACT US')]").click()
    sleep(1)
    if driver.find_element(By.XPATH, "//h1[@class ='roboto-bold contact_us ng-scope']").is_displayed():
        sleep(1)
        print('--top menu CONTACT_US link is clicked')
    else:
        print('--top menu CONTACT_US link is not clicked')
    # check CONTACT US form by sending a form
    print('-----------------*CONTACT US FORM*------------------')
    Select(driver.find_element(By.NAME, "categoryListboxContactUs")).select_by_index(1)
    sleep(1)
    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_index(1)
    sleep(1)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.aos_email)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.contact_text)
    sleep(1)
    driver.find_element(By.ID, "send_btnundefined").click()
    sleep(2)
    if driver.find_element(By.XPATH, "//p[@class='roboto-regular successMessage ng-binding']").text \
            == 'Thank you for contacting Advantage support.':
        print('--Thank you for contacting Advantage support. is displayed')
    else:
        print('--Thank you for contacting Advantage support. is not displayed')
    driver.find_element(By.XPATH, "//a[@class='a-button ng-binding']").click()
    print('--CONTINUE SHOPPING button is clicked')
    # check FOLLOW US text is displayed
    if driver.find_element(By.XPATH, "//div/h3[@class='roboto-regular center ng-scope' ]").text == 'FOLLOW US':
        print('--FOLLOW US text is displayed')
    else:
        print('--FOLLOW US text is not displayed')
    # check facebook link image is clickable
    window_before = driver.window_handles[0]
    assert driver.find_element(By.NAME, "follow_facebook").is_displayed()
    print("--facebook image  is displayed")
    driver.find_element(By.NAME, "follow_facebook").click()
    window_after_fb = driver.window_handles[1]
    sleep(1)
    driver.switch_to.window(window_after_fb)
    sleep(10)
    if driver.current_url == locators.fb_url:
        print(f'--facebook link image is clicked and navigated to {driver.current_url}')
        driver.close()
        driver.switch_to.window(window_before)
        sleep(10)
    else:
        print('--facebook image link is not clicked')

    # check Twitter link image is clickable
    assert driver.find_element(By.NAME, "follow_twitter").is_displayed()
    print('--twitter image is displayed')
    driver.find_element(By.NAME, "follow_twitter").click()
    window_after_twitter = driver.window_handles[1]
    sleep(1)
    driver.switch_to.window(window_after_twitter)
    sleep(10)
    if driver.current_url == locators.twitter_url:
        print(f'--twitter link image is clicked and navigated to {driver.current_url}')
        driver.close()
        driver.switch_to.window(window_before)
        sleep(10)
    else:
        print('--twitter image link is not clicked')
    # check linkedIn image is clickable
    assert driver.find_element(By.NAME, "follow_linkedin").is_displayed()
    print('--linkedIn image is displayed')
    driver.find_element(By.NAME, "follow_linkedin").click()
    window_after_linkedIn = driver.window_handles[1]
    sleep(1)
    driver.switch_to.window(window_after_linkedIn)
    sleep(10)
    if  driver.current_url == locators.linkedin_url:
        print(f'--linkedIn link image is clicked and navigated to {driver.current_url} ')
        driver.close()
        driver.switch_to.window(window_before)
        sleep(10)
    else:
        print('--ERROR!!!linkedIn image link is not clicked. Check your code')
        driver.switch_to.window(window_before)
        sleep(10)
    # check top menu SEARCH is clickable
    driver.find_element(By.XPATH, "//a[@title = 'SEARCH']").click()
    sleep(1)
    if driver.find_element(By.XPATH, "//input[@id='autoComplete']").is_displayed():
        sleep(1)
        print('--top menu SEARCH link is clickable')
    else:
        print('--top menu SEARCH link is not clickable')
    # check top menu USER icon is clickable
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    if driver.find_element(By.XPATH, "//div[@class='login ng-scope']").is_displayed():
        sleep(1)
        print('--top menu USER icon link is clickable')
        sleep(1)
        driver.find_element(By.XPATH, "//div[@class='closeBtn loginPopUpCloseBtn']").click()
        sleep(1)
    else:
        print('--top menu USER icon link is not clickable')
    # check top menu Shopping cart icon is clickable
    driver.find_element(By.ID, "menuCart").click()
    sleep(1)
    if driver.current_url == locators.cart_url:
        sleep(1)
        print('--top menu CART icon link is clickable')
        sleep(1)
    else:
        print('--top menu CART icon link is not clickable')
        sleep(1)
    # check shop now link for SPEAKERS is clickable
    if driver.current_url == locators.aos_url:
        sleep(1)
        # speaker =driver.find_element(By.XPATH, "//label[@id='speakersLink']")
        speaker = driver.find_element(By.ID, 'speakersLink')
        sleep(1)
        ActionChains(driver).move_to_element(speaker).click(speaker).perform()
        sleep(1)
        if driver.find_element(By.XPATH,"//h3[@class='categoryTitle roboto-regular sticky ng-binding']").text == 'SPEAKERS':
            print(f'--shop now link for SPEAKERS is clicked and navigated to {driver.current_url}')
        else:
            print(f'--shop now link for SPEAKERS is not clicked')
    else:
        driver.get(locators.aos_url)
        driver.implicitly_wait(3)
        speaker = driver.find_element(By.ID, 'speakersLink')
        sleep(1)
        ActionChains(driver).move_to_element(speaker).click(speaker).perform()
        sleep(1)
        if driver.find_element(By.XPATH,"//h3[@class='categoryTitle roboto-regular sticky ng-binding']").text == 'SPEAKERS':
            print(f'--shop now link for SPEAKERS is clicked and navigated to {driver.current_url}')
        else:
            print(f'--shop now link for SPEAKERS is not clicked')
    # Check shop now link for TABLETS is clickable
    if driver.current_url == locators.aos_url:
        driver.implicitly_wait(3)
        tablets = driver.find_element(By.ID, "tabletsLink")
        sleep(1)
        ActionChains(driver).move_to_element(tablets).click(tablets).perform()
        sleep(1)
        if driver.find_element(By.XPATH,"//h3[@class='categoryTitle roboto-regular sticky ng-binding']").text == 'TABLETS':
            print(f'--shop now link for TABLETS is clicked and navigated to {driver.current_url}')
        else:
            print('--shop now link for TABLETS is not clicked')
    else:
        driver.get(locators.aos_url)
        driver.implicitly_wait(3)
        tablets = driver.find_element(By.ID, "tabletsLink")
        sleep(1)
        ActionChains(driver).move_to_element(tablets).click(tablets).perform()
        sleep(1)
        if driver.find_element(By.XPATH,"//h3[@class='categoryTitle roboto-regular sticky ng-binding']").text == 'TABLETS':
            print(f'--shop now link for TABLETS is clicked and navigated to {driver.current_url}')
        else:
            print('--shop now link for TABLETS is not clicked')
    # Check shop now link for LAPTOPS is clickable
    if driver.current_url == locators.aos_url:
        driver.implicitly_wait(3)
        laptops = driver.find_element(By.ID, "laptopsLink")
        sleep(1)
        ActionChains(driver).move_to_element(laptops).click(laptops).perform()
        sleep(1)
        if driver.find_element(By.XPATH,"//h3[@class='categoryTitle roboto-regular sticky ng-binding']").text == 'LAPTOPS':
            print(f'--shop now link for LAPTOPS is clicked and navigated to {driver.current_url}')
        else:
            print('--shop now link for LAPTOPS is not clicked')

    else:
        driver.get(locators.aos_url)
        driver.implicitly_wait(3)
        laptops = driver.find_element(By.ID, "laptopsLink")
        sleep(1)
        ActionChains(driver).move_to_element(laptops).click(laptops).perform()
        sleep(1)
        if driver.find_element(By.XPATH,"//h3[@class='categoryTitle roboto-regular sticky ng-binding']").text == 'LAPTOPS':
            print(f'--shop now link for LAPTOPS is clicked and navigated to {driver.current_url}')
        else:
            print('--shop now link for LAPTOPS is not clicked')
    # check shop now link for MICE is clickable
    if driver.current_url == locators.aos_url:
        driver.implicitly_wait(3)
        mice = driver.find_element(By.ID, "miceLink")
        sleep(1)
        ActionChains(driver).move_to_element(mice).click(mice).perform()
        sleep(1)
        if driver.find_element(By.XPATH,"//h3[@class='categoryTitle roboto-regular sticky ng-binding']").text == 'MICE':
            print(f'--shop now link for MICE is clicked and navigated to {driver.current_url}')
        else:
            print('--shop now link for Mice is not clicked')
    else:
        driver.get(locators.aos_url)
        driver.implicitly_wait(3)
        mice = driver.find_element(By.ID, "miceLink")
        sleep(1)
        ActionChains(driver).move_to_element(mice).click(mice).perform()
        sleep(1)
        if driver.find_element(By.XPATH,"//h3[@class='categoryTitle roboto-regular sticky ng-binding']").text == 'MICE':
            print(f'--shop now link for MICE is clicked and navigated to {driver.current_url}')
        else:
            print('--shop now link for MICE is not clicked')
    # check shop now link for HEADPHONES is clickable
    if driver.current_url == locators.aos_url:
        driver.implicitly_wait(3)
        hphones = driver.find_element(By.ID, "headphonesLink")
        sleep(1)
        ActionChains(driver).move_to_element(hphones).click(hphones).perform()
        sleep(1)
        if driver.find_element(By.XPATH,"//h3[@class='categoryTitle roboto-regular sticky ng-binding']").text == 'HEADPHONES':
            print(f'--shop now link for HEADPHONES is clicked and navigated to {driver.current_url}')
        else:
            print('--shop now link for HEADPHONES is not clicked')
    else:
        driver.get(locators.aos_url)
        driver.implicitly_wait(3)
        hphones = driver.find_element(By.ID, "headphonesLink")
        sleep(1)
        ActionChains(driver).move_to_element(hphones).click(hphones).perform()
        sleep(1)
        if driver.find_element(By.XPATH,"//h3[@class='categoryTitle roboto-regular sticky ng-binding']").text == 'HEADPHONES':
            print(f'--shop now link for HEADPHONES is clicked and navigated to {driver.current_url}')
        else:
            print('--shop now link for HEADPHONES is not clicked')

def check_out_shopping_cart():
    print('------------*checkout shopping cart*---------')
    #random.choice([i for i in range(1, 35) if i != 13])
    driver.find_element(By.XPATH, "//a[contains(text(),'POPULAR ITEMS')]").click()
    sleep(2)
    driver.find_element(By.XPATH,"//a[@href='#/product/16']").click()
    sleep(1)
    driver.find_element(By.XPATH,"// button[ @ name = 'save_to_cart']").click()
    print('--item added to cart')
    sleep(2)
    driver.find_element(By.ID, "menuCart").click()
    sleep(2)
    driver.find_element(By.ID,"checkOutButton").click()
    #sleep(0.25)
    # print('---clicked')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"//button[contains(text(),'NEXT')]").click()
    sleep(1)
    driver.find_element(By.NAME,"safepay_username").send_keys(locators.aos_username)
    sleep(1)
    driver.find_element(By.NAME,"safepay_password").send_keys(locators.aos_password)
    sleep(1)
    driver.find_element(By.ID,"pay_now_btn_SAFEPAY").click()
    sleep(1)
    if driver.find_element(By.XPATH,"//span[@class='roboto-regular ng-scope']").text=='Thank_you_for_buying_with_Advantage':
        print('--Order placed and Thank_you_for_buying_with_Advantage message is displayed')
    else:
        print('Thank_you_for_buying_with_Advantage not displayed')
    sleep(1)
    locators.tracking_no = driver.find_element(By.XPATH,"//label[@id='trackingNumberLabel']").text
    print(f'--Tracking Number: {locators.tracking_no}')
    sleep(1)
    locators.order_no = driver.find_element(By.XPATH,"//label[@id='orderNumberLabel']").text
    print(f'--Order Number: {locators.order_no}')
    sleep(1)
    locators.order_date = driver.find_element(By.XPATH,"//label[contains(.,'Date ordered')]").text
    print(f'--Order date: {locators.order_date}')
    sleep(1)
    assert driver.find_element(By.XPATH,"//*[@id='orderPaymentSuccess']/div/div[1]/div/div[1]/label").is_displayed()
    print('--Full name of user is displayed in order confirmation page')
    assert driver.find_element(By.XPATH,'//*[@id="orderPaymentSuccess"]/div/div[1]/div/div[3]/label').is_displayed()
    print('-- phone number of user is displayed in order confirmation page')
    assert driver.find_element(By.XPATH,'//*[@id="orderPaymentSuccess"]/div/div[1]/div/div[2]/label[1]').is_displayed()
    print('-- address of user is displayed in order confirmation page')
    driver.implicitly_wait(10)


def delete_order():
    sleep(1)
    print('------------*delete order*------------')
    driver.find_element(By.XPATH, "//a[@id='hrefUserIcon']").click()
    driver.find_element(By.XPATH, "// div[ @ id = 'loginMiniTitle'] / label[2]").click()
    sleep(1)
    assert driver.find_element(By.XPATH,f"//td[@rowspan]/label[contains(.,'{locators.order_no}')]").is_displayed()
    print(f'Order with order number {locators.order_no} is displayed in My Orders')
    sleep(1)
    driver.find_element(By.XPATH,"//a[@class='remove red ng-scope']").click()
    driver.find_element(By.ID,'confBtn_1').click()
    sleep(1)
    assert driver.find_element(By.XPATH,"//div[@class='bigEmptyOrder center']/label[@class= 'roboto-bold ng-binding']").is_displayed()
    print('--No orders text is displayed. Hence order is removed')

def delete_user():
    print('-------------*delete user*------------')
    sleep(1)
    driver.find_element(By.XPATH, "//a[@id='hrefUserIcon']").click()
    driver.find_element(By.XPATH, "// div[ @ id = 'loginMiniTitle'] / label[1]").click()
    sleep(1)
    assert driver.find_element(By.XPATH, "//*[@id='myAccountContainer']/div[1]/div/div[1]/label").is_displayed()
    print('--My account page is displayed')
    sleep(1)
    if driver.current_url== locators.my_account_url:
        driver.find_element(By.XPATH, "//div[@class='deleteBtnText']").click()
        del_button = driver.find_element(By.XPATH, "//div[@class='deleteBtnContainer']/div[@class='deletePopupBtn deleteRed']")
        ActionChains(driver).move_to_element(del_button).click(del_button).perform()
        sleep(1)
        print(f'--user deleted at: {datetime.datetime.now()}---------')
    else:
        print('--Something went wrong')
    sleep(2)
    sleep(1)
    print("----------------test log in------------------")
    driver.get(locators.aos_url)
    driver.implicitly_wait(3)
    driver.find_element(By.ID,'menuUserLink').click()
    sleep(0.25)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(locators.aos_username)
    sleep(1)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(locators.aos_password)
    sleep(1)
    driver.find_element(By.XPATH, "//button[@id='sign_in_btnundefined']").click()
    assert driver.find_element(By.XPATH,"//label[@id='signInResultMessage']").is_displayed()
    print("Incorrect username or password message is displayed, hence confirmed user is deleted")


# setup()
# validate_dash_board()
# create_new_account()
# check_username_display()
# logout()
# login()
# check_out_shopping_cart()
# delete_order()
# delete_user()
# teardown()
