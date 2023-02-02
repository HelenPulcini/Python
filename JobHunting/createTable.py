from connect import *

# cursor.execute('CREATE TABLE "jobs"("jobID" INTEGER NOT NULL UNIQUE,"dateApplied" INTEGER,"companyName" TEXT,"location" TEXT,"position" TEXT,"salary" INTEGER,"contact" TEXT,PRIMARY KEY("jobID" AUTOINCREMENT))')

# cursor.execute('CREATE TABLE "user"(  "userID" INTEGER NOT NULL UNIQUE)')
cursor.execute('DROP TABLE "sqlite_sequence"')
