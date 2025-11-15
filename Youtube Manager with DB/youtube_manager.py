import sqlite3

con = sqlite3.connect('youtube_videos.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    print("\n ** List of YouTube Videos **")
    print("------------------------------------------")
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)
        
        
def add_video(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()
    
    
def update_video(video_id, new_name, new_time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()
    
    
def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()


def main():
    while True:
        print("\n ** YouTube Video Manager app with DB **")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter The Video Name: ")
            time = input("Enter The Video Time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter The Video ID to Update: ")
            name = input("Enter The New Video Name: ")
            time = input("Enter The New Video Time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter The Video ID to Delete: ")
            delete_video(video_id)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
            
    con.close()
            




if __name__ == '__main__':
    main()