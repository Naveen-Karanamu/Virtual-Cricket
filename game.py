# Modules
from asyncore import user2act_traceback
import math 
import random

# Welcome
name = input("Hello gamer! Please Enter Your Name 😉 : ")
user2_name="Jarwis"
print(f"Hello {name}! Welcome to the Game of Virtual Cricket 🎉🎉")

##Functios:

# user1's turn to bat first
def user1_play_first(user1_out, user1_sum, user1_turn):
    while(user1_out==0):
        user1_runs=int(input(f"Hit the {user1_turn +1} ball : "))
        user2_runs=random.randint(0,6)
        print(f"{user2_name} bowled for {user2_runs} runs")
        if 0>user1_runs or user1_runs>6:
            print("Please score runs from 0 to 6 only")
            continue
        
        elif user1_runs==0:
            user1_sum+=user2_runs
            
        elif(user1_runs==user2_runs):
            print(f"{name} you got bowled by {user2_name}")
            user1_out=1
            user1_turn+=1
        
        else:
            user1_sum+=user1_runs
            user1_turn+=1
            
    print(f"Total score of {name} is {user1_sum} 🎉")
    return user1_sum

# user1's turn to bat second
def user1_play_second(user1_out, user1_sum, user1_turn, user2_sum):
    while(user1_out==0):
        user1_runs=int(input(f"Hit the {user1_turn +1} ball : "))
        user2_runs=random.randint(0,6)
        print(f"{user2_name} bowled for {user2_runs} runs")
        if 0>user1_runs or user1_runs>6:
            print("Please score runs from 0 to 6 only")
            continue
        
        elif(user1_runs>user2_sum+1):
            user1_out=1
        
        elif user1_runs==0:
            user1_sum+=user2_runs
            
        elif(user1_runs==user2_runs):
            print(f"{name} you got bowled by {user2_name}")
            user1_out=1
            user1_turn+=1
        
        else:
            user1_sum+=user1_runs
            user1_turn+=1
            
    print(f"Total score of {name} is {user1_sum} 🎉")
    return user1_sum

# user2uter's turn to bat second
def user2_play_second(user2_out, user2_sum, user2_turn, user1_sum):
    while(user2_out==0):
        user2_runs=random.randint(0,6)
        user1_runs=int(input(f"Bowl for the {user2_turn + 1} ball "))
        print(f"{user2_name} scored {user2_runs}  ")
        if(user1_runs<0 or user1_runs > 6):
            print("Please ball from 0 to 6 only!")
            continue
        
        elif(user2_sum>user1_sum+1):
            user2_out=1
        
        elif(user2_runs==user1_runs):
            print(f"You Bowled {user2_name} 🎉 ")
            user2_out=1
            
        elif(user2_runs==0):
            user2_sum+=user1_runs
            user2_turn+=1
            
        else:
            user2_sum+=user2_runs
            user2_turn+=1
            
    print(f"Total score of {user2_name} is : {user2_sum} ")
    return user2_sum

# user2uter's turn to bat first
def user2_play_first(user2_out, user2_sum, user2_turn):
    while(user2_out==0):
        user2_runs=random.randint(0,6)
        user1_runs=int(input(f"Bowl for the {user2_turn + 1} ball "))
        print(f"{user2_name} scored {user2_runs}  ")
        if(user1_runs<0 or user1_runs > 6):
            print("Please ball from 0 to 6 only!")
            continue
        
        elif(user2_runs==user1_runs):
            print(f"You Bowled {user2_name} 🎉 ")
            user2_out=1
            
        elif(user2_runs==0):
            user2_sum+=user1_runs
            user2_turn+=1
            
        else:
            user2_sum+=user2_runs
            user2_turn+=1
            
    print(f"Total score of {user2_name} is : {user2_sum} ")
    return user2_sum
    
# Winning condition
def winner(user2_sum, user1_sum, user1_count, user2_count):
    if(user2_sum==user1_sum):
        print("The match got draw! 😑")
        
    elif(user2_sum>user1_sum):
        print(f"{name} you lost the game! 🤣 Better luck next time 😌")
        user2_count+=1
        
    else:
        print(f"Hurrayy! {name} You won the match! cheers 🍻🔥")
        user1_count+=1
        
        
#Batting or Bowling
def play_order(user1_count, user2_count, play):
    if(play=="BAT"):
        print("Remember to Enter the runs from 0 to 6")
        user1_out=0
        user2_out=0
        user1_sum=0
        user2_sum=0
        user1_turn=0
        user2_turn=0
        
        user1_sum=user1_play_first(user1_out, user1_sum, user1_turn)
        
        print(f"Now it's {user2_name} turn to Bat!")
        
        user2_sum=user2_play_second(user2_out, user2_sum, user2_turn, user1_sum)
        
        winner(user2_sum, user1_sum, user1_count, user2_count)

    elif(play=='BALL'):
        print("Remember to Enter the runs from 0 to 6")
        user1_out=0
        user2_out=0
        user1_sum=0
        user2_sum=0
        user1_turn=0
        user2_turn=0
        
        user2_sum=user2_play_first(user2_out, user2_sum, user2_turn)
        
        print(f"Now it's your turn to Bat {name}!")
        
        user1_sum=user1_play_second(user1_out, user1_sum, user1_turn, user2_sum)
        
        winner(user2_sum, user1_sum, user1_count, user2_count)
        
    else:
        print("Invalid input for playing! ⚠️ Please try again!")
        play_check()

# Fuction to check the bat and ball
def play_check(user1_count, user2_count, user1_chnace,user2_chance):
    if(user1_chnace==1):
        play=input("Please Enter BAT for Batting 1st or BALL for Bowling 1st : ").upper()
        print(f"{name} choose to {play}")
        play_order(play, user1_count, user2_count)
        
    else:
        play=random.choice(["BAT","BALL"])
        print(f"{user2_name} choose to {play}")
        play_order(play, user1_count, user2_count)
        

# Function to chech the toss
def toss_check(user1_count, user2_count):
    toss=input("Select 'E' for Even & 'O' for Odd : ").upper()
    if toss=='E' or toss == 'O':
        user1_choice=int(input("Enter any number in from 1 to 10 : "))
        user2_choice=random.randint(1,10)
        print(f"{user2_name} chosse {user2_choice}")
        total_choice=user1_choice+user2_choice
        if(total_choice%2==0 and toss=='E'):
            print(f"{name}! You won the toss 🎉 and {user2_name} lost the toss")
            play_check(user1_count, user2_count, user1_chnace=1,user2_chance=0)     
            
        elif(total_choice%2!=0 and toss=='O'):
            print(f"Hurray {name}! You won the toss 🎉 and {user2_name} lost the toss")
            play_check(user1_count, user2_count, user1_chnace=1,user2_chance=0)                   
                    
        else:
            print(f"Sorry {name}! You lost the toss 🙄 and {user2_name} won the toss")
            play_check(user1_count, user2_count, user1_chnace=0,user2_chance=1) 
            
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
        user1_count=0
        user2_count=0
        while times > 0:
            toss_check(user1_count, user2_count)          
                
            times-=1

    elif users == 2:
        print(2)

    else:
        print("Invalid input for number of users ⚠️, Please try again! 😑")
        no_of_users()

##Fucnction callls
no_of_users()