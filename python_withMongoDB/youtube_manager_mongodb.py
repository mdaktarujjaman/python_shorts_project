from pymongo import MongoClient

client = MongoClient("mongodb+srv://your_user_name:your_pass@cluster1.plkjvik.mongodb.net/") # Not a good idea to expose credentials like this in production code!

db = client["youtube_manager_db"]
video_collection = db["videos"]

print(video_collection)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def view_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def update_video(video_id, name, time):
    video_collection.update_one(
        {'_id': video_id},
        {'$set': {'name': name, 'time': time}}
    )

def delete_video(video_id):
    video_collection.delete_one({'_id': video_id})


def main():
    while True:
        print("\nYouTube Video Manager")
        print("1. Add Video")
        print("2. View Videos")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '2':
            view_videos()
        elif choice == '3':
            video_id = input("Enter the ID of the video to update: ")
            name = input("Enter the name of the video to update: ")
            time = input("Enter the new time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the ID of the video to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
