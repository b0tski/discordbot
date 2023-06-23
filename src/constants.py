import os 
import json

BOT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(BOT_DIR, os.pardir))

# Opening config file
config_path = os.path.join(PROJECT_ROOT, "config.json")
with open(config_path, "r") as f:
    data = json.load(f)