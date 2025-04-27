from bs4 import BeautifulSoup

with open('scraper/index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    # must add underscore after class because class alone is a keyword for python
    course_card = soup.find_all('div', class_='card')

    for course in course_card:
        # print(course)
        # print(course.h5)
        # print(course.h5.text)
        course_name = course.h5.text
        course_price = course.a.text.split()[-1] # taking just the last index which has the price
        # print(course_name)
        # print(course_price)
        print(f' {course_name} costs {course_price}')