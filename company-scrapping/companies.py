import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL to scrape
url = 'https://www.yell.com/ucs/UcsSearchAction.do?keywords=software+development&location=Manchester%2C+Lancashire&scrambleSeed=67794334'

# Send a GET request to the URL and parse the response using Beautiful Soup
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all company listings on the page
company_listings = soup.find_all('div', class_='row businessCapsule--mainRow')

# Create an empty list to store the extracted data
company_data = []

# Loop through each company listing and extract information
for company in company_listings:
    # Extract the company name, address, and website
    name = company.find('span', class_='businessCapsule--name').text.strip()
    address = company.find('span', class_='businessCapsule--address').text.strip()
    website = company.find('a', class_='businessCapsule--ctaItem')['href'].strip()

    # Check if the company is located in Manchester or Liverpool
    if 'Manchester' in address or 'Liverpool' in address:
        # Add the company information to the list if it meets our criteria
        company_data.append({'Name': name, 'Address': address, 'Website': website})

# Create a pandas dataframe from the list of company data
df = pd.DataFrame(company_data)

# Write the dataframe to an Excel file
filename = 'software_companies.xlsx'
df.to_excel(filename, index=False)

print(f'Successfully wrote {len(df)} companies to {filename}.')
