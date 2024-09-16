from pathlib import Path
from util import read_json


class Constants:

    config = read_json(Path("script/config.json"))
    pages_dir = Path("db/page")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://www.google.com/'
    }
    invalid_img_src: set[str] = {
        "https://cdn.mangadistrict.com/assets/publication/media/image/001.jpg"
    }

    @staticmethod
    def root() -> Path:
        return Path(Constants.config["root-dir"])