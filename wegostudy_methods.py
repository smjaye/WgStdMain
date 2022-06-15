import datetime
from selenium import webdriver  # import selenium to the file
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import wegostudy_locators as locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select # ----------add this import for drop down lists
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager



s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)



def setUp():
    print(f'Launch {locators.app} App')
    print(f'__________________________________________________________')
    # make browser full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to WeGoStudy App website
    driver.get(locators.wego_study_url)


# check that WeGoStudy URL and the home page title are as expected
    if driver.current_url == locators.wego_study_url and driver.title == locators.wego_study_homepage_title :
        print(f'Yey! {locators.app} App website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()



def tearDown():
    if driver is not None:
        print(f'______________________________________________')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()




def log_in():
    if driver.current_url == locators.wego_study_url: # Check we are in homepage
        print(f'*************You are going to log in*******************************')
        driver.find_element(By.XPATH, '//b[normalize-space()="LOGIN"]').click()
        sleep(0.25)
        driver.find_element(By.ID, 'user_email').send_keys(locators.user_email)
        sleep(0.25)
        driver.find_element(By.ID, 'user_password').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.XPATH, '//input[@name="commit"]').click()
        sleep(0.25)



def schools():
    print(f'*********************You are in School selection page*****************************************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//h3[normalize-space()="British Columbia Institute of Technology"]').is_displayed()
    sleep(0.75)
    driver.find_element(By.XPATH, '//div[3]//div[3]//a[1]//div[1]').click()
    sleep(0.75)
    Select(driver.find_element(By.ID, 'study_area')).select_by_value('Computer, information and services')
    sleep(0.75)
    Select(driver.find_element(By.ID, 'level')).select_by_value('Bachelor of Technology')
    sleep(0.75)
    driver.find_element(By.XPATH, '//input[@value="GO"]').click()
    sleep(0.75)



def filter_by_study():
    print(f'*********************Lets browse, check where you are interested in***************************************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Filter By Study Area"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Computer, information and services")]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Culinary")]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Technology")]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//div[@id="filter_by_study_area"]//a[@class="apply_filter disable_apply"][normalize-space()="Apply"]').click()
    sleep(6)



def filter_by_city():
    print(f'********************Lets try second filter**************************************************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Filter By City"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Burnaby")]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Surrey")]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Kelowna")]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//div[@id="filter_by_city"]//a[@class="apply_filter disable_apply"][normalize-space()="Apply"]').click()
    sleep(6)



def filter_by_province():
    print(f'*****************Now its time for third filter************************************************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Filter By Province"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "British Columbia")]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//div[@id="filter_by_province"]//a[@class="apply_filter disable_apply"][normalize-space()="Apply"]').click()
    sleep(6)



def filter_by_program():
    print(f'********************Lets move again to fourth filter**********************************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Filter By Program"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Advanced Certificate")]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Bachelor of Interior Design")]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Bachelor of Technology")]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//div[@id="filter_by_program"]//a[@class="apply_filter disable_apply"][normalize-space()="Apply"]').click()
    sleep(6)



def my_we_go_study():
    print(f'*********************You are in Catalogue of WeGoStudy************************************')
    print(f'*********************Now you can create a referral****************************************')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[normalize-space()="Referrals"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[@class="btn btn-green btn-sm"]').click()
    sleep(0.75)
    driver.find_element(By.ID, 'referral_first_name').send_keys(locators.first_name)
    sleep(0.75)
    driver.find_element(By.ID, 'referral_last_name').send_keys(locators.last_name)
    sleep(0.75)
    driver.find_element(By.ID, 'referral_email_id').send_keys(locators.email)
    sleep(0.75)
    driver.find_element(By.XPATH, '//select[@id="school_id"]').click()
    sleep(0.75)
    Select(driver.find_element(By.XPATH, '//select[@id="school_id"]')).select_by_value('39')
    sleep(0.75)
    driver.find_element(By.XPATH, '//select[@id="program_id"]').click()
    sleep(0.75)
    Select(driver.find_element(By.XPATH, '//select[@id="program_id"]')).select_by_value('3943')
    sleep(0.75)
    driver.find_element(By.XPATH, '//input[@id="submit_referral"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//button[@class="btn btn-default"]').click()
    sleep(0.75)



def commissions():
    print(f' ************ Check out the tab- Commissions ************************************')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Commission"]').click()
    sleep(2)



def view_application_list():
    print(f'***************** View Application list for one student  ******************')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@id="student_list"]//div[1]//div[3]//a[3]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//button[@class="btn btn-default btn-sm"]').click()
    sleep(4)




def log_out():
    print(f'****************You are going to log out*******************************************')
    driver.find_element(By.CSS_SELECTOR, 'span[class="my-auto mr-2 pf-name"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[normalize-space()="Log out"]').click()
    sleep(0.75)
    driver.find_element(By.ID, 'authentication-popup').is_displayed()
    sleep(0.75)
    print(f'********* LOG OUT IS SUCCESSFUL  {datetime.datetime.now()}********************')










# setUp()
# log_in()
# schools()
# filter_by_study()
# filter_by_city()
# filter_by_province()
# filter_by_program()
# my_we_go_study()
# commissions()
# view_application_list()
# log_out()
# tearDown()
