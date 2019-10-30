from datetime import datetime
import json

# additional imports if needed

# global variables
SHOWS_FILE = "./shows.json"
TRANSACTIONS_FILE = "./transactions.txt"
TICKET_FILE = "./ticket.txt"
SALES_TAX = 0.07  # 7% Sales Tax


def time():
    return datetime.datetime.now


def load_shows(filename):
    with open(filename) as file:
        show_inventory = json.load(file)
    return show_inventory


def save_show_inventory():
    with open(TRANSACTIONS_FILE, "a") as file:
        file.write(f"\n {name}, {show}, {code}, {tickets}, {price}, {tax}, {time()}")
    print("Thank you and enjoy!")


def get_inventory(show_inventory):
    print("Here's what we have playing: ")
    for show in show_inventory:
        artist = show.get("artist")
        opener = show.get("opener")
        date = show.get("date")
        doors = show.get("doors")
        show = show.get("show")
        price = show.get("price")  ########## STR HAS NO ATTRIBUTE 'GET' :( ##########
        tickets = show.get("tickets")
        max_size = show.get("maxSize")
        code = show.get("code")
        formatted_inventory = "{} with {}, on {}, starting at {}. Doors open at {}, with {} tickets at ${} a piece!"
        print(
            formatted_inventory.format(
                artist, opener, date, show, doors, tickets, price
            )
        )


def main():
    show_inventory = load_shows(SHOWS_FILE)
    show_information = get_inventory(show_inventory)

    while True:
        print("Welcome to The Jefferson venue ticket purchasing tool!")
        user_input = input("What would you like to see today? ")
        if user_input in show_information:
            how_many_tickets = int(input("How many tickets? "))
            if how_many_tickets > show.get("tickets"):
                print("We don't have that many tickets available.")
                continue
            elif how_many_tickets > 4:
                print("The most tickets that you can buy is 4.")
                continue
            else:
                total_price = show.get("price") * how_many_tickets * SALES_TAX
                print("{} tickets for {} will be: ${}!").format(
                    how_many_tickets, user_input, total_price
                )
                save_show_inventory()
                break
        else:
            print("We are not showing that.")
            continue


if __name__ == "__main__":
    main()
