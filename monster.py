

class Monster():

    def __init__(self,name,tax_number,fur):
        self.name = name
        self.tax= tax_number
        self.__fur = fur

    def set_fur(self,fur):
        self.__fur = fur
        return

    def get_fur(self):
        return self.__fur
