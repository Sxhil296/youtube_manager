import sqlite3
from tabulate import tabulate

conn = sqlite3.connect("youtube_manager.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
  ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("\n")
        print('*'*65)
        print("The table is empty.")
        print("\n")
        print('*'*65)
    else:
        headers = [description[0] for description in cursor.description]
        print("\n")
        # print('*'*65)
        print(tabulate(rows, headers=headers, tablefmt='grid'))
        # print('*'*65)
        print("\n")

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE ID=?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE ID=?", (video_id,))
    conn.commit()

def main():
    while True:
        print('\n Youtube Manager | Select an option')
        print("1. List Videos ")
        print("2. Add Video ")
        print("3. Update Videos ")
        print('4. Delete Videos ')
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video duration: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            new_name = input("Enter the video name: ")
            new_time = input("Enter the video duration: ")
            update_video(video_id, new_name, new_time)
        elif choice == '4':
            video_id = input("Enter video ID to update: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")

    conn.close()

if __name__ == "__main__":
    main()