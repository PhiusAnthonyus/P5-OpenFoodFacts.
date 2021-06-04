CREATE DATABASE openfoodfacts;
USE openfoodfacts;

CREATE TABLE Category (
    category_id SMALLINT NOT NULL AUTO_INCREMENT,
    category_desc VARCHAR(255) NULL,
    CONSTRAINT category_id PRIMARY KEY (category_id)
);

CREATE TABLE Product (
    product_id INT NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(255) NULL,
    product_desc TEXT NULL,
    product_packaging TEXT NULL,
	product_brand TEXT NULL,
	product_cat TEXT NULL,
	product_store TEXT NULL,
    product_nutriscore CHAR(1) NULL,
	product_link VARCHAR(255) NULL,
    CONSTRAINT product_id PRIMARY KEY (product_id)
);

CREATE TABLE Wishlist (
    product_id INT NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(255) NULL,
    product_desc TEXT NULL,
    product_packaging TEXT NULL,
	product_brand VARCHAR(50) NULL,
	product_cat TEXT NULL,
	product_store TEXT NULL,
    product_nutriscore CHAR(1) NULL,
	product_link VARCHAR(255) NULL,
    CONSTRAINT product_id PRIMARY KEY (product_id)
);
