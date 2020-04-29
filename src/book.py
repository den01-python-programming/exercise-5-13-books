class Book:

    def __init__(self,name,publication_year):
        self.name = name
        self.publication_year = publication_year

    def get_name(self):
        return self.name

    def get_publication_year(self):
        return self.publication_year

    def __eq__(self,compared):
        if (self.name == compared.name and self.publication_year == compared.publication_year):
            return True

        return False
