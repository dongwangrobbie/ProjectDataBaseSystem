from config.dbconfig import pg_config
import psycopg2

# This is the way I can login to the database
# conn = psycopg2.connect("dbname=p1 user=DongWang password=wangdong host =127.0.0.1")

class PartsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllParts(self):
        cursor = self.conn.cursor()
        query = "select * from resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPartById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from resource where resource_id = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def delete(self, pid):
        cursor = self.conn.cursor()
        query = "delete from resource where resource_id = %s;"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return pid

    def update(self, resource_id, res_type, unit_price):
        cursor = self.conn.cursor()
        query = "update resource set resource_id = %s, res_type = %s, unit_price = %s where resource_id = %s;"
        cursor.execute(query, (resource_id, res_type, unit_price,))
        self.conn.commit()
        return resource_id



