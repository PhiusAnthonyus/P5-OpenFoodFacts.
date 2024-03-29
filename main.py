import pymysql
import requests
from classes import DbProducts, DbCategories


class Browser:
    """Main class of the program"""
    def __init__(self):
        self.category = load_categories()
        self.product = load_products()

    def display_categories_browser(self):
        """Browse categories"""
        page_min = 0
        page_max = 10
        while "main":
            print("Il y a {} catégories.".format(len(self.category)))
            print("Sélectionnez une catégorie:")

            if len(self.category) - page_max < 10 <= page_max:
                page_max += len(self.category) - page_max
                if page_max < 10:
                    page_min = 0
                else:
                    page_min = page_max - 10
            if page_min < 0:
                page_min = 0
                page_max = 10

            for i in range(page_min, page_max):
                print("{} -> {}".format(self.category[i].category_id,
                                        self.category[i].category_desc))

            choice = input("Numéro -> selectionner la catégorie "
                           "| > -> page suivante | < -> page précédente "
                           "| 0 -> retour au menu principal\n")

            if choice == '0':
                break
            if choice == '>':
                page_max += 10
                page_min += 10
            if choice == '<' and page_min > 0:
                page_max -= 10
                page_min -= 10
            if choice.isdigit():
                self.display_products_browser(int(choice) - 1,
                                              self.category[int(choice) - 1]
                                              .category_desc)

    def display_products_browser(self, category_id, category_desc):
        """Browse products from the designated category."""
        category_products = self.create_products_list(category_desc)
        page_min = 0
        page_max = 10
        while "main":
            if len(category_products) - page_max < 10 <= page_max:
                page_max += len(category_products) - page_max
                if page_max < 10:
                    page_min = 0
                else:
                    page_min = page_max - 10
            if page_min < 0:
                page_min = 0
                page_max = 10

            print("Affichage des produits de la catégorie {} |"
                  "Page : {}".format(self.category[category_id].category_desc,
                                     int(page_max / 10)))
            for i in range(page_min, page_max):
                print(
                    "{} -> {} {}".format(i + 1,
                                         category_products[i].product_name,
                                         category_products[i].product_brand))

            choice = input("Numéro -> selectionner un produit "
                           "| > -> page suivante | < -> page précédente "
                           "| 0 -> retour aux catégories\n")

            if choice == '0':
                break
            if choice == '>':
                page_max += 10
                page_min += 10
            if choice == '<' and page_min > 0:
                page_max -= 10
                page_min -= 10
            if choice.isdigit():
                if 0 < int(choice) <= len(category_products):
                    self.display_product_description(
                        category_products[int(choice) - 1],
                        self.category[category_id].category_desc)

    def create_products_list(self, category_desc):
        """Create a list of products from the designated category."""
        category_products = list()
        for element in self.product:
            try:
                element.product_cat.index(category_desc)
                category_products.append(element)
            except Exception:
                continue
        return category_products

    def display_product_description(self, products, category_name):
        """Show product description."""
        while "main":
            print("Fiche Produit\n")
            print("Id du produit : " + str(products.product_id))
            print("Nom du produit : " + products.product_name)
            print("Description : " + products.product_desc)
            print("Conditionnement : " + products.product_packaging)
            print("Marque : " + products.product_brand)
            print("Catégorie : " + products.product_cat)
            print("Magasin : " + products.product_store)
            print("Nutri-score : " + products.product_nutriscore.upper())
            print("URL : " + products.product_link)

            choice = input(
                "(1 -> Rechercher un substitut |"
                " 2 -> Supprimer le produit des favoris |"
                " 3 -> Enregistrer le produit dans les favoris |"
                " 0 -> Retour à la catégorie {})\n".format(category_name))
            if choice == '0':
                break

            if choice == '1':
                self.display_substitutes_browser(products)

            if choice == '2':
                self.clear_favorite(products)

            if choice == '3':
                self.save_favorite(products)

    def display_substitutes_browser(self, products):
        """Browse substitute products in category."""
        substitutes = self.get_substitutes(products)
        page_min = 0
        page_max = 10
        while "main":
            if len(substitutes) - page_max < 10 <= page_max:
                page_max += len(substitutes) - page_max
                if page_max < 10:
                    page_min = 0
                else:
                    page_min = page_max - 10
            if page_min < 0:
                page_min = 0
                page_max = 10

            print("Il y a {} substitution(s) pour le produit \"{}\" : \n"
                  .format(len(substitutes), products.product_name))
            if len(substitutes) == 0:
                print("Vous utilisez déjà un produit sain "
                      "selon OpenFoodFacts.\n")
                break
            else:
                for i in range(page_min, page_max):
                    print("{} - {} {}".format(i + 1,
                                              substitutes[i].product_name,
                                              substitutes[i].product_brand))

            choice = input("Numéro -> selectionner un produit |"
                           " > -> page suivante |"
                           " < -> page précedente |"
                           " 0 -> revenir à la fiche produit\n")

            if choice == '0':
                break
            if choice.isdigit():
                self.display_product_description(
                    substitutes[int(choice) - 1],
                    "substitution de {}".format(products.product_name))
                continue
            if choice == '>':
                page_min += 10
                page_max += 10
            if choice == '<' and page_min > 0:
                page_min -= 10
                page_max -= 10

    def create_substitute_list(self, category_desc):
        """Create a list of substitutes that corresponds
        to categories of the product."""
        category_products = list()
        for element in self.product:
            try:
                category_desc.index(element.product_cat)
                category_products.append(element)
            except Exception:
                continue
        return category_products

    def get_substitutes(self, products):
        """Nutrition grade comparison"""
        result = self.create_substitute_list(products.product_cat)
        substitute = list()
        for element in result:
            if element.product_nutriscore >= products.product_nutriscore:
                continue

            substitute.append(element)
        return substitute

    def save_favorite(self, products):
        """Save the selected product in the wishlist"""
        cursor = login.login.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM Wishlist")
        result = cursor.fetchall()
        exist = False
        for element in result:
            # Test if the product already exist in the user's list
            if element['product_link'] == products.product_link:
                exist = True
        if exist:
            print("Le produit existe déjà dans vos favoris.")
        else:
            cursor.execute(
                'INSERT INTO Wishlist('
                'product_name, product_desc, '
                'product_packaging, product_brand, product_cat, '
                'product_store, product_nutriscore, '
                'product_link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (products.product_name, products.product_desc,
                 products.product_packaging, products.product_brand,
                 products.product_cat, products.product_store,
                 products.product_nutriscore, products.product_link))
            print("Produit sauvegardé.")
        cursor.close()
        login.login.commit()

    def clear_favorite(self, products):
        """Clear the selected product in the wishlist"""
        cursor = login.login.cursor(pymysql.cursors.DictCursor)
        sql = "DELETE FROM Wishlist WHERE product_link = '%s' "
        cursor.execute(sql % products.product_link)
        cursor.close()
        login.login.commit()
        print("Produit supprimé des favoris.")

    def get_products_from_wishlist(self):
        """Get the list of favorite products from the db"""
        cursor = login.login.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM Wishlist")
        result = cursor.fetchall()
        cursor.close()
        db_products = list()
        for element in result:
            db_products.append(DbProducts(element['product_id'],
                                          element['product_name'],
                                          element['product_desc'],
                                          element['product_packaging'],
                                          element['product_brand'],
                                          element['product_cat'],
                                          element['product_store'],
                                          element['product_nutriscore'],
                                          element['product_link']))
        return db_products

    def display_favorite_product_browser(self):
        """Display the user's saved product from the db"""
        page_min = 0
        page_max = 10
        while "main":
            u_products = self.get_products_from_wishlist()

            if len(u_products) - page_max < 10 <= page_max:
                page_max = len(u_products)
                if page_max < 10:
                    page_min = 0
                else:
                    page_min = page_max - 10
            if page_min < 0:
                page_min = 0
                page_max = 10
            if len(u_products) < 10:
                page_max = len(u_products)
                page_min = 0

            print("Liste des produits enregistrés :")
            for i in range(page_min, page_max):
                print("{} - {} {}".format(i + 1,
                                          u_products[i].product_name,
                                          u_products[i].product_brand))
            choice = input("Numéro -> selectionner un produit |"
                           " > -> page suivante |"
                           " < -> page précedente |"
                           " 0 -> revenir au menu principal\n")

            # Exit substitute manager
            if choice == '0':
                break

            if choice == '>':
                page_max += 10
                page_min += 10

            if choice == '<' and page_min > 0:
                page_max -= 10
                page_min -= 10

            # Select product
            if choice.isdigit():
                if 0 < int(choice) <= len(u_products):
                    self.display_product_description(
                        u_products[int(choice) - 1], "votre liste")


