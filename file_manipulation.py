import os.path
from offer import Offer
file_name = 'offre_emploi_dataset.csv'
file_header = 'id;skill;name;skills;date;address;contract_type;qualification;experience;languages\n'


def add_content(offer):
    if not os.path.exists(file_name):
        create_file()
    with open(file_name, 'a') as file:
        if file.writable():
            file.write(offer)


def create_file():
    with open(file_name, 'w') as file:
        file.write(file_header)


def find_offer(offer_id):
    if not os.path.exists(file_name):
        create_file()
    with open(file_name, 'r') as file:
        next(file)
        for row in file:
            cols = row.split(';')
            if cols[0] == offer_id:
                return True
    return False
