#pip install requests

from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text
# print(html_text) # 200 means request accepted
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('div', class_='srp-listing clearfix')
# print(jobs)

for job in jobs:
    job_published = job.find('span', class_='posting-time').text
    if '8' in job_published:
        company_name = job.find('span', class_='srp-comp-name').text
        skills = job.find('div', class_='srp-keyskills').text

        print(f'''
        Company Name: {company_name}
        Required Skills: {skills}
        ''')