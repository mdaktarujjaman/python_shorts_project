import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []
    
def save_deta_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)
    

def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    print("List of all Youtube Videos")
    for index, video in enumerate(videos, start=1):
        print("-" * 50)
        print(f"{index}. Name:{video['name']}, Duration:{video['time']}")
    print("*" * 50)
    
    
def add_video(videos):
    name = input("Enter video title: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_deta_helper(videos)
    
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: "))
    if 1<= index < len(videos):
        name = input("Enter new video title: ")
        time = input("Enter new video time: ")
        videos[index-1] = {"name": name, "time": time}
        save_deta_helper(videos)
    else:
        print("Invalid index. Please try again.")
        
        
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_deta_helper(videos)
    else:
        print("Invalid index. Please try again.")


def main():
    videos = load_data()  # Assume this function loads existing video data
    while True:
        print("\n ** Youtube Manager  **")
        print(" 1.List all youtube Video")
        print(" 2.Add Youtube video")
        print(" 3.Update Youtube video")
        print(" 4.Delete Youtube video")
        print(" ** Exit **")
        choice = input("Enter your choice: ")
        # print(videos)
        
        
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()