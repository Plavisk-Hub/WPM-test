import time
import random
import json
from rich.console import Console
from rich.traceback import install 
r = Console()
install()


with open('config.json', 'r') as f:
    data = json.load(f)

def load_settings():
    with open('config.json', 'r') as f:
        return json.load(f)

def save_settings(data):
    with open('config.json', 'w') as f:
        json.dump(data, f, indent=4)


import random

lives = 3
print("""
Typing the word in ANY casing works I.E.:
Word, wOrD, WORD
they're all acceptable.
""")
input("Press enter to start.")
    
    
    
# picking a list and word    
names = list(data["Categories"].keys())
weights = [int(data["Categories"][n]["weight"].strip('%')) for n in names]
list_pick = random.choices(names, weights=weights)[0]
words_list = data["Categories"][list_pick]["words"]
word_pick = random.choice(words_list)


# starting the game
r.print(f"""
you word is [red]{word_pick.capitalize()}[/]
""")
counter = int(data["Stats"]["Counter"])
for i in range(3
):
    counter -= 1
    print(f"""\r{counter}s remaining till the game starts.""", end="", flush=True)
    time.sleep(1)
    
r.print("""
\r[green]GO![/]""")




# user input
start = time.time()
user = r.input(f"""
    [red]{word_pick.capitalize()}
""")
end = time.time()

# result
if user.lower() == word_pick.lower():
    duration = end - start
    WPM = (len(word_pick) / 5) / (max(duration, 0.1) / 60)
    raw_score = len(word_pick) / max(duration, 0.1)
    base_multiplier = data["Stats"]["Base Multiplier"]
    final_coin_rate = round(base_multiplier * raw_score)
    
    r.print("you [#FFD700]WON[/]!!!")
    print(f"""
    Stats:
        Duration: {duration:.1f}s
        Words Per Minute = {WPM:.3}
        Category: {list_pick}
        Coins earned: {final_coin_rate}
    """)
    
    data["Stats"]["Coins"] += final_coin_rate
    data["Categories"][list_pick]["level"] += 1
    save_settings(data)
    
else:
    r.print("you [red]lost[/]...")
