import random
import requests
import math
url = "https://api.scryfall.com/cards/search"
Cards_In_Page = 175


#Define Functions:
#Ask for mana value (Validate that mana value is valid)
def Get_Mana_Value_X():
    while True:
        
        try:
            Mana_Value = int(input("\nEnter chosen mana value X (X can't be 0!): "))
            return Mana_Value
        
        except ValueError:
            print("Please enter a whole number.")

#Use user input to create query and find total number of cards
def Construct_List_Query(url, Mana_Value_X):
    params = {
        "q": f"-is:funny is:firstprinting type:creature game:paper mv:{Mana_Value_X} -t:land"
    }

    headers = {
        "User-Agent": "Momir-Vig-App/0.1"
    }
    
    Response = requests.get(url, params=params, headers=headers)
    Cards_List = Response.json()

    #print("Status:", Response.status_code)
    print("Total Cards:", Cards_List["total_cards"])
    return Cards_List["total_cards"]

#Using total number of cards, choose a random number creature
def Choose_Random_Creature(Total_Cards):
    Chosen_Card = random.randint(1, Total_Cards)
    return Chosen_Card

#Find page with creature
def Find_Page(Chosen_Card):
    
    Page = math.ceil(Chosen_Card/Cards_In_Page)
    Position = ((Chosen_Card - 1) % Cards_In_Page) +1

    return Page, Position

#Get data of chosen creature
def Get_Creature_Data(url, Mana_Value_X, Page, Position):
    params = {
        "q": f"-is:funny is:firstprinting type:creature game:paper mv:{Mana_Value_X} -t:land",
        "page": Page
    }

    headers = {
        "User-Agent": "Momir-Vig-App/0.1"
    }

    Response = requests.get(url, params=params, headers=headers)
    Cards_List = Response.json()

    Selected_Creature_Data = Cards_List["data"][Position - 1]

    return Selected_Creature_Data

#Display creature data
def Display_Creature_Data(Selected_Creature_Data):
    print("")
    print(Selected_Creature_Data["name"])
    print(Selected_Creature_Data["mana_cost"])
    print(Selected_Creature_Data["type_line"])
    print(Selected_Creature_Data["oracle_text"])

# #API Error handler
# def API_Error_Handler():


def main():
    Continue_Play = "Y"

    print("Welcome to Seth's Momir Vig App")

    while Continue_Play == "Y" or Continue_Play == "y":
        User_Input = Get_Mana_Value_X()
        Total_Cards = Construct_List_Query(url, User_Input)
        Chosen_Card = Choose_Random_Creature(Total_Cards)
        #print(Chosen_Card)
        Page, Position = Find_Page(Chosen_Card)
        #print("Page:", Page)
        #print("Position:", Position)
        Selected_Creature_Data = Get_Creature_Data(url, User_Input, Page, Position)
        Display_Creature_Data(Selected_Creature_Data)
        Continue_Play = input("\nRequest another creature? (Y/N): ")
        print("\n")

    print("Thank you for using Seth's Momir Vig App!")


main()