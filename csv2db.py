# This script is not related to this project and is only used to read CSV files and write to the database.

import pandas as pd

import sqlite3


conn = sqlite3.connect('db.sqlite3')

query = "SELECT * FROM GameDB_game"
df_db = pd.read_sql_query(query, conn)

print(df_db.columns)

df_csv = pd.read_csv('GameDB/static/data/data.csv')
print(df_csv.columns)

# Change the field name of CSV to the field name of DB
df_csv.rename(columns={'Name of Game': 'gameTitle', 'Release Date': 'releaseDate', 'Platforms Available': 'platform',
                       'Developer': 'developer', 'Publisher': 'publisher', 'Average Rating': 'avgRating',
                       'Age Restriction': 'ageRating', 'Multiplayer (True/False)': 'multiplayer',
                       'Average Completion Time': 'avgCompTime',
                       'Trailer Link': 'videoName', 'Image Link': 'pictureName', 'Description': 'description'}, inplace=True)

df_csv.drop(columns=['Category', 'Price'], inplace=True)  # delete columns 'Category', 'Price'
df_csv['multiplayer'] = df_csv['multiplayer'].astype(bool)


def process_url(s):
    # Convert the video URL to a URL that can be embedded with iframe tags.
    video_id = s.split('=')[1]
    return 'https://www.youtube.com/embed/' + video_id

df_csv['videoName'] = df_csv['videoName'].apply(process_url)

# Write to database
df_csv.to_sql('GameDB_game', conn, if_exists='append', index=False)

conn.close()

    

