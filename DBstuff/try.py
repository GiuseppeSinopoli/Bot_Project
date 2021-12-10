from db.connect import connect_to_db
from slugify import slugify
import pandas as pd


connection = connect_to_db()

cursor = connection.cursor()


data = pd.read_csv("team_summary.csv")

