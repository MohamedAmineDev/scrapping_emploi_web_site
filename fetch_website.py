import requests
from bs4 import BeautifulSoup
from fetch_job import grab_single_job
from db_configuration.db_job import DbJob


def fetch_website(technology, db_connection):
    print('-------------------------------')
    print(f'Begin the task')
    print('-------------------------------')
    link = f'https://candidat.pole-emploi.fr/offres/recherche?lieux=75D&motsCles={technology.name}&offresPartenaires=true&rayon=10&tri=0'
    print(f'Counting offers of {technology.name} from this link {link}')
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='result')
    targets = []
    for current in jobs:
        next_link = current.find('a').get('href').split('/')
        targets.append(next_link[len(next_link) - 1])
    print(f'For {technology.name} we have found {len(targets)} offers')
    print('Now we are going to load data from the website')
    jobs = []
    print('Loading', end='')
    for target in targets:
        print(f'.', end='')
        jobs.append(grab_single_job(f'https://candidat.pole-emploi.fr/offres/recherche/detail/{target}', technology))
    print('')
    i = 0
    print('Saving new offers')
    for job in jobs:
        db_job = DbJob(db_connection)
        job_found = db_job.select_one_job_by_unique_id(job.unique_id)
        if job_found is None:
            new_job = job
            new_job.technology = technology
            db_job.insert_offer(new_job)
            i=i+1

    print(f'{i} offre were added !')
    print('-------------------------------')
    print('End of the task')
    print('-------------------------------')
