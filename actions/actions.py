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
from googletrans import Translator

import tweepy
from googleapiclient.discovery import build

clientid = "clientid"
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
bearertoken = "bearertoken"
access_token ="access_token"
access_token_secret = "access_token_secret"
bearer_token = "bearer_token"
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


class ActionShowVideos(Action):

    def name(self) -> Text:
        return "action_show_media"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            message = tracker.latest_message.get('text')
            tweets = api.search_tweets(message,lang='en', count=3,result_type="recent",tweet_mode="extended")
            s=""
            for i in tweets:
                s+="\nhttps://twitter.com/twitter/statuses/"+str(i.id)
            DataUpdate(len(tweets),"Twitter",message)

            youtube_api_key = 'youtube_api_key'

            youtube = build('youtube','v3',developerKey=youtube_api_key)
            request = youtube.search().list(
                    part="id,snippet",
                    type='video',
                    q=message,
                    maxResults=3
            )
            response = request.execute()

            for i in response['items']:
                s+='\nhttps://www.youtube.com/watch?v='+str(i['id']['videoId'])
            DataUpdate(len(response['items']),"Youtube",message)
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
            if(media_type=='twitter' or media_type=='tweet' or media_type=='tweets'):
                message = media_text
                tweets = api.search_tweets(message,lang='en', count=int(media_size),result_type="recent",tweet_mode="extended")

                for i in tweets:
                    s+="\nhttps://twitter.com/twitter/statuses/"+str(i.id)
                if(len(tweets)!=int(media_size)):
                    s+="\nSorry didn't find the number of tweets mentioned."

            if(media_type=='youtube' or media_type=='videos' or media_type=='video'):

                youtube_api_key = 'youtube_api_key'

                youtube = build('youtube','v3',developerKey=youtube_api_key)
                request = youtube.search().list(
                        part="id,snippet",
                        type='video',
                        q=media_text,
                        maxResults=int(media_size)
                )
                response = request.execute()
                for i in response['items']:
                    s+='\nhttps://www.youtube.com/watch?v='+str(i['id']['videoId'])
                if(len(response['items'])!=int(media_size)):
                    s+="\nSorry didn't find the number of videos mentioned."

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
