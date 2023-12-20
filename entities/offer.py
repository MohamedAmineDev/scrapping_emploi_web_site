from entities.technology import Technology


class Offer:
    def __init__(self, id=None, experience=None, skills=None, languages=None, name=None, date=None, address=None,
                 contract_type=None, qualification=None, technology=None):
        if id is not None and experience is not None and skills is not None and languages is not None and name is not None and date is not None and address is not None and contract_type is not None and qualification is not None and technology is not None:
            self._id = id
            self._experience = experience
            self._skills = skills
            self._languages = languages
            self._name = name
            self._date = date
            self._address = address
            self._contract_type = contract_type
            self._qualification = qualification
            self._technology = technology
        else:
            self._id = ''
            self._experience = ''
            self._skills = ''
            self._languages = ''
            self._name = ''
            self._date = ''
            self._address = ''
            self._contract_type = ''
            self._qualification = ''
            self._technology = Technology()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value

    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, value):
        self._skills = value

    @property
    def languages(self):
        return self._languages

    @languages.setter
    def languages(self, value):
        self._languages = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def contract_type(self):
        return self._contract_type

    @contract_type.setter
    def contract_type(self, value):
        self._contract_type = value

    @property
    def qualification(self):
        return self._qualification

    @qualification.setter
    def qualification(self, value):
        self._qualification = value

    @property
    def technology(self):
        return self._technology

    @technology.setter
    def technology(self, value):
        self._technology = value

    def __str__(self):
        return f"offer(id={self.id},technology_id={self.technology.id},entreprise_name={self.name},skills=[{self.skills}],date={self.date},address={self.address},contract_type={self.contract_type},qualification={self.qualification},experience={self.experience},language={self.languages}\n"
