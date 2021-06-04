class DbCategories:
    def __init__(self, category_id, category_desc):
        self.category_id = category_id
        self.category_desc = category_desc


class DbProducts:
    def __init__(self, product_id, product_name, product_desc, product_packaging, product_brand, product_cat,
                 product_store, product_nutriscore, product_link):
        self.product_id = product_id
        self.product_name = product_name
        self.product_desc = product_desc
        self.product_packaging = product_packaging
        self.product_brand = product_brand
        self.product_cat = product_cat
        self.product_store = product_store
        self.product_nutriscore = product_nutriscore
        self.product_link = product_link