class Login:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.charset = 'utf8mb4'
        self.db = 'openfoodfacts'
        self.password = input(
            'Entrez le mot de passe de votre base de données :\n')
        self.login = None

    def db_connection(self):
        self.login = pymysql.connect(user=self.user,
                                     password=self.password,
                                     host=self.host,
                                     charset=self.charset,
                                     db=self.db)


def load_categories():
    """Load all categories from the db"""
    # Import data
    cursor = login.login.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM Category')
    result = cursor.fetchall()
    cursor.close()
    # Read data
    db_categories = []
    for element in result:
        db_categories.append(DbCategories(element['category_id'],
                                          element['category_desc']))
    return db_categories


def load_products():
    """Load a list of products from the db"""
    # Import data
    cursor = login.login.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Product")
    result = cursor.fetchall()
    cursor.close()
    # Read data
    db_products = []
    for element in result:
        db_products.append(DbProducts(element['product_id'],
                                      element['product_name'],
                                      element['product_desc'],
                                      element['product_packaging'],
                                      element['product_brand'],
                                      element['product_cat'],
                                      element['product_store'],
                                      element['product_nutriscore'],
                                      element['product_link']))
    return db_products


class Update:
    def __init__(self):
        self.link_api = 'https://fr.openfoodfacts.org/'
        self.category = []
        self.product = []

    def api_get(self, path):
        """Get json file from API"""
        path = "%s%s.json" % (self.link_api, path)
        answer = requests.get(path)
        print(answer.status_code)
        return answer.json()

    def update(self):
        """Delete old data and get new one"""
        cursor = login.login.cursor()
        # Clear data in tables
        cursor.execute('TRUNCATE TABLE category')
        cursor.execute('TRUNCATE TABLE product')

        print("Mise à jour des produits...")
        self.get_products_from_api()

        # Update categories
        print("Mise à jour des catégories...")
        category = self.api_get("categories")
        cleared_categories = []
        for element in category["tags"]:
            if element['products'] < 50:
                continue
            if element['id'][:3] not in ['en:', 'fr:']:
                continue
            cleared_categories.append(element)

        for element in cleared_categories:
            cursor.execute('INSERT INTO Category(category_desc) VALUES (%s)',
                           (element['name']))
        login.login.commit()
        cursor.close()
        print("Données à jour.")

    def get_products_from_api(self):
        # Send request from API.
        result = requests.get(
            "https://fr.openfoodfacts.org/cgi/search.pl?"
            "page_size=1000&page={}&action=process&json=1").json()
        for element in result['products']:
            if not all(tag in element for tag in (
                    "id", "product_name", "generic_name", "packaging",
                    "brands", "packaging", "categories_tags", "stores",
                    "nutrition_grade_fr", "url")):
                continue
            self.product.append(DbProducts(element['id'],
                                           element['product_name'],
                                           element['generic_name'],
                                           element['packaging'],
                                           element['brands'],
                                           element['categories'],
                                           element['stores'],
                                           element['nutrition_grade_fr'],
                                           element['url']))
        self.save_products()

    def save_products(self):
        """Save all the products in the db"""
        cursor = login.login.cursor(pymysql.cursors.DictCursor)
        for element in self.product:
            cursor.execute(
                'INSERT INTO Product(product_name, product_desc, '
                'product_packaging, product_brand, product_cat, '
                'product_store, product_nutriscore, product_link'
                ') VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (element.product_name, element.product_desc,
                 element.product_packaging, element.product_brand,
                 element.product_cat, element.product_store,
                 element.product_nutriscore, element.product_link))
        cursor.close()
        login.login.commit()


class Program:
    def main_menu(self):
        main = True
        update = Update()
        browser = Browser()

        while main:
            print('1 -> Mettre à jour la base de données.\n'
                  '2 -> Faire une recherche.\n'
                  '3 -> Afficher les favoris.\n4'
                  ' -> Quitter')
            choice = int(input())
            if choice == 1:
                update.update()
                browser = Browser()
            elif choice == 2:
                browser.display_categories_browser()
            elif choice == 3:
                browser.display_favorite_product_browser()
            elif choice == 4:
                main = False


login = Login()
login.db_connection()
program = Program()
program.main_menu()
