from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
waiting="y"
bid={}
print("Welcome to the auction program.")

while waiting[0]=='y': 

  name=input("What is your name? :")
  amount=input("What's your bid? :$")
  bid[name]=amount
  #print(bid)
  waiting=input("Is there any other bidder waiting? :")
  clear()

max=0
winner=""
for name in bid:
  bid_amount=int(bid[name]) #bid[name] stands for the amount corresponding to the name
  if bid_amount > max:
    max=bid_amount
    winner=name

print(f"The winner is {winner} with a bid of ${max}")