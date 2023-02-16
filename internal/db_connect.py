import mysql.connector
import pandas as pd

# Connect to phpMyAdmin or
# Connect to docker admin
# onlineDB = mysql.connector.connect(
#     host='192.168.2.135',
#     user='bas',
#     password='VRQ?4e5koQ!f1KT@hM',
#     port='3306',
#     database='pmt_jumboshadow'
# )
dockerDB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='example',
    port='3308',
    database='db1'
)


def execute_twd(usedDB):
    mycursor = usedDB.cursor()

    mycursor.execute(
        "SELECT store_id, subdepartment_id, year, week, day, turnover, nr_customers, items_out "
        "FROM subdepartment_turnover_week_day "
        "WHERE store_id = 508 "
        "AND subdepartment_id = 160 "
        "AND status = 'actual';"
    )
    twd = mycursor.fetchall()

    usedDB.close()
    return twd


def execute_twd_ordered_turnover(usedDB):
    mycursor = usedDB.cursor()

    mycursor.execute(
        "SELECT store_id, subdepartment_id, year, week, day, turnover, nr_customers, items_out "
        "FROM subdepartment_turnover_week_day "
        "WHERE store_id = 508 "
        "AND subdepartment_id = 160 "
        "AND status = 'actual' "
        "ORDER BY turnover ASC;"
    )
    twd = mycursor.fetchall()

    usedDB.close()
    return twd


def sqlToPandas(table, columns, dropCols=[]):
    df = pd.DataFrame(table, columns=columns)
    df = df.drop(dropCols, axis=1)
    return df