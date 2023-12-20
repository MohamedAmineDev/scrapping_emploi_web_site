def fetch_experience(line):
    experience = line.find('span', class_='skill-name')
    if experience:
        return experience.text
    return 'Unknown'


def fetch_skills(line):
    ch = ''
    competences = line.find_all('li')
    for competence in competences:
        skill = competence.find('span', itemprop='skills').text
        if len(ch) == 0:
            ch = f'{skill}'
        else:
            ch = f'{ch},{skill}'

    return ch


def fetch_language(line):
    ch = str()
    languages = line.find_all('span', class_='skill-name')
    if languages:
        for language in languages:
            if len(ch) == 0:
                ch = f'{language.text}'
            else:
                ch = f'{ch},{language.text}'
    if not ch:
        return 'Unknown'
    return ch


def fetch_title(soup):
    entreprise = soup.find('div', class_='media')
    body = soup.find('div', class_='media-body')
    # print(body)
    name = body.find('h3', class_='title')
    if name:
        return name.text.strip()
    return 'Unknown'


def fetch_date(soup):
    date_element = soup.find('p', class_='t5 title-complementary')
    date_value = date_element.find('span')
    if date_value:
        return date_value.text.strip()
    return 'Unknown'


def fetch_address(soup):
    address_element = soup.find('span', itemprop='name')
    if address_element:
        return address_element.text.strip()
    return 'Unknown'


def fetch_type_contract(soup):
    contract_element = soup.find('dl', class_='icon-group')
    contract_value = contract_element.find('dd')
    return contract_value.text.split('\n')[1]


def fetch_qualification(soup):
    qualification_element = soup.find('span', itemprop='qualifications')
    if qualification_element:
        return qualification_element.text.strip()
    return 'Unknown'


def fetch_id_offer(soup):
    id_element = soup.find('span', itemprop='value')
    if id_element:
        return id_element.text.strip()
    return 'Unknown'
