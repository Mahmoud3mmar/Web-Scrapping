# Web-Scrapping

This code is a web scraper that:

Gets input from the user for a job title to search for
Sends a request to wuzzuf.net to search for jobs matching that title
Parses the response using BeautifulSoup
Extracts details from the search results like:
Job title
Company name
Location
Job skills
Date posted
Link to job listing
Loops over multiple pages of search results and extracts data from each page

Zips the extracted data into lists and saves to a CSV file

Updates a GUI label to show the user which page is being scraped

So in summary, this code allows a user to enter a job title and get a CSV file with details of job listings matching that title, scraped from the wuzzuf.net website.
