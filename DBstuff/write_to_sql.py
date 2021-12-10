from db.connect import connect_to_db
from slugify import slugify
import pandas as pd


def write_to_sql(path):

    connection = connect_to_db()

    cursor = connection.cursor()
    
    df = pd.read_csv(path)
    
    for row in df.itertuples():
    
        cursor.execute('''
                    INSERT INTO football (Team, Manager, Founded, Website, Stadium_capacity)
                    VALUES (%s,%s,%s,%s,%s)
                    ''',
                    (row.Team,
                    row.Manager,
                    row.Founded,
                    row.Website,
                    row.Stadium_capacity
                    ))
    connection.commit()




