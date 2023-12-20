import requests
from bs4 import BeautifulSoup
from fetch_offer import grab_single_offer
from file_manipulation import *


def fetch_website(skill):
    print('-------------------------------')
    print(f'Begin the task')
    print('-------------------------------')
    link=f'https://candidat.pole-emploi.fr/offres/recherche?lieux=75D&motsCles={skill}&offresPartenaires=true&rayon=10&tri=0'
    print(f'Counting offers of {skill} from this link {link}')
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    offers = soup.find_all('li', class_='result')
    targets = []
    for current in offers:
        next_link = current.find('a').get('href').split('/')
        targets.append(next_link[len(next_link) - 1])
    print(f'For {skill} we have found {len(targets)} offers')
    print('Now we are going to load data from the website')
    offers = []
    print('Loading', end='')
    for target in targets:
        print(f'.', end='')
        offers.append(grab_single_offer(f'https://candidat.pole-emploi.fr/offres/recherche/detail/{target}', skill))
    print('')
    i=0
    print('Saving new offers')
    for offer in offers:
        found = find_offer(offer.id)
        if not found:
            add_content(offer.__str__())
            i=i+1
    print(f'{i} offre were added !')
    print('-------------------------------')
    print('End of the task')
    print('-------------------------------')
    """offer=grab_single_offer(f'https://candidat.pole-emploi.fr/offres/recherche/detail/{targets[1]}')
    print(f'Experience : {offer.experience}')
    print(f'Nom : {offer.name}')
    print(f'Addresse : {offer.address}')
    print('--')"""
