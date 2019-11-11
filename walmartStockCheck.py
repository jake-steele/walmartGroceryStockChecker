#!/home/jake/anaconda3/envs/walmart/bin/python
import csv, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

def main():
	# USER VARIABLES
	zipcodeToCheck = ""
	exportFileName = 'walmartStockCheckData' + '.csv'
	personalFavorites = [ # Array of strings, personalized list of URLs to check
		"",
		
	]
	userStoreXpath = '/html/body/div[1]/div/div[2]/aside/section[2]/div/div[1]/div/ul/li[2]/label'


	stockCheckArr = [ # Array of strings, generic grocery staples' URLs to be checked
		'https://grocery.walmart.com/ip/Bananas-each/44390948', # Bananas
		'https://grocery.walmart.com/ip/Great-Value-2-Reduced-Fat-Milk-1-Gallon-128-Fl-Oz/10450115', # Gal of 2% Milk
		'https://grocery.walmart.com/ip/Great-Value-Large-White-Eggs-18-count-36-oz/172844767', # 1.5 dz Eggs
		'https://grocery.walmart.com/ip/Great-Value-White-Bread-20-oz/10315752', # Loaf of white bread

	]
	for item in personalFavorites: # Combine lists
		stockCheckArr.append(item)

	availabilityArr = [] # Array of booleans for In Stock (True)/Out of Stock (False)
	options = Options() # Selenium Firefox options to allow headless operation
	options.headless = True
	driver = webdriver.Firefox(options=options)
	wait = WebDriverWait(driver, 5)

	# Select correct store
	driver.get("https://grocery.walmart.com")
	storeSelect = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div/section/div[1]/div[1]/div[1]/button")
	storeSelect.send_keys(Keys.SPACE)
	storeSelect = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/aside/section[2]/div/div[1]/div/div/form/input'))) # Selects zipcode text box
	storeSelect.click()
	storeSelect.clear()
	storeSelect.send_keys(zipcodeToCheck, Keys.ENTER)
	storeSelect = wait.until(EC.element_to_be_clickable((By.XPATH, userStoreXpath))) # Selects appropriate Walmart store listed based on zipcode and user-input XPATH
	storeSelect.click()
	storeSelect = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/aside[2]/section/div/button')))
	storeSelect.click()
	storeSelect = ''

	def checkStock(url):
		driver.get(url)
		wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div/section/section/div/div[1]/div/div[1]/button/i'))) # Waits until favorite button is present & visible
		try:
			if driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div/section/section/div/div[1]/div/div[3]/div[2]/div/div/button'): # Checks for "Add to Cart" button
				print('IN STOCK')
				availabilityArr.append(True)
		except:
			print('OUT OF STOCK')
			availabilityArr.append(False)

	for url in stockCheckArr:
		checkStock(url)

	print(availabilityArr)

	with open(exportFileName, mode='a', newline='') as csv_file:
		avail_writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
		newRow = [time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%a'), time.strftime('%H:%M:%S'), # Time values for data analysis
			driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div/section/div[1]/div[1]/div[1]/div/div[2]/section/div').get_attribute('aria-label'), # Current store address
			*availabilityArr] # Contents of availabilityArr, deconstructed
		avail_writer.writerow(newRow)

	driver.quit()



if __name__ == "__main__":
	main()
