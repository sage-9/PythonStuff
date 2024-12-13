import random
from collections import Counter

# Constants for anime universes and characters
ANIME_UNIVERSES = {
    1: "Naruto",
    2: "One Piece",
    3: "Demon Slayer"
}

CHARACTERS = {
    1: ["Naruto", "Sasuke", "Hinata", "Sakura", "Kakashi", "Hiruzen", "Gaara", "Rock-Lee", "Ino"],
    2: ["Luffy", "Zoro", "Nami", "Sanji", "Chopper", "Brook", "Usopp", "Robin", "Trafalgar"],
    3: ["Tanjiro", "Nezuko", "Inosuke", "Zenitsu", "Obanai", "Mitsuri", "Shinobu", "Giyu", "Rengoku"]
}

# Function to spin for anime universes
def anime_universe_spin(number_tries):
    return [random.randint(1, 3) for _ in range(number_tries)]

# Function to count occurrences of anime universes
def collate_results(results):
    return [results.count(1), results.count(2), results.count(3)]

# Function to pick random characters
def pick_characters(number_of_cards, anime):
    return [CHARACTERS[anime][random.randint(0, 8)] for _ in range(number_of_cards)]

# Function to print results of anime universe cards
def print_results(collated_results):
    for i, count in enumerate(collated_results, start=1):
        print(f"Number of {ANIME_UNIVERSES[i]} cards = {count}")

# Function to save the summary of characters to a file
def save_summary_to_file(all_characters, filename="summary_results.txt"):
    character_counts = Counter(all_characters)
    with open(filename, "w") as file:
        file.write("Summary of Characters:\n")
        for character, count in character_counts.items():
            file.write(f"{character}: {count}\n")
    print(f"\nSummary of characters saved to {filename}")

# Function to save shuffled characters to a file
def save_characters_to_file(all_characters, filename="shuffled_characters.txt"):
    with open(filename, "w") as file:
        file.write("Selected Characters (Shuffled):\n")
        file.writelines(f"{character}\n" for character in all_characters)
    print(f"\nShuffled characters saved to {filename}")

# Main function
def main():
    number_of_tries = int(input("How many cards do you want?\n"))
    
    # Get anime universe results and collate them
    universe_results = anime_universe_spin(number_of_tries)
    collated_universe_results = collate_results(universe_results)
    
    # Collect all characters in a single list
    all_characters = []
    for anime, count in enumerate(collated_universe_results, start=1):
        if count > 0:
            all_characters.extend(pick_characters(count, anime))
    
    # Print universe results
    print_results(collated_universe_results)
    
    # Save summary results before shuffling
    save_summary_to_file(all_characters)
    
    # Shuffle the list of characters
    random.shuffle(all_characters)
    
    # Save shuffled characters to a file
    save_characters_to_file(all_characters)

# Run the main function
if __name__ == "__main__":
    main()
