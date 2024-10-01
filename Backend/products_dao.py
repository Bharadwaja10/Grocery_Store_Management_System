from sql_connection import get_sql_connection

#To display all the in the manage products all the values are taken from the db and stored in the list like dictinary
def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select product_table.product_id, product_table.product_name, product_table.units, product_table.price_per_unit, units_table.units_name from product_table inner join units_table on product_table.units=units_table.unit_id")
    cursor.execute(query)
    response = []
    for (product_id, product_name, units, price_per_unit, units_name) in cursor:
        response.append({
            'product_id': product_id,
            'product_name': product_name,
            'units': units,
            'price_per_unit': price_per_unit,
            'units_name': units_name
        })
    return response

#To add new products in the product_table table
def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into product_table(product_name,units,price_per_unit)"
             " values (%s,%s,%s)")
    data = (product['product_name'], product['units'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

#To delete a record from the product_table
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM product_table where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid



if __name__ == '__main__':
    connection=get_sql_connection()
    # print(get_all_products(connection))
    # print(insert_new_product(connection, {
    #     'product_name': 'potatoe chips',
    #     'units': '1',
    #     'price_per_unit': 10
    # }))
    delete_product(connection, 14)

