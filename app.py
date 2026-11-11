import json

def load_rounds():
    try:
        with open("rounds.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

rounds = load_rounds()

def save_rounds():
    with open("rounds.json", "w") as file:
        json.dump(rounds, file, indent=4)

def get_int(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if value < min_value or value > max_value: 
            print(f"Please enter a number between {min_value} and {max_value}.")
            continue
        return value

def show_menu():
    print("\n--- GOLF PERFORMANCE TRACKER ---")
    print("1. Add Round")
    print("2. View Rounds")
    print("3. View Statistics")
    print("4. Reset All Data")
    print("5. Exit")

def add_round():
    course = input("Course name:")
    score = get_int("Score: ", 1, 200)
    fairways = get_int("Fairways hit: ", 0, 18)
    gir = get_int("Greens in regulation: ", 0, 18)
    putts = get_int("Putts: ", 0, 100)

    round_data = {
        "course": course,
        "score": score,
        "fairways": fairways,
        "gir": gir,
        "putts": putts
    }
    rounds.append(round_data)
    save_rounds()

    print("Round added successfully!")

def view_statistics():
    if not rounds:
        print("No rounds recorded yet.")
        return


    scores = []
    putts = []
    fairways = []
    gir = []

    for round_data in rounds:
        scores.append(round_data['score'])
        putts.append(round_data['putts'])
        fairways.append(round_data['fairways'])
        gir.append(round_data['gir'])

    average_score = sum(scores) / len(scores)
    average_putts = sum(putts) / len(putts)
    average_fairways = sum(fairways) / len(fairways)
    average_gir = sum(gir) / len(gir)
    fairway_percent = average_fairways / 18 * 100
    gir_percent = average_gir / 18 * 100
    best_score = min(scores)
    

    for round_data in rounds:
        if round_data['score'] == best_score:
            best_round = round_data

    print(f"Rounds Played: {len(rounds)}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Best Round: {best_round['course']} - {best_round['score']}")
    print(f"Average Putts: {average_putts:.2f}")
    print(f"% Fairways Hit: {fairway_percent:.2f}%")
    print(f"GIR %: {gir_percent:.2f}%")

def view_rounds():
    if not rounds:
        print("No rounds recorded yet.")
        return

    for i, round_data in enumerate(rounds, start=1):
        print(f"\nRound {i}:")
        print(f"Course: {round_data['course']}")
        print(f"Score: {round_data['score']}")
        print(f"Fairways hit: {round_data['fairways']}")
        print(f"GIR: {round_data['gir']}")
        print(f"Putts: {round_data['putts']}")

def reset_rounds():
    decision = input("Are you sure you want to reset all data? (y/n): ")
    if decision.lower() == "y":
        rounds.clear()
        save_rounds()
        print("All rounds and data have been reset.")
    else:
        print("Reset operation cancelled.")
while True:
    show_menu()

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_round()
    elif choice == "2":
        view_rounds()
    elif choice == "3":
        view_statistics()
    elif choice == "4":
        reset_rounds()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-5.")