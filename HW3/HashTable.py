class HTable():

    def __init__(self):
        self.table = [[] for i in range(2**20)] #Size of the hash table

    # Since the distribution of the numbers about to be chosen follows a uniform distribution,
    # The hash function can be as simple as this
    def __get_value(self, key):
        value = key%(2**20)
        return value

    def insert(self, key):
        value = self.__get_value(key)
        self.table[value].append(key)

    def search(self, key):
        value = self.__get_value(key)
        if key in self.table[value]:
            return True
        else:
            return False