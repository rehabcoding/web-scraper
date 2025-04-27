# pip install beautifulsoup4
# pip install lxml 

from bs4 import BeautifulSoup

# same directory, reading from it, read only
with open('scraper/index.html', 'r') as html_file:
    content = html_file.read() # read html file content
    # print(content)

    soup = BeautifulSoup(content, 'lxml') # specifiying parser
    # print(soup.prettify())

    # tags = soup.find('h5')
    # print(tags) # on first try, it only printed the first tag it encountered
                # because find only searches once and achieved

    courses_tags = soup.find_all('h5')
    # print(tags)

    # instead of printing the entire tag, just printing the text inside the tag
    for course in courses_tags:
        print(course.text)