import random
import requests

#Define Functions:
#Ask for mana value (Validate that mana value is valid)
def Get_Mana_Value_X():
    while True:
        
        try:
            Mana_Value = int(input("Enter chosen mana value X: "))
            return Mana_Value
        
        except ValueError:
            print("Please enter a whole number.")

#Use user input to create query
def Construct_Query():

#Request query on scryfall search
def Request_List():

#Using total number of cards, choose a random number creature
def Choose_Random_Creature():

#Find page with creature
def Find_Page():

#Get data of chosen creature
def Get_Creature_Data():

#Display creature data
def Display_Creature_Data():

#API Error handler
def API_Error_Handler():
