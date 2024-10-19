import os

japanese_songs = [
    {"title": "Hollow Purple", "artist": "Alisa Okehazama"},
    {"title": "Blue Bird", "artist": "Ikimono Gakari"},
    {"title": "Orange", "artist": "7"},
    {"title": "Mosawo", "artist": "Koiiro"},
    {"title": "Shinzo wo Sasageyo", "artist": "Linked Horizon"}
]

korean_songs = [
    {"title": "Only", "artist": "Lee Hi"},
    {"title": "Bang Bang Bang", "artist": "BigBang"},
    {"title": "Solo", "artist": "Jennie"},
    {"title": "Way Back Home", "artist": "Shaun"},
    {"title": "Super Shy", "artist": "New Jeans"}
]

english_songs = [
    {"title": "Die With A Smile", "artist": "Bruno Mars"},
    {"title": "Ghost", "artist": "Justin Bieber"},
    {"title": "Lovely", "artist": "Billie Eilish"},
    {"title": "Who Says", "artist": "Selena Gomez"},
    {"title": "Love Story", "artist": "Taylor Swift"}
]

def display_songs(song_list, category_name=None):
    if category_name:
        print(f"\n========== {category_name} ==========")
    if song_list:
        max_title_len = max(len(song["title"]) for song in song_list)
        for index, song in enumerate(song_list, start=1):
            print(f"{index}. {song['title']:<{max_title_len}}  by {song['artist']}")
    else:
        print("No songs available.")

def search_music():
    search_query = input("\nEnter song title or artist to search: ").lower()
    found_songs = []

    all_songs = japanese_songs + korean_songs + english_songs
    for song in all_songs:
        if search_query in song["title"].lower() or search_query in song["artist"].lower():
            found_songs.append(song)

    if found_songs:
        print("\nSearch Results:")
        display_songs(found_songs)
    else:
        print("\nNo matching songs found.")
    input("\nPress Enter to go back.")

def display_all_songs():
    print("\n========== All Songs ==========")

    sorted_japanese_songs = sorted(japanese_songs, key=lambda song: song["title"].lower())
    sorted_korean_songs = sorted(korean_songs, key=lambda song: song["title"].lower())
    sorted_english_songs = sorted(english_songs, key=lambda song: song["title"].lower())

    display_songs(sorted_japanese_songs, "Japanese Songs")
    display_songs(sorted_korean_songs, "Korean Songs")
    display_songs(sorted_english_songs, "English Songs")

    input("\nPress Enter to go back.")

def song_menu(song_list, category_name):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print(f"========== {category_name} ==========")
        print("1. Display Songs")
        print("2. Add Song")
        print("3. Delete Song")
        print("0. Back")
        choice = input("Choose an option: ")

        if choice == '1':
            display_songs(song_list, category_name)
            input("\nPress Enter to go back.")
        elif choice == '2':
            add_song(song_list)
        elif choice == '3':
            delete_song(song_list)
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")

def add_song(song_list):
    title = input("Enter the song title: ")
    artist = input("Enter the artist: ")
    song_list.append({"title": title, "artist": artist})
    print(f"\n'{title}' by {artist} has been added.")
    input("Press Enter to go back.")

def delete_song(song_list):
    display_songs(song_list)
    try:
        song_num = int(input("\nEnter the number of the song to delete: "))
        if 1 <= song_num <= len(song_list):
            removed_song = song_list.pop(song_num - 1)
            print(f"\n'{removed_song['title']}' by {removed_song['artist']} has been deleted.")
        else:
            print("Invalid song number.")
    except ValueError:
        print("Please enter a valid number.")
    input("Press Enter to go back.")

def display_main_menu():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("========== Playlist Music ==========")
    print("1. Japanese Song")
    print("2. Korean Song")
    print("3. English Song")
    print("4. Display All Songs")
    print("5. Search Music")
    print("0. Keluar")
    return input("Masukan Pilihan: ")

def main():
    while True:
        choice = display_main_menu()
        
        if choice == '1':
            song_menu(japanese_songs, "Japanese Songs")
        elif choice == '2':
            song_menu(korean_songs, "Korean Songs")
        elif choice == '3':
            song_menu(english_songs, "English Songs")
        elif choice == '4':
            display_all_songs()
        elif choice == '5':
            search_music()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
