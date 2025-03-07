import mysql.connector
import psycopg2
import pymongo
import sqlite3

class Database:
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    def connect(self):
        raise NotImplementedError("Subclasses must implement this method")

    def validate_connection(self):
        try:
            self.connect()
            return True
        except Exception as e:
            print(f"Connection validation failed: {e}")
            return False

class MySQLDatabase(Database):
    def connect(self):
        return mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            database=self.database
        )

class PostgreSQLDatabase(Database):
    def connect(self):
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            dbname=self.database
        )

class MongoDBDatabase(Database):
    def connect(self):
        return pymongo.MongoClient(
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password
        )[self.database]

class SQLiteDatabase(Database):
    def connect(self):
        return sqlite3.connect(self.database)
