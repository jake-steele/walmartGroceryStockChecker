# walmartGroceryStockChecker
Script to check availability of items from grocery pickup at local Walmart, then log the findings in a CSV file.

## Dependencies
Uses following Python modules:
* csv
* time
* [Selenium](https://selenium-python.readthedocs.io/index.html)

## Usage Instructions:
User should change/enter their preferred:
* Zipcode in the zipcodeToCheck variable
* File name in the exportFileName variable
* XPATH for correct selection in the penultimate wait.until for store selection block
* URLs for personalized items in the personalFavorites array

After making these changes, ensure the CSV file is not open in another application, then build/execute the script.
