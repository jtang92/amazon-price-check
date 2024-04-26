from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def fetch_product_details_with_selenium(url):
    # Setting up the Firefox WebDriver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    try:
        # Navigate to the Amazon product page
        driver.get(url)
        
        # Extracting the product name
        product_name = driver.find_element(By.ID, "productTitle").text.strip()
        
        # Find the entire price element
        price_element = driver.find_element(By.CSS_SELECTOR, "span.a-price")
        # Extract the whole and decimal parts within this element
        price_whole = price_element.find_element(By.CLASS_NAME, "a-price-whole").text.strip()
        price_fraction = price_element.find_element(By.CLASS_NAME, "a-price-fraction").text.strip()
        # Concatenate the whole number and the decimal part
        product_price = f"{price_whole}.{price_fraction}"
        
        return product_name, product_price
    finally:
        # Closing the browser
        driver.quit()

# Prompt the user to enter an Amazon URL
user_url = input("Please enter the Amazon product URL: ")

# Fetching product details using the user-provided URL
product_name, product_price = fetch_product_details_with_selenium(user_url)
print("Product Name:", product_name)
print("Product Price:", product_price)
