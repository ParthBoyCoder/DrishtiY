from zipfile import ZipFile
from urllib.request import urlretrieve
import os

def download_and_unzip(url, save_path):
    print(f"Downloading and extracting assests....", end="")

    # Downloading zip file using urllib package.
    urlretrieve(url, save_path)

    try:
        # Extracting zip file using the zipfile package.
        with ZipFile(save_path) as z:
            # Extract ZIP file contents in the same directory.
            z.extractall(os.path.split(save_path)[0])

        print("Done")

    except Exception as e:
        print("\nInvalid file.", e)

# The 'r' before the string handles backslashes, and dl=1 forces the download.
URL = r"https://www.dropbox.com/scl/fi/9wtqc2hrvzjw087s7x5pr/files.zip?rlkey=i7ywp0o3t2b2ejaar1lf0aubt&st=n3rhku7x&dl=1"

asset_zip_path = os.path.join(os.getcwd(), "files.zip") # Corrected path to include .zip extension

# Download if assest ZIP does not exists.
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)