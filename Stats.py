import csv

# CSV file to store data
CSV_file = "team_stats.csv"

# Load data from CSV 
def load_data():
    players = []
    try:
        with open(CSV_file, "r", newline="") as file:
            lector = csv.DictReader(file)
            for row in lector:
                players.append(dict(row))
    except FileNotFoundError:
        pass
    return players

# Save data in CSV
def save_data(players):
    with open(CSV_file, "w", newline="") as file:
        fields = ["Pos", "Player", "Appearances", "Goals", "Assists", "CleanSheets", "RedCards", "Mvp"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for player in players:
            writer.writerow(player)
      
# Initialize app, load data from CSV
team = load_data()

# Import tabulate - pip install tabulate
from tabulate import tabulate  

# Function to add player to the team
def add_player():
    while True:
        print("==============================================")
        print("Add new player to team")
        print("==============================================")
        print("1. Add player")
        print("2. Main menu")

        option = input("Select an option: ")

        if option == "1":
            Pos = input("Posición del player: ")
            player = input("Nombre del player: ")
            appearances = int(input("appearances: "))
            goals = int(input("goals: "))
            assists = int(input("assists: "))
            clean_sheets = int(input("Clean Sheets: "))
            red_cards = int(input("Red Cards: "))
            mvp = int(input("MVP: "))

            player_stats = {
                "Pos": Pos,
                "Player": player,
                "Appearances": appearances,
                "Goals": goals,
                "Assists": assists,
                "CleanSheets": clean_sheets,
                "RedCards": red_cards,
                "Mvp": mvp
            }

            team.append(player_stats)
            print(f"player {player} has been added succesfully.")
        elif option == "3":
            option = main_menu()
        elif option == "2":
            option = main_menu()
            save_data(team)
            break
        else:
            print("Invalid choice. Please, try again.")

# Function to show a player stats
def show_stats(player_name):
    for player in team:
        if player["player"] == player_name:
            print(f"{player_name} stats:")
            for key, value in player.items():
                print(f"{key}: {value}")
            return
    print(f"No stats found for {player_name}.")

# Function to show all players stats in a table
def show_all_stats():
    if team:
        print("Players stats:")
        players = []
        stats = []
        for player in team:
            players.append(player["player"])
            stats.append([player["Pos"], player["Appearances"], player["Goals"], player["Assists"],
                                 player["CleanSheets"], player["RedCards"], player["Mvp"]])

        # Use tabulate to show all data in a table
        print(tabulate(stats, headers=["Pos", "Appearances", "Goals", "Assists", "CleanSheets", "RedCards", "Mvp"],
                       showindex=players, tablefmt="grid"))
    else:
        print("No stats found.")

# Function main menu
def main_menu():
    print("==============================================")
    print("Football team stats")
    print("==============================================")
    print("1. Add player")
    print("2. Show player stats")
    print("3. Show all players stats")
    print("4. Update stats of a player")
    print("5. Delete a player")
    print("6. Exit")

    option = input("Choose an option: ")
    return option

while True:
    option = main_menu()

    if option == "1":
        add_player()
    elif option == "2":
        player = input("Enter player name: ")
        show_stats(player)
    elif option == "3":
        show_all_stats()
    elif option == "4":
        player = input("Enter player name you want to update: ")
        update_stats(player)
        save_data(team)
    elif option == "5":
        player = input("Enter player name you want to delete: ")
        eliminate_player(player, team)
        save_data(team)
    elif option == "6":
        print("¡Thanks for using the app!")
        break
    else:
        print("No valid option. Please, try again.")

    print("¡Thanks for using the app!")
    break