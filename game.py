# Modules
from asyncore import compact_traceback
import math 
import random

# Welcome
name = input("Hello gamer! Please Enter Your Name 😉 : ")
comp_name="Jarwis"
print(f"Hello {name}! Welcome to the Game of Virtual Cricket 🎉🎉")

user2_count=0
user1_count=0

##Functios:

# User's turn to bat first
def user_play_first(user_out, user_sum, user_turn):
    while(user_out==0):
        user_runs=int(input(f"Hit the {user_turn +1} ball : "))
        comp_runs=random.randint(0,6)
        print(f"Jarwis bowled for {comp_runs} runs")
        if 0>user_runs or user_runs>6:
            print("Please score runs from 0 to 6 only")
            continue
        
        elif user_runs==0:
            user_sum+=comp_runs
            
        elif(user_runs==comp_runs):
            print(f"{name} you got bowled by Jarwis")
            user_out=1
            user_turn+=1
        
        else:
            user_sum+=user_runs
            user_turn+=1
            
    print(f"Total score of {name} is {user_sum} 🎉")
    return user_sum

# User's turn to bat second
def user_play_second(user_out, user_sum, user_turn, comp_sum):
    while(user_out==0):
        user_runs=int(input(f"Hit the {user_turn +1} ball : "))
        comp_runs=random.randint(0,6)
        print(f"Jarwis bowled for {comp_runs} runs")
        if 0>user_runs or user_runs>6:
            print("Please score runs from 0 to 6 only")
            continue
        
        elif(user_runs>comp_sum+1):
            user_out=1
        
        elif user_runs==0:
            user_sum+=comp_runs
            
        elif(user_runs==comp_runs):
            print(f"{name} you got bowled by Jarwis")
            user_out=1
            user_turn+=1
        
        else:
            user_sum+=user_runs
            user_turn+=1
            
    print(f"Total score of {name} is {user_sum} 🎉")
    return user_sum

# Computer's turn to bat second
def comp_play_second(comp_out, comp_sum, comp_turn, user_sum):
    while(comp_out==0):
        comp_runs=random.randint(0,6)
        user_runs=int(input(f"Bowl for the {comp_turn + 1} ball "))
        print(f"Jarwis took {comp_runs} runs  ")
        if(user_runs<0 or user_runs > 6):
            print("Please ball from 0 to 6 only!")
            continue
        
        elif(comp_sum>user_sum+1):
            comp_out=1
        
        elif(comp_runs==user_runs):
            print("You Bowled Jarwis 🎉 ")
            comp_out=1
            
        elif(comp_runs==0):
            comp_sum+=user_runs
            comp_turn+=1
            
        else:
            comp_sum+=comp_runs
            comp_turn+=1
            
    print(f"Total score of Jarwis is : {comp_sum} ")
    return comp_sum

# Computer's turn to bat first
def comp_play_first(comp_out, comp_sum, comp_turn):
    while(comp_out==0):
        comp_runs=random.randint(0,6)
        user_runs=int(input(f"Bowl for the {comp_turn + 1} ball "))
        print(f"Jarwis took {comp_runs} runs ")
        if(user_runs<0 or user_runs > 6):
            print("Please ball from 0 to 6 only!")
            continue
        
        elif(comp_runs==user_runs):
            print("You Bowled Jarwis 🎉 ")
            comp_out=1
            
        elif(comp_runs==0):
            comp_sum+=user_runs
            comp_turn+=1
            
        else:
            comp_sum+=comp_runs
            comp_turn+=1
            
    print(f"Total score of Jarwis is : {comp_sum} ")
    return comp_sum
    
# Winning condition
def winner(comp_sum, user_sum):
    if(comp_sum==user_sum):
        print("The match got draw! 😑")
        
    elif(comp_sum>user_sum):
        print(f"{name} you lost the game! 🤣 Better luck next time 😌")
        global user2_count
        user2_count+=1
        
    else:
        print(f"Hurrayy! {name} You won the match! cheers 🍻🔥")
        global user1_count
        user1_count+=1
        
