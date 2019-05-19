#script by Wealy Cassano
#script on python2.7

import rcon_mc.rcon
import rcon_mc.lib.msocket
from types import *

developer = "Wealy Cassano"
site = "http://wealy.pw"
vk = "https://vk.cc/8W177v"
date_first_version = "01/18/2019"
version = "1.2"
###
def about():
	print("Script Developer: " + developer)
	print("Link to my personal site: " + site)
	print("Link to my VK page: " + vk)
	print("\nDate of the first version of the script: " + date_first_version)
	print("Script Version: " + version)
###

###
def lavatech(command):
	client=rcon_mc.rcon.client("ip", 2212, "pass")
	response = client.send(command)
	print("\n" + response)
def lavadupe(command):
	client=rcon_mc.rcon.client("ip", 1121, "pass")
	response = client.send(command)
	print("\n" + response)
def lavalite(command):
	client=rcon_mc.rcon.client("ip", 1123, "pass")
	response = client.send(command)
	print("\n" + response)
###

def main():
	print("\n\n!!!!! ATTENTION: SCRIPT SUPPORTS ONLY ENGLISH RATING !!!!!\n\n")
	linexaxa = input("Select from the list item: \n\n[1] - RCON Control Server\n[2] - About script\n[3] - Exit from the program\n\nSelect: ")
	if linexaxa == 1:
		lineone = input("Select a server from the list \n\n[1] - LavaTech\n[2] - LavaDupe\n[3] - LavaLite\n\nSelect server: ")
		if lineone == 1:
			print("You selected LavaTech server!")
			print("To go back (to server selection), type 'quit' on the command line.")
			while 2 > 1:
				linetwo = raw_input("Enter the command (without /): ")
				if linetwo == "quit":
					main()
				else:
					lavatech(linetwo)
		elif lineone == 2:
			print("You selected LavaDupe server!")
			print("To go back (to server selection), type 'quit' on the command line.")
			while 2 > 1:
				linetwo = raw_input("Enter the command (without /): ")
				if linetwo == "quit":
					main()
				else:
					lavadupe(linetwo)
		elif lineone == 3:
			print("You selected LavaLite server!")
			print("To go back (to server selection), type 'quit' on the command line.")
			while 2 > 1:
				linetwo = raw_input("Enter the command (without /): ")
				if linetwo == "quit":
					main()
				else:
					lavalite(linetwo)
		else:
			print("You must select one of the suggested servers!")
	elif linexaxa == 2:
		about()
		while 2 > 1:
			linethree = raw_input("\nCommand Line: ")
			if linethree == "quit":
				main()
			elif linethree == "help":
				print("\n")
				print("----------------[ HELP PAGE ]----------------")
				print("\n")
				print("1. Command 'quit' - return to the main menu (without quotes)")
				print("\n")
				print("---------------------------------------------")
			else:
				print("Command '" + linethree + "' not found! Use 'help'")
	elif linexaxa == 3:
		print("You have successfully quit the program!")
	else:
		print("Select an item from the list!")

main()