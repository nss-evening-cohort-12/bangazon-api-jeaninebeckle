import sqlite3
from django.shortcuts import render
from bangazonapi.models import Product
from bangazonreports.views import Connection


def lowproductprice_list(request):
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all products, with related price info.
            db_cursor.execute("""
              SELECT 
                p.name,
                p.description,
                p.price
              FROM bangazonapi_product p
              WHERE p.price <= 999
            """)

            dataset = db_cursor.fetchall()

            products_priced_under_1000 = []

            for row in dataset:
                # Create a Product instance and set its properties. String in brackets matches the SQL results
                product = Product()
                product.name = row["name"]
                product.description = row["description"]
                product.price = row["price"]

                products_priced_under_1000.append(product)

        # Specify the Django template and provide data context
        template = 'products/products_under_1000.html'
        context = {
            'lowproductprice_list': products_priced_under_1000
        }

        return render(request, template, context)
