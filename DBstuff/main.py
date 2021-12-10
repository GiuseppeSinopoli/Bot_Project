from db.connect import connect_to_db
from slugify import slugify



connection = connect_to_db()

cursor = connection.cursor()


# get blogs

# get_blog_query = "SELECT * FROM blogs;"

# cursor.execute(get_blog_query)

# result = cursor.fetchall()

# print(len(result))




def insert_team(title,summary,author):
    try:
        cursor.execute("""INSERT INTO
	homework(
		team,
        manager,
		founded,
		website,
		stadium_capacity
	)
	VALUES(
		%s,
		%s,
		%s,
		%s;
		%s
        )""",(title,summary,author,slugify(title)))
        connection.commit()
    except Exception as e:
        print(e)



insert_team("Article_2",'FROM PYTHON','Giuseppe')