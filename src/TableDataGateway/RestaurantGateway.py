import psycopg2
from contextlib import closing


class RestaurantGateway:
    def __init__(self):
        self.metro = None
        self.kitchen = None
        self.avg_bill = None

        self.tablename = 'restaurants'
        self.connect = "host='localhost' dbname='nikita' user='' password=''"

    def Insert(self):
        with closing(psycopg2.connect(self.connect)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""INSERT INTO {self.tablename} (metro, kitchen, avg_bill)
                            VALUES ('{self.metro}', '{self.kitchen}', {self.avg_bill})
                            """)
                conn.commit()
        return

    def getAll(self):
        with closing(psycopg2.connect(self.connect)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""
                    SELECT * FROM {self.tablename}
                """)

                rows = cursor.fetchall()
        return rows

    def getLastId(self):
        with closing(psycopg2.connect(self.connect)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT id FROM {self.tablename}""")
                lastId = cursor.fetchall()[-1][0]
        return lastId

    def getLastRestaurant(self, id):
        with closing(psycopg2.connect(self.connect)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM {self.tablename} WHERE id = {id}""")
                restaurantInfo = cursor.fetchone()
        return restaurantInfo
