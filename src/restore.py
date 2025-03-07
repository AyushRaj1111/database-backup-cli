import os
import shutil
import tarfile
import datetime
from database import MySQLDatabase, PostgreSQLDatabase, MongoDBDatabase, SQLiteDatabase

def perform_restore(db, backup_file, tables=None):
    if not db.validate_connection():
        print("Database connection failed. Restore aborted.")
        return

    if not os.path.exists(backup_file):
        print("Backup file not found. Restore aborted.")
        return

    if isinstance(db, MySQLDatabase):
        restore_mysql(db, backup_file, tables)
    elif isinstance(db, PostgreSQLDatabase):
        restore_postgresql(db, backup_file, tables)
    elif isinstance(db, MongoDBDatabase):
        restore_mongodb(db, backup_file, tables)
    elif isinstance(db, SQLiteDatabase):
        restore_sqlite(db, backup_file, tables)
    else:
        print("Unsupported database type")
        return

def restore_mysql(db, backup_file, tables):
    command = f"mysql -h {db.host} -P {db.port} -u {db.username} -p{db.password} {db.database} < {backup_file}"
    os.system(command)

def restore_postgresql(db, backup_file, tables):
    command = f"pg_restore -h {db.host} -p {db.port} -U {db.username} -d {db.database} -v {backup_file}"
    os.system(command)

def restore_mongodb(db, backup_file, tables):
    command = f"mongorestore --host {db.host} --port {db.port} --username {db.username} --password {db.password} --db {db.database} {backup_file}"
    os.system(command)

def restore_sqlite(db, backup_file, tables):
    shutil.copyfile(backup_file, db.database)
