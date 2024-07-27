from sql_connection import get_sql_connection


def get_all_customers(connection):
    cursor = connection.cursor()
    query1 = "select customer_name, total from customers"
    cursor.execute(query1)
    response_c = []
    for (customer_name, total) in cursor:
        response_c.append({
            'customer_name': customer_name,
            'total': total
        })
    return response_c


def insert_new_customer(connection, customer):
    data = (customer[0], customer[1])
    cursor1 = connection.cursor()
    query1 = "select * from customers where customer_name = %s"
    cursor1.execute(query1, (data[0],))
    result = cursor1.fetchone()

    if result:
        cursor = connection.cursor()
        update_query = "update customers set total = total + %s where customer_name = %s"
        cursor.execute(update_query, (data[1], data[0]))
    else:
        cursor = connection.cursor()
        query = ("INSERT INTO customers "
                 "(customer_name, total)"
                 "VALUES (%s, %s)")

        cursor.execute(query, (data[0], data[1]))

    connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
    # get_all_customers(connection)
    #print(insert_new_customer(connection, {
    #    'customer_name': "champ",
    #    'total': 233.5
    #}))
