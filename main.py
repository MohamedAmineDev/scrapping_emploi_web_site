import time

from fetch_website import fetch_website
from db_configuration.db_connection import DbConnection
from db_configuration.db_technologie import DbTechnology
from entities.technology import Technology
from db_configuration.db_offer import DbJob
from entities.job import Job


def main():
    db_technology = DbTechnology(DbConnection())
    db_offer = DbJob(DbConnection())
    languages = ['java', 'python', 'c', 'c#', 'html', 'css', 'angular', 'react js', 'javascript', 'go', 'android',
                 'flutter']
    sleeping_time = 20
    while True:
        for language in languages:
            fetch_website(language)
            print('\n\n\n')
            print(f'Now sleeping for {sleeping_time}')
            time.sleep(sleeping_time)


db_technology = DbTechnology(DbConnection())
db_job = DbJob(DbConnection())
db_job.drop_index()
db_job.drop_table()
db_technology.drop_index()
db_technology.drop_table()
db_technology.create_table()
db_technology.create_index()
db_job.create_table()
db_job.create_index()
db_technology.insert_technology(Technology(1, 'Html'))
db_technology.insert_technology(Technology(1, 'Css'))
db_technology.insert_technology(Technology(1, 'Java'))
db_technology.insert_technology(Technology(1, 'Python'))
db_technology.insert_technology(Technology(1, 'C'))
db_technology.insert_technology(Technology(1, 'C#'))
technologies = db_technology.select_technology()
print('List of technologies : \n')
for t in technologies:
    print(t)

print(f'Find a single element avec un id={1}')
print(db_technology.select_one_technology_by_id(1))

db_job.insert_offer(Job(1, 1, 'Java', 'Francais', 'Sesame', '01/01/2005', 'Paris', 'CDI', 'Dev', technologies[0]))
db_job.insert_offer(Job(1, 1, 'C', 'Anglais', 'Sesame', '01/01/2005', 'Paris', 'CDI', 'Dev', technologies[1]))
db_job.insert_offer(Job(1, 1, 'C++', 'Francais', 'Sesame', '01/01/2005', 'Paris', 'CDI', 'Dev', technologies[2]))
db_job.insert_offer(Job(1, 1, 'C#', 'Anglais', 'Sesame', '01/01/2005', 'Paris', 'CDI', 'Dev', technologies[3]))
print('List of offers : \n')
offers = db_job.select_offer()
for o in offers:
    print(o)

print(f'Find a single element avec un id={1}')
print(db_job.select_one_offer_by_id(offers[0].id))
