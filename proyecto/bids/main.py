from replit import clear
import art

print(art.logo)
bids = {}
higher_bid = 0
winner = ''


def add_people(name_person, bid_amount):
    bids[name_person] = bid_amount


end_bid = True
while end_bid:
    names = input("What's your name: \n")
    price = int(input('Insert your bid: \n'))

    add_people(name_person=names, bid_amount=price)

    end_program_question = input("is there another person that want bid type 'yes' or 'no': \n")
    if end_program_question == 'yes':
        clear()
    elif end_program_question == 'no':
        end_bid = False
        for key in bids:
            if bids[key] > higher_bid:
                higher_bid = bids[key]
                winner = key

print(f'the winner is: {winner} bid: {higher_bid}')
