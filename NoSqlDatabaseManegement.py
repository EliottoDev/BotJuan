import os
import json

class Database:

    def __init__(self, database: str):
        self.dbase = database
        self.data = json.load(database)
