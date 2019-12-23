class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Course:
    def __init__(self, id, category, name):
        self.id = id
        self.category = category
        self.name = name
