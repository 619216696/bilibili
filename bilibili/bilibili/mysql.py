import pymysql

db = pymysql.connect(host = 'localhost',user = 'root',password = '********',db = 'bilibili',charset = 'utf8')
cur = db.cursor()

class sql:

    @classmethod

    def insert_data(cls,name_,uid,play_num,sex,birthday,area,reg_time,coins,article,level_,exp,description,fans,following):
        sql = 'insert into bilibili(uid,name_,sex,area,fans,following,birthday,play_num,coins,article,level_,exp,reg_time,description)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql,(uid,name_,sex,area,fans,following,birthday,play_num,coins,article,level_,exp,reg_time,description))
        db.commit()

    @classmethod
    def ifexists(cls,uid):
        sql = 'select exists(select 1 from bilibili where uid=%s)'
        cur.execute(sql,uid)
        result = cur.fetchall()[0][0]
        return int(result)

    @classmethod
    def not_requests(cls):
        sql = 'select * from not_requests'
        cur.execute(sql)
        results = cur.fetchall()
        return results

    @classmethod
    def delete_requested(cls,uid):
        sql = 'delete from not_requests where uid=%s'
        cur.execute(sql,uid)
        db.commit()