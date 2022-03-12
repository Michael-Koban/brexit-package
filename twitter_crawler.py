import requests
import os
import json
import pandas as pd
import csv , datetime, unicodedata, time, datetime, tweeterid #dateutil.parserm, 


class TwitterCrawler():
    """Summary of class here.

    You must define a TwitterCrawler instance to start crawling Twitter Data.
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """ 
     
    def __init__(self, bearer_token: str):
        """Inits SampleClass with blah."""
        self.bearer_token = bearer_token
        os.environ['TOKEN'] = self.bearer_token
        self.headers = {"Authorization": "Bearer {}".format(self.bearer_token)}

    def auth():
     return os.getenv('TOKEN')

    # def create_headers(self):
    #     """ Creates a header for the Twitter API request,
    #      based on the Bearer Token

    #     Parameters
    #     ----------
    #     sound : str, optional
    #         The sound the animal makes (default is None)

    #     Raises
    #     ------
    #     NotImplementedError
    #         If no sound is set for the animal or passed in as a
    #         parameter.
    #     """

    #     headers = {"Authorization": "Bearer {}".format(self.bearer_token)}
    #     return headers

    def __connect_to_endpoint(self, url, params, next_token = None, verbose = True):
        """ Connect to Twitter API via a endpoint

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        params['next_token'] = next_token   #params object received from create_url function
        response = requests.request("GET", url, headers = self.headers, params = params)
        if verbose == True:
            print("Endpoint Response Code: " + str(response.status_code))
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()
    
    def get_url_by_tweet_id(tweet_id):
        return "https://twitter.com/anyuser/status/" + str(tweet_id)

    
    def create_url_tweet_id(self, tweet_id):
    
        search_url = "https://api.twitter.com/2/tweets/:id"
        search_url = search_url.replace(":id", tweet_id)
        #change params based on the endpoint you are using
        query_params = {
                        'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                        'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                        'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                        'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                        'next_token': {}}
        json_response = self.__connect_to_endpoint(url = search_url, params = query_params)
        return json_response
        
        #search url for idtweet - App rate limit: 300 requests per 15-minute window shared among all users of your app
        #User rate limit (OAuth 1.0a): 900 requests per 15-minute window per each authenticated user
        headers = create_headers(os.environ['TOKEN'])
        search_url = "https://api.twitter.com/2/tweets/:id" #Change to the endpoint you want to collect data from
        tweet_id = "1470753200311517189" #"1108157488581562373"
        ###-------------------------------------------------------------------------------------
        search_url, query_params = create_url_tweet_id(search_url, tweet_id)
        json_response = connect_to_endpoint(search_url, headers, query_params) #new


    
