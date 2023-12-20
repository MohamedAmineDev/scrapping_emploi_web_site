from bs4 import BeautifulSoup
import requests
from fetch_attributes import *
from offer import Offer


def grab_single_offer(link, keyword):
    offer = Offer()
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    data_titles = soup.find_all('h3', class_='skill-subtitle')
    # skill-list list-unstyled
    data = soup.find_all('ul', class_='skill-list list-unstyled')
    experience = ''
    skills = ''
    languages = ''
    tests = []
    for t in data_titles:
        if 'Expérience' in t or 'Compétences' in t or 'Langue' in t:
            tests.append(False)
    while False in tests:
        i = 0
        while i < len(data_titles):
            if 'Expérience' in data_titles[i]:
                offer.experience = fetch_experience(data[i])
                tests.pop()
                # data_titles.pop(i)


            elif 'Compétences' in data_titles[i]:
                # print(data[i])
                offer.skills = fetch_skills(data[i])
                tests.pop()
                # data_titles.pop(i)
            elif 'Langue' in data_titles[i]:
                offer.languages = fetch_language(data[i])
                tests.pop()
                # data_titles.pop(i)
            # elif 'Savoir-être professionnels' in data_titles[i]:
            #    tests.pop()
            #    data_titles.pop(i)

            i = i + 1
    offer.id = fetch_id_offer(soup)
    offer.name = fetch_title(soup)
    offer.date = fetch_date(soup)
    offer.address = fetch_address(soup)
    offer.contract_type = fetch_type_contract(soup)
    offer.qualification = fetch_qualification(soup)
    offer.skill = keyword
    return offer
    # print(f'Experience : {experience}')
    # print(f'Competences : {skills}')
    # print(f'Langues : {languages}')
    # print(f"Nom de l'entreprise : {name}")
    # print(f'Date : {date}')
    # print(f'Adresse : {address}')
    # print(f'Type de contrat : {contract_type}')
    # print(f'Qualification : {qualification}')
