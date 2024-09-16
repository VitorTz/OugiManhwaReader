from selenium.webdriver import Firefox, FirefoxOptions
from constants import Constants
from manhwa import Manhwa
from bs4 import BeautifulSoup
from source import Source


class Scrapper:

    def __init__(self) -> None:
        print("Starting Firefox driver")
        self.__options = FirefoxOptions()
        self.__options.add_argument("--headless")
        self.__driver = Firefox(self.__options)
        print("Firefox driver loaded")
    
    def add_to_images(self, images: list[str], src: str) -> None:
        if src not in Constants.invalid_img_src:
            images.append(src)
    
    def get(self, link: str) -> BeautifulSoup:        
        path = Constants.pages_dir / link.replace("/", '-').replace(":", '')
        if path.exists():
            with open(path, "r") as file:
                return BeautifulSoup(file.read(), "lxml")
        self.__driver.get(link)
        with open(path, "w+") as file:
            file.write(self.__driver.page_source)
        return BeautifulSoup(self.__driver.page_source, "lxml")
    
    def get_images(self, manhwa: Manhwa, chapter: str) -> list[str]:
        page: BeautifulSoup = self.get(chapter)
        images: list[str] = []
        match manhwa.source:
            case Source.MangaDistrict:
                div = page.find("div", class_="reading-content")
                for img in div.find_all("img", class_="wp-manga-chapter-img"):
                    self.add_to_images(images, img["src"].strip())                    

        return images
