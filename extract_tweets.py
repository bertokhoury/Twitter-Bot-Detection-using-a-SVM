
#import libs
import tweepy


#to install using pip -> 'pip install tweepy'
#to install using conda -> 'conda install tweepy'


##To obtain keys
# 1) Login into twitter developer section
# 2) Locate 'Create an App' and fill out the details of the app
# 3) Click 'Create your Twitter Application'
# 4) App details such as consumer_secret and consumer_key will be displayed
# 5) click 'Create my Access Token' ..Page will refresh generating
#       access_key


consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

#Create the function to retrieve tweets
def get_tweets(username) :


    #authorize consumer_key and consumer_secret
    authorize = tweepy.OAuthHandler(consumer_key, consumer_secret)

    #get access to user using access_key and access_secret
    authorize.set_access_token(access_key, access_secret)

    #call API
    tweepy_api = tweepy.API(authorize)

    #count of tweets to retrieve
    extract_count = 100
    tweets = tweepy_api.user_timeline(screen_name = username)

    #create an array of tweet information containing:
        #username, timestamp, text
        #also create the CSV file
    array = []
    tweets_to_csv = [tweet.text for tweet in tweets]

    for j in tweets_to_csv :
        #append array
        array.append(j)

    #Print the tweets
    print("Printing the Tweets \n")
    print(array)

#Testing Code
#Make sure to enter username in to extract the tweets
#
#if __name__ == '__main__':
    #get_tweets(username)








