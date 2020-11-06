import time
import bs4
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def login(driver, email, password):
    try:
        driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        emailTextBox = driver.find_element_by_id("ap_email")
        emailTextBox.send_keys(email)

        continueButton = driver.find_element_by_id("continue")
        continueButton.click()

        time.sleep(10)

        passwordTextBox = driver.find_element_by_id("ap_password")
        passwordTextBox.send_keys(password)

        submit = driver.find_element_by_id("signInSubmit")
        submit.click()

        return True
    except Exception as e:
        print(e)
        return False

def checkStock(driver, page):
    driver.get(page)

    try:
        status = driver.find_element_by_id("add-to-cart-button")
        status.click()
        return True

    except Exception as e:
        print(e)
        return False


def placeOrder(driver):
    try:
        try:
            noThanks = driver.find_element_by_id("siNoCoverage-announce")
            noThanks.click()

            time.sleep(10)
        except Exception as e:
            print(e)

        proceedToCheckout = driver.find_element_by_id(
            "proceedToRetailCheckout")
        proceedToCheckout.click()

        time.sleep(10)

        placeOrder = driver.find_element_by_name("placeYourOrder1")
        placeOrder.click()
        
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    pages = [
        "https://www.amazon.com/dp/B08L8HPKR6?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08L8LG4M3?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08L8JNTXQ?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08L8KC1J7?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08L8L9TCZ?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08LW46GH2?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08L8L71SM?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08KY322TH?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08KXZV626?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08KWPDXJZ?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08KWLMZV4?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08KWN2LZG?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08HBF5L3K?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08HBJB7YD?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08LF32LJ6?tag=nismain-20&linkCode=ogi&th=1&psc=1",
        "https://www.amazon.com/dp/B08LF1CWT2?tag=nismain-20&linkCode=ogi&th=1&psc=1"
    ]

    print("Enter your email: ")
    email = input()

    print("Enter your password: ")
    password = input()

    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    if login(driver, email, password):
        print("Login Successful")
        time.sleep(10)
        while True:
            for page in pages:
                if checkStock(driver, page):
                    print("In Stock")
                    time.sleep(5)
                    if placeOrder(driver):
                        print("Purchase Successful. Exiting...")
                        exit()
                time.sleep(2)
            time.sleep(1)
    else:
        print("Failed Login. Exiting...")
        exit()
