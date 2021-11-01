import os
from imbox import Imbox # pip install imbox
import traceback
import email
from mysql.connector.connection import MySQLConnection
import pymongo
import mysql.connector
from pymongo import MongoClient
import gridfs


host = "imap.gmail.com"
username = "barywoad@gmail.com"
password = 'BARYWOAD165@'
download_folder = "D:\DataScience\WEEK 2\Industry Project\Attachments"

if not os.path.isdir(download_folder):
    os.makedirs(download_folder, exist_ok=True)
    
mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)
messages = mail.messages(sent_from='sargundeepkaur.s@somaiya.edu',unread=True) # defaults to inbox

for (uid, message) in messages:
    print(message.keys())
    x=message.body['plain'][0]
    new_x=[]
    for x1 in x:
        new_x = x.replace("\r\n\r\n", " , ")
    
    new_x=new_x.split(" ") 
    print(new_x)
    print(new_x[0]) 
    print(new_x[4])
    print(new_x[8])
    print(new_x[12])
    x=new_x[16]+new_x[17]+new_x[18]+new_x[19]
    print(x)
    con=None
    try:
        
        con =mysql.connector.connect(host='localhost',database='textmail',user='root',password='abc123')
        mySql_insert_query = "INSERT INTO emailbody VALUES('%s','%s','%s','%s','%s')"
        cursor = con.cursor()
        cursor.execute(mySql_insert_query %(new_x[0],new_x[4],new_x[8],new_x[12],x))
        con.commit()
        print(cursor.rowcount, "Record inserted successfully into emailbody table")
        cursor.close()

    except Exception as error:
        print("Failed to insert record into emailbody table {}".format(error))

    finally:
        if con is not None:
            con.close()
            # print("MySQL connection is closed")
    for idx, attachment in enumerate(message.attachments):
        try:
            att_fn = attachment.get('filename')
            # print(att_fn)
            download_path = f"{download_folder}/{att_fn}"
            # print(download_path)
            with open(download_path, "wb") as fp:
                fp.write(attachment.get('content').read())
                # databases = pymongo.MongoClient()
                # text_db = databases.text
                # tutorial_collection = text_db.attachment
                def mongo_conn():
                    try:
                        conn=MongoClient(host='127.0.0.1',port=27017)
                        print("Mongo connected",conn)
                        return conn.grid_file
                    except Exception as e:
                        print("error in mongo connection: ",e)
                db=mongo_conn()
                name=att_fn
                file_location="/DataScience/WEEK 2/Industry Project/Attachments/" + name
                file_data=open(file_location,"rb")
                data=file_data.read()
                fs=gridfs.GridFS(db)
                fs.put(data,filename=name)
                print("Upload completed")

        except:
            print(traceback.print_exc())
    

mail.logout()