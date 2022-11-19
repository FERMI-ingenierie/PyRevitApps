# # -*- coding: utf-8 -*-

import requests

class ManufacturerProduct:

    def __init__(self):
        self.key_Schedulable = 'SP_FER_SCH_Schedulable'
        self.key_Fabricant = "SP_FER_ID_Fabricant"
        self.key_Fabricant_gamme = "SP_FER_ID_Fabricant gamme"
        self.key_Fabricant_reference = "SP_FER_ID_Fabricant référence"
        self.key_Product_URL = "SP_FER_ID_Product URL"

    @property
    def is_schedulable(self):
        _bool = getattr(self,"SP_FER_SCH_Schedulable",False)
        if _bool == 1 or '1':
            return True
        return False

    @property
    def product_information(self):
        return "{}_{}_{}".format(getattr(self, "SP_FER_ID_Fabricant","Unknown"),
                                 getattr(self, "SP_FER_ID_Fabricant gamme", "Unset"),
                                 getattr(self, "SP_FER_ID_Fabricant référence", "Unset"))
    @property
    def product_url(self):
        return "{}".format(getattr(self, "SP_FER_ID_Product URL", False))

    @property
    def parameters_names (self):
        return self.key_Fabricant,\
               self.key_Fabricant_gamme,\
               self.key_Fabricant_reference,\
               self.key_Product_URL

    def set_data(self, key, value):
        setattr(self, key, value,)















downloadUrl = 'https://www.trilux.com/products/pdf/o____F010228293.pdf'

req = requests.get(downloadUrl)
filename = req.url[downloadUrl.rfind('/')+1:]

with open(filename, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

def download_file(url, filename=''):
    try:
        if filename:
            pass
        else:
            filename = req.url[downloadUrl.rfind('/')+1:]

        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None


downloadLink = 'https://www.trilux.com/products/pdf/o____F010228293.pdf'

download_file(url=downloadLink, filename='aaaaa.pdf')



class DatasheetsProductDownloader:
    downloadUrl = ''

    def __init__(self, manufacturer_product):
        """
        Download datasheets products

        :param manufacturer_product: products
        :type manufacturer_product: ManufacturerProduct
        :return None
        :return
        """
        pass


    @property
    def products(self):
        return False


    @products.setter
    def products(self, elements = []):
        pass

    def destination_path(self):
        pass

    def downlaoder(self):
        pass
