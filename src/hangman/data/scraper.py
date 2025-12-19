import requests
from pathlib import Path
from bs4 import BeautifulSoup
import hangman.config as c
from datetime import datetime, date

from hangman.models.word import WordEntry

class WebScraper:
    def __init__(self):
        # self.word_of_the_day = self.get_word_of_the_day()
        self.last_100_words = []
    
    def get_words(self, no_of_words = 100):
        try:
            request = requests.get(c.CALENDAR_OF_WORDS_URL, timeout = 10)
            content = request.content
            soup = BeautifulSoup(content, "html.parser")
            print("soup taken!")
            try:
                word_containers = soup.find_all("div", class_="more-words-of-day-container")
                for container in word_containers:
                    words_tag = container.find_all("a")
                    print(words_tag)
            except Exception:
                print("Error occurred!")
            except requests.exceptions.Timeout as e:
                print(f"Request timed out: {e}")

        except ConnectionError:
            print("Network connection error!")