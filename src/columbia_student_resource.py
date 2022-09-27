import pymysql

import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        # usr = os.environ.get("")
        # pw = os.environ.get("DBPW")
        # h = os.environ.get("DBHOST")

        usr = "admin"
        pw = "Aws0925Yy!"
        h = "e61561.cy3ibfupequv.us-east-1.rds.amazonaws.com"

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_student where uni=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

