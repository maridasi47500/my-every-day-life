# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Stuff(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.con.commit()
        #self.con.close()
    def getallstuff(self):
        self.cur.execute("select "+self.tablename+".*, count("+self.tablename+".user_id) as countuser, ( select count(distinct x.user_id) from "+self.tablename+" x ) usertotal from "+self.tablename+" group by "+self.tablename+".name")

        row=self.cur.fetchall()
        return row
