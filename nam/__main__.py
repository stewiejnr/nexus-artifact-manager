# __main__.py

from configparser import ConfigParser
from importlib import resources # Python 3.7+
import sys

from nam import upload
from nam import download

def main():
    cfg = ConfigParser()
    cfg.read_string(resources.read_text("reader", "config.txt"))
    url = cfg.get("feed", "url")

    if true:
        upload.mvn()

    else:
        download.mvn()

if __name__ == "__main__":
    main()
