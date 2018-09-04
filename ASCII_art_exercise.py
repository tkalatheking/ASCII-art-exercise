from pyfiglet import figlet_format
from termcolor import colored



while True:
	user_messege = input("What massage you wanna print?: ")
	user_color = input("What color?: ")
	user_messege_text = figlet_format(user_messege, font='standard')
	if user_color == "red":
		print(colored(user_messege_text, color = "red", attrs = ["blink"]))
		break
	elif user_color == "blue":
		print(colored(user_messege_text, color = "blue", attrs = ["blink"]))
		break
	elif user_color == "magenta":
		print(colored(user_messege_text, color = "magenta", attrs = ["blink"]))
		break
	elif user_color == "cyan":
		print(colored(user_messege_text, color = "cyan", attrs = ["blink"]))
		break
	elif user_color == "yellow":
		print(colored(user_messege_text, color = "yellow", attrs = ["blink"]))
		break
	else:
		print("Try Again")
	








