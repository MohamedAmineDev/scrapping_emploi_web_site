class Technology:
    def __init__(self, id=None, name=None):
        if id is not None and name is not None:
            self._id = id
            self._name = name
        else:
            self._id = ''
            self._name = ''

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f"Technology(id={self.id},name={self.name})\n"
