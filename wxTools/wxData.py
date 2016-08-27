#conding:utf-8
import json
import MySQLdb

def selectFromeTable(con,lookingforstr,tablename,conditions=''):
    if conditions!='':
        statement='SELECT %s FROM %s WHERE %s'%(lookingforstr,tablename,conditions)
        con.excute(statement)
        con.commit()