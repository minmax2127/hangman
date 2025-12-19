from hangman.data.fetcher import Fetch
from hangman.data.scraper import WebScraper

def main():
    scraper = WebScraper()
    print(scraper.get_words(10))
    '''
    storage = WordStorage("data/saved_words.csv")
    scraper = WebScraper()
    fetcher = Fetcher(storage, scraper)
    ui = CliRenderer()

    game = Hangman(fetcher, ui)
    game.run()
    '''

if __name__ == "__main__":
    main()