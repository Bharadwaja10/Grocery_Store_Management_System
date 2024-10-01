import mysql.connector
import datetime

#making it globally by initalizing none so that we dont need to close the connection everytime we use it makes reusable
__cnx=None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
      __cnx=mysql.connector.connect(user='root', password='967679', database='grocery')
  return __cnx
