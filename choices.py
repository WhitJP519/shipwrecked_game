import time
import random
from art import *

def start_game(): #Starts the game
  try:
      user_name = input("What is your name? ->")
      
      print("You, ", user_name, 
      "crashed near the shores of Roanoke Island."
      "following the storm that ",
      "took out your cruise ship. ",
      "You seem to be alone. ",
      "What are you going to do now?")

      choice_1()

  except Exception as e:
    print("An error occurred:", str(e))
def end_game():#Ends the game
  print("Would you like to play again?")
  user_choice = input("1. Yes "
                      "\n 2. No ")
  if user_choice == "1":
    print("Restarting game...")
    time.sleep(2)
    print('Game restarted!')
    intro_art()
    start_game()

  else:
    print("Thanks for playing!")
    exit()
def choice_1():#First choice after crashing.
  user_choice = input("What are you going to do? "
                       "\n 1. Stay put " 
                       "\n 2. Look for food "
                       "\n 3. Look for survivors->")

  if user_choice == "1":
      print("\n\n You decide to stay put.")
      print("You figure that not moving is the best option."
            "Someone will have noticed the giant capsized cruise ship"
            "and will try to rescue you. So you wait.")
      time.sleep(3)
      print("\n\nYou waited for hours. No help arrives. You are starting to feel hungry. "
  "Looking around, you notice some debris from the ship hitting the shoreline. "
  "There are a few suitcases, some waterlogged boxes, and a burlap sack. "
  "Behind you, there's a jungle. What will you do? -->")
      user_choice = input("1. Check out the suitcases. "
                       "\n 2. Check out the boxes "
                       "\n 3. Check out the sack "
                       "\n 4. Enter the jungle ")
      if user_choice == "1":
        suitecases()
      elif user_choice == "2":
        boxes()  
      elif user_choice == "3":
        sack()
      else:
        jungle()
        
  elif user_choice == "2":
      print("\n\n You decide to look for food.")
def go_back():
  print("You head back to the crash site.")
def suitecases():
  print("You check out the suitcases.")
  print("You find some waterlogged sundresses.")
  print("You find snack pretels, some beef jerky and a cigar box.")
  inven =[ "waterlogged sundresses", "snack pretels", "beef jerky", "cigar box"]
  print("You decide to pick up:", inven)
def boxes():
  print("You check out the boxes.")
  print("You find some bed linens.")
  print("You find a first aid kit.")
  inven =[ "first aid kit" , "bed linens"]
  print("You decide to pick up", inven)
def sack():
  print("You check out the sack.")
  print("You find some rotten food.")
  print("You decide to head back.")
def jungle():
  print("You decide to enter the jungle.")
  print("You walk for hours until you come across a cave. You could try to explore it, or keep walking. What will you do?")
  user_choice = input("1. Explore the cave "
                       "\n 2. Keep walking ")
  if user_choice == "1": 
    print("You decide to explore the cave.")
    death_art()
    print("\n Deep inside the cave, you find a sleeping bear. You attempt to creep out of the cave, but the bear wakes up and eats you.")
    print("You died.")
    end_game()
  else:
    print("You decide to keep walking.")
    print("")
    print(""""You walk for hours until you come large splotch of blood on the ground. Maybe it's a survivor. Should you follow the trail to see where it leads?""")
    user_choice = input("1. Yes "
                       "\n 2. No")

    
    if user_choice == "1": 
      print("""You decide to follow the trail of blood. """)
      death_art()
      print("\n The trail of blood led right to a group of cannibals living on the island. The supreme chef Slowick would later comment on your taste as bland and uninspiring. Would have been better as a s'more, 3/10 \n \n You died. Obviously.")
      end_game()
    else:
      print("You decide not to follow the trail of blood.")
      print(""""It's getting dark out. You need to decide where to make shelter for the night if you want to survive. Should you make a tent, or sleep in a cave?""")
    user_choice2 = input("1. Make a tent where you are. "
                          "\n 2. Make a tent at the edge of the jungle."
                          "\n 3. Sleep in the cave."
                        )
    if user_choice2 == "1":
      print("You decide to make a tent where you are.")
    
    if user_choice2 == "2":
      print("You decide to make camp for the night near the edge of the jungle. \n You wake up to the sound of birds chirping and singing.")
     
      