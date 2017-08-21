from os.path import join, dirname
from dotenv import load_dotenv
import logging
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
