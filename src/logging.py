import logging
import os
import requests
from datetime import datetime

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "backup.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_backup_activity(start_time, end_time, status, time_taken, error=None):
    logging.info(f"Backup started at: {start_time}")
    logging.info(f"Backup ended at: {end_time}")
    logging.info(f"Backup status: {status}")
    logging.info(f"Time taken: {time_taken} seconds")
    if error:
        logging.error(f"Error encountered: {error}")

def send_slack_notification(message, webhook_url):
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        logging.error(f"Failed to send Slack notification: {response.text}")

def setup_logging():
    logging.info("Logging setup complete")
