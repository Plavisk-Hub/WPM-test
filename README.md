THIS IS A TERMINAL BASED TYPING TEST

 Features;

	- Random Selected Categories based on percentage
	
	- Shows you how many times you have scored one of the categories correctly ( inside 'config.json' )
	
	- Decent User Experience powered by Rich


 Installing Dependencies;

	```bash
	py -m pip install rich
	```
	
 Running the game
	
	```bash
	py main.py
	```


Configurations
 the configuration file is 'config.json'

| Key               | Description                                                |
| :---------------: | :--------------------------------------------------------: |
| `weight`          | Change the % chance of a category appearing (e.g., "10%"). |
| `Base Multiplier` | Increase this to give more coins per win.                  |
| `Counter`         | Change the length of the pre-game countdown.               |
