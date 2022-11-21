# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


import datetime as dt 
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from .datastore import *

import tweepy
from googleapiclient.discovery import build

clientid = "K3zFmMUSZ-maPz8s9TokiQs0V9NtTv-MpzkFVLPmUWTGJHznU_"
consumer_key = "hed40uwwO3yBYozPwJ6TIZDJD"
consumer_secret = "govduaChw5C5z05GLzZHCNkJImvyRvjJ1DImKty7ygYNEnndkp"
bearertoken = "AAAAAAAAAAAAAAAAAAAAAOfYYgEAAAAAaCY0M6qX9qgapv0Bk%2BvUvC9RDdE%3DbaEvNrXnooc2FQGjtso9qFwUS0YPKXQwiQUz0JvxwREvpA79Bn"
access_token ="792344353024856068-jLbPMxdgTQ9jeHonhbE6nqbp7uvYNQ8"
access_token_secret = "W70yP0eM5mKy9pBL4cYZAa7U8Mfd17PuJ86eI1sO7AUZC"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAOfYYgEAAAAAaCY0M6qX9qgapv0Bk%2BvUvC9RDdE%3DbaEvNrXnooc2FQGjtso9qFwUS0YPKXQwiQUz0JvxwREvpA79Bn"
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"{dt.datetime.now()}")

        return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_elon_tweets"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        search_query = "elon OR musk OR elon musk"
        # get tweets from the API
        tweets = api.search_tweets(search_query,lang='en', count=3,result_type="recent",tweet_mode="extended")
        # store the API responses in a list
        # tweets_copy = []
        # for tweet in tweets:
        #     tweets_copy.append(tweet)
        s=""
        for i in tweets:
            s+="\nhttps://twitter.com/twitter/statuses/"+str(i.id)
            # print(i.full_text)
            # print("-" * 15)
        youtube_api_key = 'AIzaSyCB0RoVJ0ml1cpUbM6GBePuxw8oUYA4Llk'

        youtube = build('youtube','v3',developerKey=youtube_api_key)
        request = youtube.search().list(
                part="id,snippet",
                type='video',
                q="elon musk",
                # videoDuration='short',
                # videoDefinition='high',
                maxResults=3#,
                #fields="nextPageToken,items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
        )
        response = request.execute()

        for i in response['items']:
            s+='\nhttps://www.youtube.com/watch?v='+str(i['id']['videoId'])
        dispatcher.utter_message(text=s)

        return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_cook_tweets"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        search_query = "cook OR tim OR tim cook"
        # get tweets from the API
        tweets = api.search_tweets(search_query,lang='en', count=3,result_type="recent",tweet_mode="extended")
        # store the API responses in a list
        # tweets_copy = []
        # for tweet in tweets:
        #     tweets_copy.append(tweet)
        s=""
        for i in tweets:
            s+="\nhttps://twitter.com/twitter/statuses/"+str(i.id)
            # print(i.full_text)
            # print("-" * 15)
        youtube_api_key = 'AIzaSyCB0RoVJ0ml1cpUbM6GBePuxw8oUYA4Llk'

        youtube = build('youtube','v3',developerKey=youtube_api_key)
        request = youtube.search().list(
                part="id,snippet",
                type='video',
                q="tim cook",
                # videoDuration='short',
                # videoDefinition='high',
                maxResults=3#,
                #fields="nextPageToken,items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
        )
        response = request.execute()

        for i in response['items']:
            s+='\nhttps://www.youtube.com/watch?v='+str(i['id']['videoId'])
        dispatcher.utter_message(text=s)

        return []


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_cricket_media"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        search_query = "cricket"
        # get tweets from the API
        tweets = api.search_tweets(search_query,lang='en', count=3,result_type="recent",tweet_mode="extended")
        # store the API responses in a list
        # tweets_copy = []
        # for tweet in tweets:
        #     tweets_copy.append(tweet)
        s=""
        for i in tweets:
            s+="\nhttps://twitter.com/twitter/statuses/"+str(i.id)
            # print(i.full_text)
            # print("-" * 15)
        youtube_api_key = 'AIzaSyCB0RoVJ0ml1cpUbM6GBePuxw8oUYA4Llk'

        youtube = build('youtube','v3',developerKey=youtube_api_key)
        request = youtube.search().list(
                part="id,snippet",
                type='video',
                q="cricket",
                # videoDuration='short',
                # videoDefinition='high',
                maxResults=3#,
                #fields="nextPageToken,items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
        )
        response = request.execute()

        for i in response['items']:
            s+='\nhttps://www.youtube.com/watch?v='+str(i['id']['videoId'])
        dispatcher.utter_message(text=s)

        return []

