import streamlit as st
from googleapiclient.discovery import build

api_key = 'AIzaSyDJmK_6vf--oQQpRavSQ2XNyaX8xyI8KkE'
channel_ids = ['UC2J_VKrAzOEJuQvFFtj3KUw', #csk
               'UC4FUjHHzr753fv9vQ4mE32g', #tamil cricket news
               'UCXsJyNCjFthPLQ9U5KI-Frg', #kickflix
               'UCNMg6XDhRZI2QzL4pWOvP_w', #volleyball world
               'UCtInrnU3QbWqFGsdKT1GZtg', #fiba-the baseketball
              ]

youtube=build('youtube','v3',developerKey=api_key)

def get_channel_stats(youtube,channel_ids):
    all_data = []
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=','.join(channel_ids))
    response = request.execute()
    
    for i in range(len(response['items'])):
        data = dict(channel_name=response['items'][i]['snippet'] ['title'],
                    subscribers=response['items'][i]['statistics']['subscriberCount'],
                    views=response['items'][i]['statistics']['viewCount'],
                    Total_videos=response['items'][i]['statistics']['videoCount'],
                    playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])

        all_data.append(data)
        
    return all_data
channel_statistics = get_channel_stats(youtube, channel_ids)

a = "Youtubedata Harvesting!"
st.write(a)
