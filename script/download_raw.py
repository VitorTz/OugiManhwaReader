from constants import Constants
from pathlib import Path
from multiprocessing.pool import Pool
from manhwa import Manhwa
from source import Source
from scrapper import Scrapper
from time import sleep
from random import random
from PIL import Image
import sys
import requests


MANHWAS = {
    "Addicted to My Mom":  Manhwa("Addicted to My Mom", Source.MangaDistrict, "https://mangadistrict.com/read-scan/addicted-to-my-mom-official/"),
    "Eat First, Mom": Manhwa("Eat First, Mom", Source.MangaDistrict, "https://mangadistrict.com/read-scan/eat-first-mom-official/")
}



def download_image(image: tuple[str, Path]) -> None:
    if image[1].exists():
        return
    sleep(random())
    print(f"[DOWNLOADING IMAGE -> {image[1]}]")
    r = requests.get(image[0], stream=True, timeout=10, headers=Constants.headers)
    with open(image[1], 'wb') as file:
        for chunck in r.iter_content(1024):
            file.write(chunck)
    img = Image.open(image[1])
    img = img.convert("RGB")
    img.save(image[1])
    print(f"[IMAGE DOWNLOADED -> {image[1]}]")


def main() -> None:
    chapter_num: int = int(sys.argv[1])
    
    scrapper = Scrapper()
    manhwa: Manhwa = MANHWAS["Addicted to My Mom"]
    manhwa.path.mkdir(exist_ok=True, parents=True)
    raw_path = manhwa.path / "raw"
    raw_path.mkdir(exist_ok=True)
    pt_path = manhwa.path / "pt-br"
    pt_path.mkdir(exist_ok=True)
    eng_path = manhwa.path / "en-us"
    eng_path.mkdir(exist_ok=True)
    
    chapter: str = f"{manhwa.link}chapter-{chapter_num}"
    chapter_path = eng_path / f"{chapter_num}"
    chapter_path.mkdir(exist_ok=True)    
    
    images: list[str] = scrapper.get_images(manhwa, chapter)
    images: list[str, Path] = [(p, chapter_path / f"{i}.png") for i, p in enumerate(images)]    
    with Pool(4) as pool:
        pool.map(download_image, images)
    pool.join()


if __name__ == "__main__":
    main()