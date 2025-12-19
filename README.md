# hangman

A classic CLI hangman game that fetches data from online through webscraping.



## Python Files

1. main.py

```
MAIN_FUNCTION():
	Run hangman game <- Hangman.RUN_GAME()
```

2. fetcher.py

```
class Fetcher:
	-- variables --
	saved_words_filepath <- saved words csv file
	merriam_webster_base_url <- base url of merriam webster
	word_of_the_day_url <- full url for the word of the day website
    definition_url <- full url for the definition
    
    is_online_mode <- True
   	
   	-- function --
   	[1] GET_WORD_AND_DEF(online_mode = True):
   		is_online_mode = online_mode
   		
   	 	word = GET_WORD()
   	 	definition = GET_DEFINITION(word)
   	 	
   	 	return word, definition, is_online_mode
   	
   	[2] GET_WORD():
   	
        IF is_online_mode:
            Try to fetch words from webscraper
            Save the 100 most recent words in Saved Words CSV (word, date, definition)
            Delete the words that are past 100 days old
			Get random word

            IF no connection:
                is_online_mode = False
 
        IF Saved Words CSV Exists:
        	If there are words with definition:
            	Get random word with definition
			Else:
            	Get random word
                 
		return word
		
     [3] GET_DEFINITION(word):
   		
   		Get definition from saved_csv
   		If no definition:
   			Scrape for web
   			
   		return definition

   	 	
```

3. hangman.py		

	class Hangman:
		-- variables --
		score <- 0
		losses <- 0
		attempts <- 0
		level <- 0
	
	    base_score_per_letter <- 30
	    base_bonus_score <- 10
	
	    is_online_mode <- False
	
	    current_word <- None
	    current_definition <- None
	
	    fetcher <- object of class Fetcher
	
	    -- constructor --
	    HANGMAN():
	        Get current_word and current_definition and is_online_mode <- fetcher.GET_WORD()
	
	    -- functions --
	
	    [1] RUN_GAME():
	
	        WHILE game is not lost:
	            Get word and definition <-- GET_WORD(is_online_mode)
	            score = Play current level <-- PLAY_LEVEL(word, definition, level)
	
	    [2] PLAY_LEVEL(word, definition):
	
	        mistakes <- 0
	
	        WHILE game not won or lost:
	            Display hangman image <-- DISPLAY HANGMAN(mistakes)
	            Display definition
	            Display currently guessed word
	            Ask user input
	            Display if correct
	
	            return CALCULATED_SCORE(level, no_of_correct_guesses, no_of_mistakes)
	
	    [3] DISPLAY_HANGMAN(mistakes):
	
	        Show hangman CLI visual based on no of mistakes
	
	    [4] CALCULATED_SCORE(level, no_of_correct_guesses, no_of_mistakes):
	        score = (no_of_correct_guesses * base_score_per_letter)
	        score -= (no_of_mistakes * base_score_per_letter)
	
	        if level won:
	            bonus = level * base_bonus_score
	
	        return score + bonus





## File Structure

```
hangman/
│
├── pyproject.toml        # packaging, dependencies
├── README.md
├── .gitignore
│
├── data/
│   └── saved_words.csv   # cached words & definitions
│
├── src/
│   └── hangman/
│       ├── __init__.py
│       │
│       ├── main.py       # CLI entry point
│       │
│       ├── game/
│       │   ├── __init__.py
│       │   ├── hangman.py
│       │   └── scoring.py
│       │
│       ├── data/
│       │   ├── __init__.py
│       │   ├── fetcher.py
│       │   ├── scraper.py
│       │   └── storage.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   └── word.py
│       │
│       ├── ui/
│       │   ├── __init__.py
│       │   └── cli.py
│       │
│       └── config.py
│
└── tests/
    ├── test_fetcher.py
    ├── test_hangman.py
    └── test_scoring.py

```