
def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from units_table")
    cursor.execute(query)
    response = []
    for (unit_id, units_name) in cursor:
        response.append({
            'unit_id': unit_id,
            'units_name': units_name
        })
    return response


if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_uoms(connection))