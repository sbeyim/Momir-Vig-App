import random
import requests
url = "https://api.scryfall.com/cards/search"


#Define Functions:
#Ask for mana value (Validate that mana value is valid)
def Get_Mana_Value_X():
    while True:
        
        try:
            Mana_Value = int(input("Enter chosen mana value X: "))
            return Mana_Value
        
        except ValueError:
            print("Please enter a whole number.")

#Use user input to create query and find total number of cards
def Construct_List_Query(url, Mana_Value_X):
    params = {
        "q": f"is:firstprinting type:creature game:paper mv:{Mana_Value_X}"
    }

    headers = {
        "User-Agent": "Momir-Vig-App/0.1"
    }
    
    Response = requests.get(url, params=params, headers=headers)
    Cards_List = Response.json()

    return Cards_List["total_cards"]

# #Using total number of cards, choose a random number creature
# def Choose_Random_Creature():

# #Find page with creature
# def Find_Page():

# #Get data of chosen creature
# def Get_Creature_Data():

# #Display creature data
# def Display_Creature_Data():

# #API Error handler
# def API_Error_Handler():


def main():
    User-Input = Get_Mana_Value_X
    Total-Cards = Construct_List_Query(url, User-Input)
    