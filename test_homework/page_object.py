import os

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)


downloads_file = os.path.join(CURRENT_DIR, "downloads_file")
resources = os.path.join(CURRENT_DIR, 'resources')
all_file = os.listdir(downloads_file)
zip_file = os.path.join(resources, 'new.zip')

