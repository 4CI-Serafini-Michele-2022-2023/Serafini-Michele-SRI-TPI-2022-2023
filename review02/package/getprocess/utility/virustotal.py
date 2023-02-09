"""
virustotal
"""
from pprint import pprint
import os
import virustotal_python
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def virustotal(path):
    """
    huibbhyu
    """
    file_path = path

    # Create dictionary containing the file to send for multipart encoding upload
    files = {"file": (os.path.basename(file_path), open(os.path.abspath(file_path), "rb"))}

    with virustotal_python.Virustotal(API_KEY) as vtotal:
        resp = vtotal.request("files", files=files, method="POST")
        pprint(resp.json())


if __name__ == "__main__":
    print("Dammi un percorso di un file .exe")
    virustotal(str(input()))
