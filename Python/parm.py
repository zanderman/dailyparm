
##########################################################
# Chicken Parmesan Checker
#
# Author:
# 	Alexander DeRieux
#
# Description:
# 	Curious if it's chicken parmesan day at Owen's?
# 	Well, this tool is for you! This tool will check
# 	the current date and then tell you if it is chicken
# 	parmesan day.
##########################################################
import requests
from BeautifulSoup import BeautifulSoup

def scrape():

	# Link to the Owen's menu website.
	URL = "http://foodpro.dsa.vt.edu/FoodPro.NET/shortmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=09&locationName=FOOD+CRT%2f+HOKIE+GRILL+AT+OWENS+&naFlag=1"
	
    # Gather HTML from the URL.
    response = requests.get(URL)
	html = response.content

	# Run the HTML content through BeautifulSoup
	soup = BeautifulSoup(html)

	# Iterate over all meals for the day at Owen's
	for meal in soup.findAll('div', attrs={'class': 'meal_listing_item'}):
		
		# Get all recipes
		for recipe in meal.findAll('div', attrs={'class': 'shortmenurecipes'}):

			# Get all links associated with the current recipe
			for link in recipe.findAll('a'):

				# Check if the text of the link contains wording for Chicken Parmesan
				if "chicken parmesan" in link.contents[0].lower():
					print "Yes, today is Chicken Parmesan day." # prints name of meal!
					return True

	# No parmesan was found.
	print "No, today is not Chicken Parmesan day."
	return False

if __name__ == "__main__":
	scrape()
