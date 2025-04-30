#pip install requests

from bs4 import BeautifulSoup
import requests
import time

print("Put in the skill that you are not familiar with")
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text
    # print(html_text) # 200 means request accepted
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('div', class_='srp-listing clearfix')
    # print(jobs)

    for index, job in enumerate(jobs):
        job_published = job.find('span', class_='posting-time').text
        if '9' in job_published:
            company_name = job.find('span', class_='srp-comp-name').text
            skills = job.find('div', class_='srp-keyskills').text
            more_info = job.div.a['href']
            if unfamiliar_skill not in skills:
                with open(f'scraper/posts/{index}.txt', 'w') as f: # file name, permission 
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f'More Information: {more_info}')
                print(f"File saved: {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print('Waiting....')
        time.sleep(time_wait * 60)