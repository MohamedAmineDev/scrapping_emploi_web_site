import time

from fetch_website import fetch_website

#grab_single_offer('https://candidat.pole-emploi.fr/offres/recherche/detail/164YKZV')
#print('---------------------')
#grab_single_offer('https://candidat.pole-emploi.fr/offres/recherche/detail/166LHSN')
#print('---------------------')
#grab_single_offer('https://candidat.pole-emploi.fr/offres/recherche/detail/166BKXD')
languages=['java','python','c','c#','html','css','angular','react js','javascript','go','android','flutter']
sleeping_time=20
while True:
    for language in languages:
        fetch_website(language)
        print('\n\n\n')
        print(f'Now sleeping for {sleeping_time}')
        time.sleep(sleeping_time)

