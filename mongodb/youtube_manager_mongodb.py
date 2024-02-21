# import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://youtube_py:youtube_py@cluster0.rjhsn2x.mongodb.net/")

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_videos():
    video_collection.find()

def add_video(name, time):
    video_collection.insert_one({"name": name, "time":time})

def update_video(video_id, new_name, new_time):
    pass

def delete_video(video_id):
    pass


def main():
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all videos ")
        print("2. Add a new video ")
        print("3. Update video details ")
        print('4. Delete a video ')
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        if choice=='1':
            list_videos()
        elif choice=='2':
            name=input("Enter the video name: ")
            time=input("Enter the video duration: ")
            add_video(name, time)
        elif choice=='3':
            video_id=input("Enter the video ID: ")
            new_name=input("Enter the new video name: ")
            new_time=input("Enter the new video duration: ")
            update_video(name, time)
        elif choice=='4':
            video_id=input("Enter the video ID: ")        
            delete_video(name, time)
        elif choice=='5':
            break
        else:
            print("Invalid Choice")
        

if __name__ == "__main__":
    main()