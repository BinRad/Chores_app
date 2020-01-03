import mysql.connector

class Main:
    def __init__(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="abcdefg"
        )
        self.cursor = mydb.cursor()
        print('Seems like everything is working properly!')
        self.DeleteDB()
        self.CreateTables()

    def DeleteDB(self):
        self.cursor.execute("DROP DATABASE 'chores'")
        return

    def CreateTables(self):
        self.cursor.execute("CREATE DATABASE chores")
        self.cursor.execute("CREATE TABLE `chores`.`roomates` ("
                            "`name` VARCHAR(255) NOT NULL,"
                            "PRIMARY KEY (`name`),"
                            "UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE) ")
        self.cursor.execute("CREATE TABLE `chores`.`tasks` ( "
                            "`task` VARCHAR(255) NOT NULL,"
                            "`frequency` VARCHAR(255) NULL,"
                            "`catgory` VARCHAR(255) NULL,"
                            "PRIMARY KEY (`task`),"
                            "UNIQUE INDEX `name_UNIQUE` (`task` ASC) VISIBLE) ")
        return