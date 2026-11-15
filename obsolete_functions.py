import random
import requests
import math

#Define Functions:
#Ask for mana value (Validate that mana value is valid)

#{Get_Mana_Value_X function is no longer needed for app. Just used when directly in console.}

# def Get_Mana_Value_X():
#     while True:
        
#         try:
#             Mana_Value = int(input("\nEnter chosen mana value X (X can't be 0!): "))
#             if Mana_Value < 1:
#                 print("Please enter a number greater than 0.")
#                 continue
#             return Mana_Value
        
#         except ValueError:
#             print("Please enter a whole number.")




#Display card face for MDFCs
# def Display_Face(face):
#     print(face.get("name", ""))
#     print(face.get("mana_cost", ""))
#     print(face.get("type_line", ""))
#     print(face.get("oracle_text", ""))
#     power = face.get("power")
#     toughness = face.get("toughness")
#     if power is not None and toughness is not None:
#         print(f"({power}/{toughness})")

# #Display creature data
# def Display_Creature_Data(Selected_Creature_Data):
#     print("")
#     if "card_faces" in Selected_Creature_Data:
#         for face in Selected_Creature_Data["card_faces"]:
#             Display_Face(face)
#             print("")
#             #print this face's name, mana_cost, etc.
#     else:
#         print(Selected_Creature_Data["name"])
#         print(Selected_Creature_Data["mana_cost"])
#         print(Selected_Creature_Data["type_line"])
#         print(Selected_Creature_Data["oracle_text"])
#         power = Selected_Creature_Data["power"]
#         toughness = Selected_Creature_Data["toughness"]
#         if power is not None and toughness is not None:
#             print(f"({power}/{toughness})")



# def main():
#     Continue_Play = "Y"

#     print("Welcome to Seth's Momir Vig App")

#     while Continue_Play == "Y" or Continue_Play == "y":
#         User_Input = Get_Mana_Value_X()
#         Total_Cards = Construct_List_Query(url, User_Input)
#         if Total_Cards == 0:
#             pass
#         else:
#             Chosen_Card = Choose_Random_Creature(Total_Cards)
#             #print(Chosen_Card)
#             Page, Position = Find_Page(Chosen_Card)
#             #print("Page:", Page)
#             #print("Position:", Position)
#             Selected_Creature_Data = Get_Creature_Data(url, User_Input, Page, Position)
#             Display_Creature_Data(Selected_Creature_Data)
        
#         Continue_Play = input("\nRequest another creature? (Y/N): ")
#         print("\n")

#     print("Thank you for using Seth's Momir Vig App!")