import random
import requests
import math
url = "https://api.scryfall.com/cards/search"
Cards_In_Page = 175

def Build_Params(Mana_Value_X, Page=None):
    params = {
        "q": rf"game:paper -is:funny type:/^[^\/]*creature/ -t:land mv:{Mana_Value_X}",
        "unique": "cards",
        "order": "name",
    }
    if Page is not None:
        params["page"] = Page
    return params

#Use user input to create query and find total number of cards
def Construct_List_Query(url, Mana_Value_X):
    params = Build_Params(Mana_Value_X)

    headers = {
        "User-Agent": "Momir-Vig-App/0.1",
        "Accept": "application/json"
    }
    
    Response = requests.get(url, params=params, headers=headers)

    if Response.status_code != 200:
        #print("No creatures found for that mana value.")
        return 0

    Cards_List = Response.json()

    #print("Status:", Response.status_code)
    #print("Total Cards:", Cards_List["total_cards"])
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

    if Response.status_code != 200:
        #print("Could not retrieve the creature.")
        return None

    Cards_List = Response.json()

    Selected_Creature_Data = Cards_List["data"][Position - 1]

    return Selected_Creature_Data


#{Display_Face and Display_Creature_Data functions are replaced in website code with Format_Creature_Data}


def format_Creature_Data(Selected_Creature_Data):
    face = Selected_Creature_Data["card_faces"][0] if "card_faces" in Selected_Creature_Data else Selected_Creature_Data
    images = Selected_Creature_Data.get("image_uris") or face.get("image_uris", {})
    return {
        "name": face.get("name", ""),
        "mana_cost": face.get("mana_cost", ""),
        "type_line": face.get("type_line", ""),
        "oracle_text": face.get("oracle_text", ""),
        "power": face.get("power"),
        "toughness": face.get("toughness"),
        "image": images.get("normal")
    }

# #API Error handler
# def API_Error_Handler():


#{main function no longer used because no more console use. Also no more direct user connection to program.}



#Function that can be called by website to get random creature data.
def Get_Random_Creature(Mana_Value_X):
    Total_Cards = Construct_List_Query(url, Mana_Value_X)
    if Total_Cards == 0:
        return None
    Chosen_Card = Choose_Random_Creature(Total_Cards)
    Page, Position = Find_Page(Chosen_Card)
    Data = Get_Creature_Data(url, Mana_Value_X, Page, Position)
    return format_Creature_Data(Data) if Data else None