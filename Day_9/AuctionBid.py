from art import logo
from os import system   # Python modeule to clear screen

print(logo)
print("\n ================= Welcome to The Secret Auction Game ================= \n")

# Function to get Name and Bid
def get_name_and_bid():
    bidder_name = input("Enter your Name : ")
    bid = float(input("Enter your bid : $"))
    return bidder_name, bid
# Function to get Name and Bid
def add_name_and_bid(bidder_name, bid):
    bidder_name_and_bid[bidder_name] = bid
# Function to get highest bid
def get_highest_bidder():
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidder_name_and_bid:
        if bidder_name_and_bid[bidder] > highest_bid:
            highest_bid = bidder_name_and_bid[bidder]
            highest_bidder = bidder
    return highest_bid, highest_bidder

bidder_name_and_bid = {}
game_continue = True

bidder_name, bid = get_name_and_bid()
add_name_and_bid(bidder_name, bid)

while game_continue:
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == "yes":
        system("cls")
        bidder_name, bid = get_name_and_bid()
        add_name_and_bid(bidder_name, bid)
    elif other_bidders == "no":
        highest_bid, highest_bidder = get_highest_bidder()
        print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}")
        print("\n ================= Thank you for participating in the auction =================")
        game_continue = False

print(bidder_name_and_bid)