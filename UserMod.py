
#this class will allow the user to modify the database. We will create the cellular message class
#laterthat will utilize the methods in this class to modify the database as done by the user
class UserMod:
    def __init__(self, cursor):
        self.cursor = cursor
    def adduser(self, name):
        stmt = " INSERT chores.roomates(name) " \
               " VALUES(" + name + ") "
        self.cursor.execute(stmt)
    def deleteuser(self, name):
        stmt = "DELETE FROM  chores.roomates " \
               " WHERE name = " + name
        self.cursor.execute(stmt)