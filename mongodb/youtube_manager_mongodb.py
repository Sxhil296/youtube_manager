# import pymongo
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")


client = MongoClient(MONGODB_URI)

db = client["ytmanager"]
video_collection = db["videos"]

# print(video_collection)

def list_videos():
    print('\n')
    print("*"*65)
    for video in video_collection.find():
        print(f"ID : {video['_id']}, Name : {video['name']}, Time : {video['time']}")
    print("*"*65)
    print('\n')

def add_video(name, time):
    video_collection.insert_one({"name": name, "time":time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set":{"name":new_name,"time":new_time}})

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube Manager | Choose an option\n")
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
            update_video(video_id, new_name, new_time)
        elif choice=='4':
            video_id=input("Enter the video ID: ")        
            delete_video(video_id)
        elif choice=='5':
            break
        else:
            print("Invalid Choice")
        

if __name__ == "__main__":
    main()