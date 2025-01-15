import art
print(art.logo)
bids = {}
again = True

def find_highest_bidder(dict):
    highest = 0
    winner = ""
    for key in dict:
        if dict[key] > highest:
            winner = f"The winner is {key} with a bid of ${dict[key]}"
            highest = dict[key]
    print(winner)

while again:
    name = input("What is your name? : ")
    price = int(input("What's your bid? : "))
    bids[name] = price
    should_continue = input("Are they any other bidders? Type 'yes' or 'no'.")

    if should_continue == "no":
        again = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)


