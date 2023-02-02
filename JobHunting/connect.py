import sqlite3 as sql

connection = sql.connect("/home/helenpulcini/Python/JobHunting/jobs.db")

cursor = connection.cursor()
# cursor.execute('CREATE TABLE "jobs"(  "jobID" INTEGER NOT NULL UNIQUE)')