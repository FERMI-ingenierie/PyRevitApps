# # -*- coding: utf-8 -*-


class ManufacturerProduct:

    def __init__(self):
        # self.key_Schedulable = 'SP_FER_SCH_Schedulable'
        self.key_Fabricant = 'SP_FER_ID_Fabricant'
        self.key_Fabricant_gamme = 'SP_FER_ID_Fabricant gamme'
        self.key_Fabricant_reference = 'SP_FER_ID_Fabricant référence'
        self.key_Product_URL = 'SP_FER_ID_Product URL'

    @property
    def product_information(self):
        return "{}_{}_{}".format(getattr(self, "key_Fabricant"),
                                 getattr(self, "key_Fabricant_gamme"),
                                 getattr(self, "key_Fabricant_reference"))
    @property
    def product_url(self):
        return "{}".format(getattr(self, "key_Product_URL"))

    @property
    def parameters_names (self):
        return (self.key_Fabricant,
                self.key_Fabricant_gamme,
                self.key_Fabricant_reference,
                self.key_Product_URL)

    def set_data(self, key, value):
        setattr(self, key, value)

    @property
    def test(self):
        return getattr(self, "key_Fabricant")





    # class Outer(object):
    #
    #     def createInner(self):
    #         return Outer.Inner(self)
    #
    #     class Inner(object):
    #         def __init__(self, outer_instance):
    #             self.outer_instance = outer_instance
    #             self.outer_instance.somemethod()
    #
    #         def inner_method(self):
    #             self.outer_instance.anothermethod()

    # class TestClass(object):
    #     def __init__(self, **kwargs):
    #         for key, value in kwargs.items():  # items return list of dict
    #             setattr(self, key, value)

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











