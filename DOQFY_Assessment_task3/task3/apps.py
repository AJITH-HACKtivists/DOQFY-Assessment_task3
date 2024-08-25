from django.apps import AppConfig
import threading
from .scapper import scrape_data
import time


class Task3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task3'
    def ready(self):
        thread = threading.Thread(target=start_scraping)
        thread.daemon = True
        thread.start()

def start_scraping():
    """Function to run the scraping task in a loop."""
    while True:
        scrape_data()
        time.sleep(300)
    
