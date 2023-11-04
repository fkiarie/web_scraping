# Fake Jobs Web Scraper

This is a Python script that scrapes job listings from the "Fake Jobs" website, which is a fictitious website for demonstration purposes. The script uses the `requests` library to make an HTTP GET request to the website and the `BeautifulSoup` library to parse the HTML content of the page. It then extracts job listings that mention "python" and prints out the title, company, location, and a link to apply for each job.

## Prerequisites

Before running the script, make sure you have the following libraries installed:

- `requests`: This library is used to send HTTP GET requests to the website.
- `BeautifulSoup`: This library is used to parse and navigate the HTML content of the page.

You can install these libraries using `pip` if you haven't already:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Set the `url` variable to the URL of the website you want to scrape. In this case, it's set to "https://realpython.github.io/fake-jobs/" for the "Fake Jobs" website.

2. Run the script.

```bash
python job_scraper.py
```

## Code Description

1. The script starts by importing the necessary libraries: `requests` and `BeautifulSoup`.

2. It defines the `url` variable, which holds the URL of the "Fake Jobs" website, and uses `requests.get(url)` to fetch the page content.

3. It uses `BeautifulSoup` to parse the HTML content of the page and find the element with the id "ResultsContainer," which contains the job listings.

4. It finds all job elements (divs with the class "card-content") within the "ResultsContainer."

5. It further filters the job elements to find those that mention "python" in the job title (case-insensitive) using a lambda function.

6. For each Python-related job, it extracts the job title, company, location, and the URL to apply for the job.

7. It prints the extracted information for each job listing, including the job title, company, location, and the application link.

## Output

The script prints the job listings with the following format:

```
Job Title
Company Name
Location
Apply here: Application URL

...
```

Each job listing is separated by an empty line.

## Note

This script is designed for educational and demonstration purposes. When using web scraping techniques on real websites, make sure to respect the website's terms of service, robots.txt, and legal requirements. Always obtain proper authorization when scraping real websites and be mindful of the website's usage policies.