#Batting or Bowling
def play_order1(play):
    if(play=="BAT"):
        print("Remember to Enter the runs from 0 to 6")
        user_out=0
        comp_out=0
        user_sum=0
        comp_sum=0
        user_turn=0
        comp_turn=0
        
        user_sum=user_play_first(user_out, user_sum, user_turn)
        
        print("Now it's Jarwis turn to Bat!")
        
        comp_sum=comp_play_second(comp_out, comp_sum, comp_turn, user_sum)
        
        winner(comp_sum, user_sum)

    elif(play=='BALL'):
        print("Remember to Enter the runs from 0 to 6")
        user_out=0
        comp_out=0
        user_sum=0
        comp_sum=0
        user_turn=0
        comp_turn=0
        
        comp_sum=comp_play_first(comp_out, comp_sum, comp_turn)
        
        print(f"Now it's your turn to Bat {name}!")
        
        user_sum=user_play_second(user_out, user_sum, user_turn, comp_sum)
        
        winner(comp_sum, user_sum)
        
    else:
        print("Invalid input for playing! ⚠️ Please try again!")
        play_check()
        
def play_order2(play):
    if(play=="BAT"):
        print("Remember to Enter the runs from 0 to 6")
        user_out=0
        comp_out=0
        user_sum=0
        comp_sum=0
        user_turn=0
        comp_turn=0
        
        comp_sum=comp_play_first(comp_out, comp_sum, comp_turn)
        
        print(f"Now it's your turn to Bat {name}!")
        
        user_sum=user_play_second(user_out, user_sum, user_turn, comp_sum)
        
        winner(comp_sum, user_sum)
        
        

    elif(play=='BALL'):
        print("Remember to Enter the runs from 0 to 6")
        user_out=0
        comp_out=0
        user_sum=0
        comp_sum=0
        user_turn=0
        comp_turn=0
        
        user_sum=user_play_first(user_out, user_sum, user_turn)
        
        print("Now it's Jarwis turn to Bat!")
        
        comp_sum=comp_play_second(comp_out, comp_sum, comp_turn, user_sum)
        
        winner(comp_sum, user_sum)
        
        
    else:
        print("Invalid input for playing! ⚠️ Please try again!")
        play_check()

# Fuction to check the bat and ball
def play_check(user_chnace,comp_chance):
    if(user_chnace==1):
        play=input("Please Enter BAT for Batting 1st or BALL for Bowling 1st : ").upper()
        print(f"{name} choose to {play}")
        play_order1(play)
        
    else:
        play=random.choice(["BAT","BALL"])
        print(f"Jarwis choose to {play}")
        play_order2(play)
        

# Function to chech the toss
def toss_check():
    toss=input("Select 'E' for Even & 'O' for Odd : ").upper()
    if toss=='E' or toss == 'O':
        user_choice=int(input("Enter any number in from 1 to 10 : "))
        comp_choice=random.randint(1,10)
        print(f"Jarwis chosse {comp_choice}")
        total_choice=user_choice+comp_choice
        if(total_choice%2==0 and toss=='E'):
            print(f"{name}! You won the toss 🎉 and {comp_name} lost the toss")
            play_check(user_chnace=1,comp_chance=0)     
            
        elif(total_choice%2!=0 and toss=='O'):
            print(f"Hurray {name}! You won the toss 🎉 and {comp_name} lost the toss")
            play_check(user_chnace=1,comp_chance=0)                   
                    
        else:
            print(f"Sorry {name}! You lost the toss 🙄 and {comp_name} won the toss")
            play_check(user_chnace=0,comp_chance=1) 
            
    else:
        print("Invalid input for Toss! ⚠️ Please try again")
        toss_check()

# Functions for number of users
def no_of_users():    
    # No.of users
    print("Please Select the Number of users in the game 🤴🏼 : ")
    users = int(input("Enter '1' for one user, '2' for two users : "))

    # If one user
    if users == 1:
        times = int(input("How many times you want to play this game? 🤔 : "))
        while times > 0:
            toss_check()   
            times-=1
        if(user1_count>user2_count):
            print(f"{name} Won the grand finale 🔥🍻🎉")
        elif(user2_count>user1_count):
            print("Jarwis Won the grand finale 🔥🍻🎉")
        else:
            print("The Grand finale ended with a draw 😑")

    elif users == 2:
        print("More than one person can't play this game as there is a chance of cheating")

    else:
        print("Invalid input for number of users ⚠️, Please try again! 😑")
        no_of_users()

##Fucnction callls
no_of_users()