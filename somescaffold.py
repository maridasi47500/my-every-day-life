# -*- coding: utf-8 -*-

import sys
import os
class Scaffold():
    def __init__(self,arg1,items=["name"]):
        print(arg1)
        filename=arg1.lower()
        myclass=(filename).capitalize()
        modelname=(filename).capitalize()
        marouteget="\"/%s\"" % filename
        maroutenew="\"/%s_new\"" % filename
        maroutecreate="\"/%s_create\"" % filename
        marouteget2="\\\"/%s\\\"" % filename
        myhtml="my"+filename+"html"
        myfavdirectory=filename
        index = 0
        createtable=""
        columns="("
        values="("
        myparam=","
        while index < (len(items)):
        
            try:
              print(index, items[index])
              paramname=items[index]
              print(items[(index+1)])
            except:
              myparam=""
            index += 1
            columns+="{paramname}{myparam}".format(myparam=myparam,paramname=paramname)
            values+=":{paramname}{myparam}".format(myparam=myparam,paramname=paramname)
            createtable+="""        {paramname} text{myparam}
            """.format(myparam=myparam,paramname=paramname)
        columns+=")"
        values+=")"
        mystr="""# coding=utf-8
        import sqlite3
        import sys
        import re
        from model import Model
        from stuff import Stuff
        class {modelname}(Stuff):
            def __init__(self):
                self.tablename="{filename}"
                self.con=sqlite3.connect(self.mydb)
                self.con.row_factory = sqlite3.Row
                self.cur=self.con.cursor()
                self.cur.execute(\"\"\"create table if not exists {filename}(
                id integer primary key autoincrement,
        """
        mystr+=createtable
        
        mystr+=""",
            Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );\"\"\")
                self.con.commit()
                #self.con.close()
            def getall(self):
                self.cur.execute("select * from {filename}")
        
                row=self.cur.fetchall()
                return row
            def deletebyid(self,myid):
        
        """
        mystr+="""        self.cur.execute("delete from {filename} where id = ?",(myid,))
                job=self.cur.fetchall()
                self.con.commit()
                return None
            def getbyid(self,myid):
                self.cur.execute("select * from {filename} where id = ?",(myid,))
                row=dict(self.cur.fetchone())
                print(row["id"], "row id")
                job=self.cur.fetchall()
                return row
            def addnew{filename}(self,myid):
                inp="0"
                stuff=""

                while inp != "n" and inp != "quit":
                    inp = input('will u tell me any more {filename}? [y/n/quit]') 

                    if inp == "y":
                        print("ok")
                        while stuff.strip() == "":
                            stuff=input("what {filename}?")
                            self.create({"name": stuff})

                    elif inp == "n":
                        print("ok")
                    elif inp == "quit":
                        print("bye")
                    elif input !== "y":
                        print("only answer y, n or quit")
                return row
            def create(self,params):
                print("ok")
                myhash={myhash}
                for x in params:
                    if 'confirmation' in x:
                        continue
                    if 'envoyer' in x:
                        continue
                    if '[' not in x and x not in ['routeparams']:
                        #print("my params",x,params[x])
                        try:
                          myhash[x]=str(params[x].decode())
                        except:
                          myhash[x]=str(params[x])
                print("M Y H A S H")
                print(myhash,myhash.keys())
                myid=None
                try:
                  self.cur.execute("insert into {filename} {columns} values {values}",myhash)
                  self.con.commit()
                  myid=str(self.cur.lastrowid)
                except Exception as e:
                  print("my error"+str(e))
                azerty={notice}
                azerty["{filename}_id"]=myid
                azerty["notice"]="votre {filename} a été ajouté"
                return azerty
        
        
        
        
        """
        self.filename=filename
        self.modelname=modelname
        self.columns=columns
        self.values=values
        self.mystr=mystr
    def wrotetofile(self):
        if not os.path.isfile(self.filename+".py"):
          f = open(self.filename+".py", "w") 
          res=(self.mystr.format(modelname=self.modelname,filename=self.filename,columns=self.columns,values=self.values,myhash={},notice={}))
          print(res)
          f.write(res)
          f.close()
