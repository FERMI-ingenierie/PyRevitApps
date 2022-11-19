# # -*- coding: utf-8 -*-


class ManufacturerProduct:

    def __init__(self):
        # self.key_Schedulable = 'SP_FER_SCH_Schedulable'
        self.key_Fabricant = "SP_FER_ID_Fabricant"
        self.key_Fabricant_gamme = "SP_FER_ID_Fabricant gamme"
        self.key_Fabricant_reference = "SP_FER_ID_Fabricant référence"
        self.key_Product_URL = "SP_FER_ID_Product URL"

    @property
    def product_information(self):
        return "{}_{}_{}".format(getattr(self, "key_Fabricant","Unknown"),
                                 getattr(self, "key_Fabricant_gamme", "Unset"),
                                 getattr(self, "key_Fabricant_reference", "Unset"))
    @property
    def product_url(self):
        return "{}".format(getattr(self, "key_Product_URL"))

    @property
    def parameters_names (self):
        return self.key_Fabricant,\
               self.key_Fabricant_gamme,\
               self.key_Fabricant_reference,\
               self.key_Product_URL

    def set_data(self, key, value):
        setattr(self, key, value,)

    @property
    def test(self):
        return getattr(self, "SP_FER_ID_Fabricant", "No value")
