# imports
import pandas as pd
import numpy as np
import pickle
import time, datetime
import re
import pickle

from datetime import timedelta
from twitterscraper import query_tweets
from flask import Flask, request, Response, render_template, jsonify
from twitterscraper import query_tweets
from nltk.tokenize import RegexpTokenizer
# initialize the flask app
app = Flask('myApp')

@app.route('/form')
def form():
   return render_template('form.html')

# define the route
@app.route('/submit')
def submit():
    select = request.args["state_select"]#form('state_select')# )

    #scraper function
    def scrape_twitter(place):
        # set empty lists that we will fill with tweet data
        text = []
        # scrape twitter for tweets containing certain keywords
        query_string = f'"power outage" OR "power is out" OR "power\'s out" OR "blackouts" OR "blackout" -"video game" OR "power failure" OR "power failures" OR "no electricity" OR "power shortage" OR "electrical failure" OR "power loss" OR "power cuts" OR "power cut" OR "power went out" OR "power interuption" OR "brownout" OR "power goes out" OR "brownouts" OR "without power" near:"{place}" within:15mi -filter:retweets'
        list_of_tweets = query_tweets(query_string,
                                      begindate = datetime.datetime.today().date(),
                                      enddate = datetime.datetime.today().date() + timedelta(days=1),
                                      poolsize = 2,
                                      lang="en")
        # loop through each tweet to grab data and append the data to their respective lists
        for tweet in list_of_tweets:
            text.append(tweet.text)

        # build the dataframe
        df = pd.DataFrame({
            'tweet': text,
        })

        # remove any twitter pic urls
        df['tweet'] = [re.sub(r'pic.twitter.com\S+', '', post).strip() for post in df['tweet']]
        # remove any http urls
        df['tweet'] = [re.sub(r'http\S+', '', post).strip() for post in df['tweet']]

        # instatiate the tokenizer
        tknr = RegexpTokenizer(r'[a-zA-Z&0-9]+')
        # start with empty lists
        tokens = []
        # fill the list with tokenized versions of each post title
        for post in df['tweet']:
            tokens.append(" ".join(tknr.tokenize(post.lower())))
        df['tweet'] = tokens

        # drop duplicates
        #df = df.drop_duplicates()

        return df['tweet']

    def avg_prob(some_array):
        counter = 0
        for i in some_array:
            counter += i[1]
        return counter/len(some_array)

    data = scrape_twitter(select)
    model = pickle.load(open('./final_model.p', 'rb'))
    prediction = round(avg_prob(model.predict_proba(data))*100,2)
    time_now = datetime.datetime.now()
    return render_template('results.html', prediction= prediction, state=select, time=time_now)

# run the app
if __name__ == '__main__':
    app.run(debug=True)
