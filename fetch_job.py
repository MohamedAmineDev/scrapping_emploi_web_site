from bs4 import BeautifulSoup
import requests
from fetch_attributes import *
from entities.job import Job


def grab_single_job(link, technology):
    job = Job()
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    data_titles = soup.find_all('h3', class_='skill-subtitle')
    data = soup.find_all('ul', class_='skill-list list-unstyled')
    tests = []
    for t in data_titles:
        if 'Expérience' in t or 'Compétences' in t or 'Langue' in t:
            tests.append(False)
    while False in tests:
        i = 0
        while i < len(data_titles):
            if 'Expérience' in data_titles[i]:
                job.experience = fetch_experience(data[i])
                tests.pop()
                # data_titles.pop(i)


            elif 'Compétences' in data_titles[i]:
                # print(data[i])
                job.skills = fetch_skills(data[i])
                tests.pop()
                # data_titles.pop(i)
            elif 'Langue' in data_titles[i]:
                job.languages = fetch_language(data[i])
                tests.pop()
                # data_titles.pop(i)
            # elif 'Savoir-être professionnels' in data_titles[i]:
            #    tests.pop()
            #    data_titles.pop(i)

            i = i + 1
    job._unique_id = fetch_id_offer(soup)
    job.enterprise_name = fetch_title(soup)
    job.date = fetch_date(soup)
    job.address = fetch_address(soup)
    job.contract_type = fetch_type_contract(soup)
    job.qualification = fetch_qualification(soup)
    job.technology = technology
    return job
    # print(f'Experience : {experience}')
    # print(f'Competences : {skills}')
    # print(f'Langues : {languages}')
    # print(f"Nom de l'entreprise : {name}")
    # print(f'Date : {date}')
    # print(f'Adresse : {address}')
    # print(f'Type de contrat : {contract_type}')
    # print(f'Qualification : {qualification}')
