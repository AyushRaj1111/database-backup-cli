import argparse
import sys
from database import MySQLDatabase, PostgreSQLDatabase, MongoDBDatabase, SQLiteDatabase
from backup import perform_backup
from restore import perform_restore
from config import load_config
from logging import setup_logging

def main():
    parser = argparse.ArgumentParser(description="Database Backup CLI Utility")
    subparsers = parser.add_subparsers(dest="command")

    # Backup command
    backup_parser = subparsers.add_parser("backup", help="Perform a database backup")
    backup_parser.add_argument("--type", required=True, choices=["full", "incremental", "differential"], help="Type of backup")
    backup_parser.add_argument("--db", required=True, choices=["mysql", "postgresql", "mongodb", "sqlite"], help="Database type")
    backup_parser.add_argument("--host", required=True, help="Database host")
    backup_parser.add_argument("--port", required=True, type=int, help="Database port")
    backup_parser.add_argument("--username", required=True, help="Database username")
    backup_parser.add_argument("--password", required=True, help="Database password")
    backup_parser.add_argument("--database", required=True, help="Database name")

    # Restore command
    restore_parser = subparsers.add_parser("restore", help="Restore a database from a backup file")
    restore_parser.add_argument("--db", required=True, choices=["mysql", "postgresql", "mongodb", "sqlite"], help="Database type")
    restore_parser.add_argument("--host", required=True, help="Database host")
    restore_parser.add_argument("--port", required=True, type=int, help="Database port")
    restore_parser.add_argument("--username", required=True, help="Database username")
    restore_parser.add_argument("--password", required=True, help="Database password")
    restore_parser.add_argument("--database", required=True, help="Database name")
    restore_parser.add_argument("--backup-file", required=True, help="Path to the backup file")
    restore_parser.add_argument("--tables", help="Comma-separated list of tables to restore (optional)")

    args = parser.parse_args()

    # Load configuration
    config = load_config()

    # Setup logging
    setup_logging()

    # Handle backup command
    if args.command == "backup":
        if args.db == "mysql":
            db = MySQLDatabase(args.host, args.port, args.username, args.password, args.database)
        elif args.db == "postgresql":
            db = PostgreSQLDatabase(args.host, args.port, args.username, args.password, args.database)
        elif args.db == "mongodb":
            db = MongoDBDatabase(args.host, args.port, args.username, args.password, args.database)
        elif args.db == "sqlite":
            db = SQLiteDatabase(args.host, args.port, args.username, args.password, args.database)
        else:
            print("Unsupported database type")
            sys.exit(1)

        perform_backup(db, args.type)

    # Handle restore command
    elif args.command == "restore":
        if args.db == "mysql":
            db = MySQLDatabase(args.host, args.port, args.username, args.password, args.database)
        elif args.db == "postgresql":
            db = PostgreSQLDatabase(args.host, args.port, args.username, args.password, args.database)
        elif args.db == "mongodb":
            db = MongoDBDatabase(args.host, args.port, args.username, args.password, args.database)
        elif args.db == "sqlite":
            db = SQLiteDatabase(args.host, args.port, args.username, args.password, args.database)
        else:
            print("Unsupported database type")
            sys.exit(1)

        perform_restore(db, args.backup_file, args.tables)

    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
