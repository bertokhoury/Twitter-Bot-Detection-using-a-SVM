#This program uses a Support Vector Machine (SVM) to train a model on two
#datasets
# a bot and a human dataset
#

#packages/functions to import
import pandas as pd
import numpy as np
import matplotlib.pyplot as pp

from sklearn import svm
from sklearn import metrics
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

from plotnine import *
#from ggplot import *

#read in CSV data of genuine Twitter users
read_in_genuine = pd.read_csv("humans.100k.csv", encoding = "latin")

#read in CSV data of fake Twitter Account Users
read_in_fake = pd.read_csv("bots.100k.csv", encoding = "latin")

#create array of rows from the CSV data for genuine users
genuine = read_in_genuine[['screen_name','user_tweeted','user_retweeted', 'user_favourited','user_replied','likes_per_tweet','retweets_per_tweet', 'lists_per_user','follower_friend_ratio','tweet_frequency','favourite_tweet_ratio','age_of_account_in_days','sources_count','urls_count','cdn_content_in_kb','source_identity']]

#create array of rows from the CSV data for fake users
fake = read_in_fake[['screen_name','user_tweeted','user_retweeted', 'user_favourited','user_replied','likes_per_tweet','retweets_per_tweet', 'lists_per_user','follower_friend_ratio','tweet_frequency','favourite_tweet_ratio','age_of_account_in_days','sources_count','urls_count','cdn_content_in_kb','source_identity']]

#combine two objects
combined_dataset = pd.concat([genuine, fake])

#normalize labels
le = preprocessing.LabelEncoder()
le.fit_transform(combined_dataset['screen_name','user_tweeted','user_retweeted', 'user_favourited','user_replied','likes_per_tweet','retweets_per_tweet', 'lists_per_user','follower_friend_ratio','tweet_frequency','favourite_tweet_ratio','age_of_account_in_days','sources_count','urls_count','cdn_content_in_kb','source_identity'])
#combined_dataset.screen_name = le.transform(combined_dataset.screen_name)
#le.fit_transform(combined_dataset.user_tweeted)
#le.fit_transform(combined_dataset.user_retweeted)
#le.fit_transform(combined_dataset.user_favourited)
#le.fit_transform(combined_dataset.user_replied)
#le.fit_transform(combined_dataset.likes_per_tweet)
#le.fit_transform(combined_dataset.retweets_per_tweet)
#le.fit_transform(combined_dataset.lists_per_user)
#le.fit_transform(combined_dataset.follower_friend_ratio)
#le.fit_transform(combined_dataset.tweet_frequency)
#le.fit_transform(combined_dataset.favourite_tweet_ratio)
#le.fit_transform(combined_dataset.age_of_account_in_days)
#le.fit_transform(combined_dataset.sources_count)
#le.fit_transform(combined_dataset.urls_count)
#le.fit_transform(combined_dataset.cdn_content_in_kb)
#le.fit_transform(combined_dataset.source_identity)

#train via the joined dataset
train_specifications = combined_dataset[['screen_name','user_tweeted','user_retweeted', 'user_favourited','user_replied','likes_per_tweet','retweets_per_tweet', 'lists_per_user','follower_friend_ratio','tweet_frequency','favourite_tweet_ratio','age_of_account_in_days','sources_count','urls_count','cdn_content_in_kb','source_identity']]
train_distinction = combined_dataset.values



X_train, X_test, y_train, y_test = train_test_split(train_specifications,train_distinction, test_size=.75,random_state=0)


#use C-Support Vector Classification

svc_object= svm.SVC()
#svc_object_float = pd.to_numeric(svc_object)
svc_object.fit(X_train, y_train)

#use a Multinomial Naive Bayes classifier
mnb_object = MultinomialNB()
mnb_object.fit(X_train, y_train)


#predict for y
y_prediction = svc_object.predict(X_test)
fpr, tpr, _ = metrics.roc_curve(y_test, y_prediction)

#create dataframe + rate of change
dataframe_roc = pd.DataFrame(dict(fpr=fpr, tpr=tpr))
gg = ggplot(dataframe_roc, aes(x='fpr', y='tpr')) + geom_line() + geom_abline(linetype='dashed')
print(gg)

y_prediction = mnb_object.predict(X_test)
fpr, tpr, _ = metrics.roc_curve(y_test, y_prediction)

dataframe_roc = pd.DataFrame(dict(fpr=fpr, tpr=tpr))
gg = ggplot(dataframe_roc, aes(x='fpr', y='tpr')) + geom_line() + geom_abline(linetype='dashed')
print(gg)

















