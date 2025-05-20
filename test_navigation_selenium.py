from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # Run headless so no GUI is needed

driver = webdriver.Chrome(options=options)

try:
    # Open your local file or a URL
    driver.get("file:///path/to/your/index.html")  # Change this path accordingly

    # Validate title
    assert "Home - My Demo Website" in driver.title
    print("✅ Title check passed")

    # Check Home link
    home_link = driver.find_element(By.LINK_TEXT, "Home")
    assert home_link.get_attribute("href").endswith("index.html")
    print("✅ Home link is correct")

    # Check About link
    about_link = driver.find_element(By.LINK_TEXT, "About")
    assert about_link.get_attribute("href").endswith("about.html")
    print("✅ About link is correct")

    # Check Contact link
    contact_link = driver.find_element(By.LINK_TEXT, "Contact")
    assert contact_link.get_attribute("href").endswith("contact.html")
    print("✅ Contact link is correct")

finally:
    driver.quit()
