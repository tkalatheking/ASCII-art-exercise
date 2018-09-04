from pyfiglet import figlet_format
from termcolor import colored


valid_colors = ( "red", "green", "yellow", "blue", "magenta", "cyan", "white")

user_messege = input("What massage you wanna print?: ")
user_color = input("What color?: ")

if user_color not in valid_colors:
	user_color = "cyan"

user_messege_text = figlet_format(user_messege)
print(colored(user_messege_text, color = user_color, attrs = ["blink"]))









