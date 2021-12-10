import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


DBHOST = os.environ.get("DBHOST")
DBNAME= os.environ.get("DBNAME")
DBUSER= os.environ.get("DBUSER")
DBPASSWORD= os.environ.get("DBPASSWORD")



def db(database_name='pepe'):
    return psycopg2.connect(database=database_name)

def query_db(query, args=(), one=False):
    cur = db().cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r

my_query = query_db("select * from majorroadstiger limit %s", (3,))

json_output = json.dumps(my_query)