
from page_object import all_file, zip_file, resources, downloads_file
import zipfile
import pytest
import os


@pytest.fixture
def test_zip_create():
    if not os.path.exists(resources):
        os.mkdir(resources)
    with zipfile.ZipFile(zip_file, mode='w', compression=zipfile.ZIP_DEFLATED) as file_z:
        for file_name in all_file:
            create_file = os.path.join(downloads_file, file_name)
            file_z.write(create_file, os.path.basename(create_file))