# class ActionShowTweets(Action):

#     def name(self) -> Text:
#         return "action_show_tweets"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         try:
#             current_name = next(tracker.get_latest_entity_values("item"))
#             search_query = current_name + " -filter:retweets"
#             # get tweets from the API
#             tweets = api.search_tweets(search_query,lang='en', count=3,result_type="recent",tweet_mode="extended")
#             # store the API responses in a list
#             # tweets_copy = []
#             # for tweet in tweets:
#             #     tweets_copy.append(tweet)
#             s=""
#             if(len(tweets)!=0):
#                 for i in tweets:
#                     s+="\nhttps://twitter.com/twitter/statuses/"+str(i.id)
#             else:
#                 s="Not found"
        
#         except:
#             s="Not found"


#         dispatcher.utter_message(text=s)

#         return []

# class ActionShowVideos(Action):

#     def name(self) -> Text:
#         return "action_show_videos"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         try:
#             current_name = next(tracker.get_latest_entity_values("item"))
#             youtube_api_key = 'AIzaSyCB0RoVJ0ml1cpUbM6GBePuxw8oUYA4Llk'

#             youtube = build('youtube','v3',developerKey=youtube_api_key)
#             request = youtube.search().list(
#                     part="id,snippet",
#                     type='video',
#                     q=current_name,
#                     videoDuration='short',
#                     videoDefinition='high',
#                     maxResults=3,
#                     fields="nextPageToken,items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
#             )
#             response = request.execute()
#             s=""
#             if(response['items']):
#                 for i in response['items']:
#                     s+='\nhttps://www.youtube.com/watch?v='+str(i['id']['videoId'])
#             else:
#                 s="Not Found"
#         except:
#             s="Not found"
#         dispatcher.utter_message(text=s)

#         return []

class ActionShowVideos(Action):

    def name(self) -> Text:
        return "action_show_media"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            message = tracker.latest_message.get('text')
            tweets = api.search_tweets(message,lang='en', count=3,result_type="recent",tweet_mode="extended")
        # store the API responses in a list
        # tweets_copy = []
        # for tweet in tweets:
        #     tweets_copy.append(tweet)
            s=""
            for i in tweets:
                s+="\nhttps://twitter.com/twitter/statuses/"+str(i.id)
                # print(i.full_text)
                # print("-" * 15)
            youtube_api_key = 'AIzaSyCB0RoVJ0ml1cpUbM6GBePuxw8oUYA4Llk'

            youtube = build('youtube','v3',developerKey=youtube_api_key)
            request = youtube.search().list(
                    part="id,snippet",
                    type='video',
                    q=message,
                    # videoDuration='short',
                    # videoDefinition='high',
                    maxResults=3#,
                    #fields="nextPageToken,items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
            )
            response = request.execute()

            for i in response['items']:
                s+='\nhttps://www.youtube.com/watch?v='+str(i['id']['videoId'])

        except:
            s="Not found"
        dispatcher.utter_message(text=s)

        return []
    
ALLOWED_MEDIA_SIZES = [1,2,3,4,5,6,7,8,9,10]
ALLOWED_MEDIA_TYPES = ["youtube", "twitter","tweets","tweet","videos","video"]

class ValidateSimpleMediaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_media_form"

    def validate_media_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `media_size` value."""
        # print(slot_value,type(slot_value))
        # print(type(ALLOWED_MEDIA_SIZES),type(ALLOWED_MEDIA_SIZES[0]))
        # print(type(int(slot_value)))
        # print(int(slot_value) not in ALLOWED_MEDIA_SIZES)
        # print(ALLOWED_MEDIA_SIZES)
        if int(slot_value) not in ALLOWED_MEDIA_SIZES:
            dispatcher.utter_message(text=f"We only accept only numbers between 1 to 10.")
            return {"media_size": None}
        dispatcher.utter_message(text=f"OK! You want to have a {slot_value} posts.")
        return {"media_size": slot_value}

    def validate_media_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `media_type` value."""
        #print(slot_value)
        if slot_value.lower() not in ALLOWED_MEDIA_TYPES:
            dispatcher.utter_message(text=f"I don't recognize that media. We have {'/'.join(ALLOWED_MEDIA_TYPES)}.")
            return {"media_type": None}
        dispatcher.utter_message(text=f"OK! You want to have posts from {slot_value.lower()}.")
        return {"media_type": slot_value.lower()}

    def validate_media_text(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `media_text` value."""
        #print(slot_value)
        dispatcher.utter_message(text=f"OK! You want I will get posts from {slot_value}.")
        return {"media_text": slot_value}

class ActionShowVideos(Action):

    def name(self) -> Text:
        return "action_show_posts"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        s=""
        media_type = tracker.get_slot('media_type')
        media_text = tracker.get_slot('media_text')
        media_size = tracker.get_slot('media_size')
        try:

            #print(media_type,media_text,media_size)
            if(media_type=='twitter' or media_type=='tweet' or media_type=='tweets'):
                message = media_text
                tweets = api.search_tweets(message,lang='en', count=int(media_size),result_type="recent",tweet_mode="extended")
            # store the API responses in a list
            # tweets_copy = []
            # for tweet in tweets:
            #     tweets_copy.append(tweet)
                #print(tweets)

                for i in tweets:
                    s+="\nhttps://twitter.com/twitter/statuses/"+str(i.id)
                    # print(i.full_text)
                    # print("-" * 15)

            if(media_type=='youtube' or media_type=='videos' or media_type=='video'):

                youtube_api_key = 'AIzaSyCB0RoVJ0ml1cpUbM6GBePuxw8oUYA4Llk'

                youtube = build('youtube','v3',developerKey=youtube_api_key)
                request = youtube.search().list(
                        part="id,snippet",
                        type='video',
                        q=media_text,
                        # videoDuration='short',
                        # videoDefinition='high',
                        maxResults=int(media_size)#,
                        # fields="nextPageToken,items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
                )
                response = request.execute()
                #print(response)
                for i in response['items']:
                    s+='\nhttps://www.youtube.com/watch?v='+str(i['id']['videoId'])

        except:
            s="Not found"
        dispatcher.utter_message(text=s)
        DataUpdate(media_size,media_type,media_text)

        return []

class action_show_search(Action):

    def name(self) -> Text:
        return "action_show_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        s=SearchHistory()
        dispatcher.utter_message(text=s)

        return []

class action_delete_search(Action):

    def name(self) -> Text:
        return "action_delete_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        s=DeleteHistory()
        dispatcher.utter_message(text=s)

        return []
# ALLOWED_FEEDBACK_VALUES = [1,2,3,4,5]
# class ValidateSimpleFeedbackForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_simple_feedback_form"

#     def validate_feedback_rating(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `feedback_rating` value."""

#         if int(slot_value) not in ALLOWED_FEEDBACK_VALUES:
#             dispatcher.utter_message(text=f"We only accept only numbers between 1 to 5.")
#             return {"media_size": None}
#         if(slot_value>=3):
#             dispatcher.utter_message(text=f"Thank you for {slot_value} stars.")
#         else:
#             dispatcher.utter_message(text=f"Sorry for the bad experience")

#         return {"media_size": slot_value}

#     def validate_feedback_text(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `feedback_text` value."""
#         #print(slot_value)
#         dispatcher.utter_message(text=f"FEEDBACK: {slot_value}.")
#         return {"media_text": slot_value}
