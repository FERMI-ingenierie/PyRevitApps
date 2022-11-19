# # -*- coding: utf-8 -*-

class ManufacturerProduct:
    def __init__(self):
        pass

    @classmethod
    def create(cls, kwargs):
            for key, value in kwargs.items():
                cls.key = value

    @property
    def aaa(self):
        return "{}_{}_{}".format(self.mark, self.gamme, self.reference)



    # @property
    # def klass(self):
    #     return False
    #
    # @property
    # def subklass(self):
    #     return False
    #
    # @property
    # def description(self):
    #     return False
    #
    # @property
    # def mark(self):
    #     return False
    #
    # @property
    # def gamme(self):
    #     return False
    #
    # @property
    # def reference(self):
    #     return False
    #
    # @property
    # def commande_code(self):
    #     return "{}_{}_{}".format(self.mark, self.gamme, self.reference)
    #











