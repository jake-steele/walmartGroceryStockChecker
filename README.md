# walmartGroceryStockChecker
Script to check availability of items from grocery pickup at local Walmart, then log the findings in a CSV file.


## Reason for Project
In using grocery pickup, I will often find that the items I ordered were out-of-stock and either replaced or missing upon pickup. In an effort to find the objective best time for grocery pickup scheduling, based on the metric of grocery staple and personal favorite availability, I constructed this script. The goal is to output a csv file available for easy data analysis to make that determination.

## Personal Usage
I have setup this script to run as a cron job (every 15 minutes during Grocery Pickup hours) on a Linux droplet from Digital Ocean. I have determined that the 2GB Memory/2 vCPU droplet architecture is sufficient for this job. It typically takes less than one minute to perform this task and update the files, which are automatically updated via cloud storage accessible on my local machines.

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
