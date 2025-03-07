import os
import shutil
import tarfile
import datetime
from database import MySQLDatabase, PostgreSQLDatabase, MongoDBDatabase, SQLiteDatabase

def perform_backup(db, backup_type):
    if not db.validate_connection():
        print("Database connection failed. Backup aborted.")
        return

    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file = os.path.join(backup_dir, f"{db.database}_{backup_type}_{timestamp}.sql")

    if isinstance(db, MySQLDatabase):
        backup_mysql(db, backup_file, backup_type)
    elif isinstance(db, PostgreSQLDatabase):
        backup_postgresql(db, backup_file, backup_type)
    elif isinstance(db, MongoDBDatabase):
        backup_mongodb(db, backup_file, backup_type)
    elif isinstance(db, SQLiteDatabase):
        backup_sqlite(db, backup_file, backup_type)
    else:
        print("Unsupported database type")
        return

    compress_backup(backup_file)
    store_backup(backup_file)

def backup_mysql(db, backup_file, backup_type):
    command = f"mysqldump -h {db.host} -P {db.port} -u {db.username} -p{db.password} {db.database} > {backup_file}"
    os.system(command)

def backup_postgresql(db, backup_file, backup_type):
    command = f"pg_dump -h {db.host} -p {db.port} -U {db.username} -F c -b -v -f {backup_file} {db.database}"
    os.system(command)

def backup_mongodb(db, backup_file, backup_type):
    command = f"mongodump --host {db.host} --port {db.port} --username {db.username} --password {db.password} --db {db.database} --out {backup_file}"
    os.system(command)

def backup_sqlite(db, backup_file, backup_type):
    shutil.copyfile(db.database, backup_file)

def compress_backup(backup_file):
    compressed_file = f"{backup_file}.tar.gz"
    with tarfile.open(compressed_file, "w:gz") as tar:
        tar.add(backup_file, arcname=os.path.basename(backup_file))
    os.remove(backup_file)

def store_backup(backup_file):
    # Placeholder for storing backup files locally or on cloud storage services
    pass
