# Sample web scraper for Craigslist using Beautiful Soup
# This will retrieve a list of apartment rentals within 15 miles from 04073 between 375 and 975 per month sorted by price
# Author: Fredric B. Gluck
# CNS1 - Sanford Regional Technical Center


# I am going to need these libraries
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable ## Allows printing in table format
# set variables
# This is the URL that we will be scraping
url="https://maine.craigslist.org/search/apa?sort=pricedsc&search_distance=15&postal=04073&min_price=375&max_price=975&availabilityMode=0&housing_type=1&housing_type=2&housing_type=9&sale_date=all+dates/"
#Lists that contain data scraped from page
apt_title = []
titles_found = 0 # counter to allow synching between lists 
apt_price = []
prices_found = 0
apt_neighborhood = []
neighborhoods_found = 0
apt_distance = []
distances_found = 0
counter=0
# Do the initial scrape of the Site and assign it to a variable
scraped_url = requests.get(url)
# Get the status of the request
returned_status = scraped_url.status_code
# Check the status code of the request to see if it was successful
if returned_status != 200:
	print(f"status code returned was: {returned_status}. Expected status code of 200")
else:
	print (f"The Status Code returned was: {scraped_url.status_code}")
	# Create a BS object of the data you scraped
	soup = BeautifulSoup(scraped_url.text, 'html.parser')
	# Returns the contents of the first <title> block as a string
	print(f"\n* Here is the scraped data from: {soup.find('title').string}")
	# Generate an list called obj_row_data. Each item is the list is the p.result-info
	obj_row_data = soup.select("p.result-info")
	# obj_row_data = soup.select("a.hdrlnk")
	# From each p.result-info, pull out specific information by string slicing
	for each_item in obj_row_data:
		#print (type(each_item))
		# Convert bs object to a string for further processing
		text_portion = str(each_item)
		#### print(f"****Text: {text_portion}")

		# 1. Gather title from html string
		start_pos= text_portion.find('.html">')
		end_pos = text_portion.find("</a>")
		# print(f"Title start:{start_pos}, Title end:{end_pos}")
		title_text = text_portion[start_pos+7:end_pos]
		# print(title_text)
		if len(title_text) != 0:
			titles_found += 1  # Keep track of number of titles found
			apt_title.append(title_text) #append it to the list
		else: # No title found
			titles_found += 1
			apt_title.append("entry: "+str(titles_found)+"--no title")
		
		#2. Gather Price
		start_pos= text_portion.find('class="result-price">')
		end_pos = text_portion.find("</span>",start_pos)
		# print(f"Start:{start_pos}, end:{end_pos}")
		price = text_portion[start_pos+21:end_pos]
		if len(price) !=0:
			prices_found +=1
			apt_price.append(price)
		else:
			prices_found +=1
			apt_price.append("entry:" + str(prices_found) + "--- no price")

		#3. Gather Location
		start_pos=0 # reset our pointer
		if text_portion.find('class="result-hood">') != -1:
			# print('*********** LOCAL NEIGHBORHOOD ***********')
			start_pos = text_portion.find('class="result-hood">')
			end_pos = end_pos= (text_portion.find("</span>",start_pos+20))
			neighborhood=text_portion[start_pos+20:end_pos]
			neighborhoods_found += 1
		elif text_portion.find('class="nearby"') !=-1: # No local neighborhood was found
			# print(f"********* NO LOCAL NEIGHBORHOOD **********")
			start_pos=text_portion.find('class="nearby"')
			start_pos=text_portion.find(">",start_pos)
			end_pos= (text_portion.find("</span>",start_pos))
			neighborhood=text_portion[start_pos+1:end_pos]
			neighborhoods_found += 1
		else:
			# print('********** NO NEIGHBORHOOD ****************')
			neighborhoods_found +=1
			neighborhood = "Listing " + str(neighborhoods_found) + ": NO NEIGHBORHOOD FOUND"

		# Get the neighborhood info
		# print(f"Neighborhood: {neighborhood}")
		apt_neighborhood.append(neighborhood)

		#4. Gather Distance
		start_pos=text_portion.find('class="maptag">')
		end_pos=text_portion.find('</span>',start_pos)
		distance=neighborhood=text_portion[start_pos+15:end_pos]
		distances_found += 1
		apt_distance.append(distance)

print (f"Titles:{titles_found}, Prices:{prices_found}, Neighborhood:{neighborhoods_found}, Distance:{distances_found}")

print (f"Quick print of results")
counter = 1	
output_table = PrettyTable()
output_table.field_names=[" ","Price", "Location", "Dist", "Description"]
output_table.align[" "]="l"
output_table.align["Price"]="l"
output_table.align["Location"]="l"
output_table.align["Dist"]="l"
output_table.align["Description"] = "l"
for (a,b,c,d) in zip(apt_price,apt_neighborhood,apt_distance,apt_title): 
	output_table.add_row([counter,a,b,c,d])
	counter += 1
print (output_table)
output_table.sortby="Dist"
print (output_table)





