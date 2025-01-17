import art
print(art.logo)
print("Welcome to the Auction!")
bids={}
highest_value=0
winner=""
loop=True
while loop:
    person_amt = input("What's Your Name: ")
    bid_amt = int(input("Enter Your BID Amount:$ "))
    repeat_loop = input("Are there any other bidders?Type \"Yes or No\":").lower()
    bids[person_amt] = bid_amt
    print("\n"*100)   #For New Line So its like blind bidding can't see previous bids.
    if repeat_loop=='no':
        print(bids)
        loop=False
        for bidder, amount in bids.items():
            if highest_value < amount:
                highest_value += amount
                winner = bidder
    else:
        print("Type Proper characters!!")
print(f"The Winner is {winner} with bit amount of ${highest_value}.")
