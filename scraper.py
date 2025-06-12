
import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

# Setup database
conn = sqlite3.connect('db/price_data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS prices (
        product_name TEXT,
        price TEXT,
        url TEXT,
        timestamp TEXT
    )
''')

# Setup Selenium
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Product URL (Example: A search results page)
url = 'https://www.flipkart.com/search?q=monitor'
driver.get(url)
time.sleep(5)

# Parse HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')
products = soup.find_all("div", class_="_4rR01T")
prices = soup.find_all("div", class_="_30jeq3")

for product, price in zip(products, prices):
    pname = product.get_text()
    pprice = price.get_text()
    print(f"{pname} - {pprice}")
    cursor.execute("INSERT INTO prices VALUES (?, ?, ?, ?)",
                   (pname, pprice, url, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

conn.commit()
conn.close()
driver.quit()
