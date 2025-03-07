import os
import json

class Config:
    def __init__(self):
        self.host = None
        self.port = None
        self.username = None
        self.password = None
        self.database = None
        self.backup_type = None
        self.storage_option = None
        self.slack_webhook_url = None

    def load_from_file(self, file_path):
        with open(file_path, 'r') as file:
            config_data = json.load(file)
            self._load_config_data(config_data)

    def load_from_env(self):
        config_data = {
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT'),
            'username': os.getenv('DB_USERNAME'),
            'password': os.getenv('DB_PASSWORD'),
            'database': os.getenv('DB_NAME'),
            'backup_type': os.getenv('BACKUP_TYPE'),
            'storage_option': os.getenv('STORAGE_OPTION'),
            'slack_webhook_url': os.getenv('SLACK_WEBHOOK_URL')
        }
        self._load_config_data(config_data)

    def _load_config_data(self, config_data):
        self.host = config_data.get('host')
        self.port = config_data.get('port')
        self.username = config_data.get('username')
        self.password = config_data.get('password')
        self.database = config_data.get('database')
        self.backup_type = config_data.get('backup_type')
        self.storage_option = config_data.get('storage_option')
        self.slack_webhook_url = config_data.get('slack_webhook_url')

def load_config():
    config = Config()
    config_file_path = os.getenv('CONFIG_FILE_PATH', 'config.json')
    if os.path.exists(config_file_path):
        config.load_from_file(config_file_path)
    else:
        config.load_from_env()
    return config
