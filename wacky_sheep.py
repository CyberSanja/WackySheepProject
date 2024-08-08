from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def load_wacky_sheep_web_page(url):

    driver = webdriver.Chrome(service=Service("C:/Windows/chromedriver-win64/chromedriver.exe"))
    driver.maximize_window()
    driver.get(url)

    return driver


def test_account_login():

    driver = load_wacky_sheep_web_page("https://wackysheep.com/")
    sleep(2)

    driver.find_element(By.CSS_SELECTOR, "a[href='/account/login']").click()
    sleep(2)
    driver.find_element(By.ID, "customer_email").send_keys("sanja.pistac@gmail.com")
    sleep(1)
    driver.find_element(By.NAME, "customer[password]").send_keys("SanjosSuperPistac19")
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    sleep(2)

    assert driver.current_url == "https://wackysheep.com/account"

    close_chrome(driver)


def test_wrong_password_login():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[href='/account/login']").click()
    sleep(2)
    driver.find_element(By.ID, "customer_email").send_keys("sanja.pistac@gmail.com")
    sleep(1)
    driver.find_element(By.NAME, "customer[password]").send_keys("SanjosSuperPistac")
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    sleep(2)

    assert driver.find_element(By.XPATH, "//li[contains(., 'Incorrect email or password')]").text, "Logged In"

    close_chrome(driver)


def test_password_input_text_field_empty():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[href='/account/login']").click()
    sleep(2)
    driver.find_element(By.ID, "customer_email").send_keys("sanja.pistac@gmail.com")
    sleep(1)
    driver.find_element(By.NAME, "customer[password]").send_keys("")
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    sleep(2)

    driver.save_screenshot("LoginError.png")
    sleep(1)

    close_chrome(driver)


def test_both_input_text_fields_empty():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[href='/account/login']").click()
    sleep(2)
    driver.find_element(By.ID, "customer_email").send_keys("")
    sleep(1)
    driver.find_element(By.NAME, "customer[password]").send_keys("")
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    sleep(2)

    assert driver.current_url == "https://wackysheep.com/account/login"
    sleep(1)

    close_chrome(driver)


def test_search_the_wacky_sheep_page():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[aria-label='Search']").click()
    sleep(5)
    driver.find_element(By.ID, "search-input").send_keys("hoodies")
    driver.find_element(By.CSS_SELECTOR, "input#search-input").send_keys(Keys.ENTER)
    sleep(3)

    assert driver.current_url == "https://wackysheep.com/search?type=product&q=hoodies"

    close_chrome(driver)


def test_contact_info():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[href='/pages/contact']").click()
    sleep(3)

    assert driver.current_url == "https://wackysheep.com/pages/contact"

    close_chrome(driver)


def test_display_item_info():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)
    driver.find_element(By.XPATH,
                        "//*[@id='shopify-section-template--15501061750956__featured-collection-grid']"
                        "/div""/div[2]/div[4]/a/div[2]/div[1]/div[1]/p").click()
    sleep(3)

    assert driver.current_url == "https://wackysheep.com/products/ms-neon-cotton-shorts"

    close_chrome(driver)


def test_search_item_and_add_to_cart():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[aria-label='Search']").click()
    sleep(5)
    driver.find_element(By.ID, "search-input").send_keys("shorts")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input#search-input").send_keys(Keys.ENTER)
    sleep(3)
    driver.find_element(By.XPATH, "//*[@id='search-results-root']/div[2]/div[4]/a/div[2]/div[1]"
                                  "/div[1]/p").click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, "input[value='Medium']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//span[contains(., 'Add to Cart')]").click()
    sleep(2)

    driver.save_screenshot("item_added_to_cart.png")
    sleep(2)

    close_chrome(driver)


def test_remove_item_from_cart():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[aria-label='Search']").click()
    sleep(5)
    driver.find_element(By.ID, "search-input").send_keys("shorts")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input#search-input").send_keys(Keys.ENTER)
    sleep(3)
    driver.find_element(By.XPATH, "//*[@id='search-results-root']/div[2]/div[4]/a/div[2]/div[1]"
                                  "/div[1]/p").click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, "input[value='Medium']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//span[contains(., 'Add to Cart')]").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[href='/cart/change?line=1&quantity=0']").click()
    sleep(3)

    driver.save_screenshot("item_removed_from_cart")

    close_chrome(driver)


def test_checkout():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[aria-label='Search']").click()
    sleep(5)
    driver.find_element(By.ID, "search-input").send_keys("shorts")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input#search-input").send_keys(Keys.ENTER)
    sleep(3)
    driver.find_element(By.XPATH, "//*[@id='search-results-root']/div[2]/div[4]/a/div[2]/div[1]"
                                  "/div[1]/p").click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, "input[value='Medium']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//span[contains(., 'Add to Cart')]").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input#agree").click()
    sleep(3)
    driver.find_element(By.NAME, "checkout").click()
    sleep(3)

    assert driver.title == "Checkout - Wacky Sheep"
    sleep(2)

    close_chrome(driver)


def test_if_logo_button_returns_to_main_page():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)
    driver.find_element(By.LINK_TEXT, "SHOP NOW").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[title='Wacky Sheep']").click()
    sleep(3)

    assert driver.current_url == "https://wackysheep.com/"

    close_chrome(driver)


def test_open_privacy_policy():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[title='Privacy Policy']").click()
    sleep(10)

    assert driver.title == "Privacy policy | Wacky Sheep"

    close_chrome(driver)


def test_open_refund_policy():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)

    driver.find_element(By.LINK_TEXT, "Refund Policy").click()
    sleep(5)

    assert driver.current_url == "https://wackysheep.com/policies/refund-policy"

    close_chrome(driver)


def test_about_page():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[title='About']").click()
    sleep(2)

    assert driver.current_url == "https://wackysheep.com/pages/about"

    close_chrome(driver)


def test_contest_page():

    driver = load_wacky_sheep_web_page("https://www.wackysheep.com/")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a[href='/pages/umetnik-nije-ovca-4']").click()
    sleep(2)

    assert driver.current_url == "https://wackysheep.com/pages/umetnik-nije-ovca-4"

    close_chrome(driver)


def close_chrome(driver):
    driver.maximize_window()
    driver.quit()

