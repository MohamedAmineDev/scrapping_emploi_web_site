import time

from fetch_website import fetch_website

languages = ['java', 'python', 'c', 'c#', 'html', 'css', 'angular', 'react js', 'javascript', 'go', 'android',
             'flutter']
sleeping_time = 20
while True:
    for language in languages:
        fetch_website(language)
        print('\n\n\n')
        print(f'Now sleeping for {sleeping_time}')
        time.sleep(sleeping_time)
