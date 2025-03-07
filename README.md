# Database Backup CLI Utility

## Project Description

This project is a command-line interface (CLI) utility for backing up any type of database. The utility supports various database management systems (DBMS) such as MySQL, PostgreSQL, MongoDB, SQLite, and others. The tool features automatic backup scheduling, compression of backup files, storage options (local and cloud), and logging of backup activities.

## Features

- **Database Connectivity**:
  - Support for Multiple DBMS: MySQL, PostgreSQL, MongoDB, SQLite.
  - Connection Parameters: Specify database connection parameters like host, port, username, password, and database name.
  - Connection Testing: Validate credentials based on the database type before proceeding with backup operations.
  - Error Handling: Implement error handling for database connection failures.

- **Backup Operations**:
  - Backup Types: Support full, incremental, and differential backup types based on the database type and user preference.
  - Compression: Compress backup files to reduce storage space.

- **Storage Options**:
  - Local Storage: Store backup files locally on the system.
  - Cloud Storage: Store backup files on cloud storage services like AWS S3, Google Cloud Storage, or Azure Blob Storage.

- **Logging and Notifications**:
  - Logging: Log backup activities, including start time, end time, status, time taken, and any errors encountered.
  - Notifications: Optionally send Slack notifications on completion of backup operations.

- **Restore Operations**:
  - Restore Backup: Recover the database from a backup file.
  - Selective Restore: Provide options for selective restoration of specific tables or collections if supported by the DBMS.

## Installation

To install the CLI utility, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration

Configure the database connection parameters, backup options, and storage settings by editing the `config.py` file or setting environment variables.

## Usage

### Backup Operations

To perform a full backup of a MySQL database:
```sh
python src/main.py backup --type full --db mysql --host localhost --port 3306 --username root --password secret --database mydb
```

To perform an incremental backup of a PostgreSQL database:
```sh
python src/main.py backup --type incremental --db postgresql --host localhost --port 5432 --username postgres --password secret --database mydb
```

### Restore Operations

To restore a MySQL database from a backup file:
```sh
python src/main.py restore --db mysql --host localhost --port 3306 --username root --password secret --database mydb --backup-file path/to/backup/file
```

To selectively restore specific tables in a MongoDB database:
```sh
python src/main.py restore --db mongodb --host localhost --port 27017 --username admin --password secret --database mydb --backup-file path/to/backup/file --tables table1,table2
```

## Logging and Notifications

Backup activities are logged in the `logs` directory. Optionally, you can configure Slack notifications by setting the appropriate environment variables in the `config.py` file.

## Compatibility

The CLI utility is compatible with different operating systems, including Windows, Linux, and macOS.

## Documentation

Ensure the tool is well-documented and easy to use. Provide clear instructions for installation, configuration, and usage.

## Security

Ensure that the backup and restore operations are secure and reliable.

## Performance

Consider the performance implications of backup operations on the database server.

## Error Handling

Implement proper error handling and logging mechanisms to track backup activities.
