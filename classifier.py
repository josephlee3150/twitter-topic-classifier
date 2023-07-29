import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
import csv
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

label_distribution = dict()
label_counter = 0
with open ('labeled_tweets.csv', 'r') as csv_file:
    # Tweeter,Tweet ID,Tweet Time,Tweet Text,Topics.
    csv_reader = csv.DictReader(csv_file)

    # obtain Tweet texts
    for line in csv_reader:
        if label_counter < 460:
            label_counter += 1
            # obtain text
            # print(line)
            text = line['Tweet Text']
            # print(text)
            result = re.sub(r"http\S+", "", text)
            # tweet_text.append(result)  # obtain list of Tweet Text
            label = ''
            # obtain labels
            # print(line)

            if line['Topics'] == '':
                label = ''
            else:
                # print(line['Topics'])
                label = line['Topics'].strip().replace("“", "\"").replace("”", "\"")
                # print(label)
                label = label[1:-1].split('" "')


            # print(label)

            if len(label) > 0:
                if label[0] not in label_distribution:
                    label_distribution[label[0]] = 1
                else:
                    label_distribution[label[0]] += 1

            else:
                if '' not in label_distribution:
                    label_distribution[''] = 1
                else:
                    label_distribution[''] += 1

labels = []
frequency = []
for label in label_distribution:
    if label == "olida":
        labels.append("Holiday")
    elif label == "":
        labels.append("Empty Label")
    else:
        labels.append(label)
    frequency.append(label_distribution[label])
zipped = zip(labels, frequency)
zipped = list(zipped)
res = sorted(zipped, key = lambda x: x[1], reverse=True)
print(res)
labels = []
frequency = []
low_label = []
for tuple in res:
    if tuple[1] != 1:
        labels.append(tuple[0])
        frequency.append(tuple[1])
    elif tuple[1] == 1:
        low_label.append(tuple[0])
print(len(labels))
print(frequency)
print(low_label)
plt.rcdefaults()
fig, ax = plt.subplots()
bar1 = np.arange(len(labels))
plt.barh(range(len(frequency)), frequency, align='edge')
plt.yticks(bar1 + 0.9/2, labels, size='large', rotation='horizontal')
plt.tight_layout()
plt.xlabel("Frequency")
plt.ylabel("Labels")
plt.title("Frequencies Of Each Label In Dataset")
ax.invert_yaxis()
# plt.show()
# training_counter = 0

# obtain training data
# with open('labeled_tweets.csv', 'r') as csv_file:
#
#     # Tweeter,Tweet ID,Tweet Time,Tweet Text,Topics.
#     csv_reader = csv.DictReader(csv_file)
#     with open('training_data_A.csv', 'w') as write_csv_file:
#         fieldnames = ['Tweeter', 'Tweet ID', 'Tweet Time', 'Tweet Text', 'Topics']
#         writer = csv.DictWriter(write_csv_file, fieldnames=fieldnames)
#         writer.writeheader()
#
#         for line in csv_reader:
#             if line['Tweet ID'] not in development_id and training_counter < 351:
#                 development_id.add(line['Tweet ID'])
#                 training_counter += 1
#                 writer.writerow({'Tweeter': line['Tweeter'], 'Tweet ID': line['Tweet ID'], 'Tweet Time': line['Tweet Time'], 'Tweet Text': line['Tweet Text'], 'Topics': line['Topics']})



# obtain testing data
# with open('labeled_tweets.csv', 'r') as csv_file:
#     training_counter = 0
#     print("development ID SIZE", len(development_id))
#     # Tweeter,Tweet ID,Tweet Time,Tweet Text,Topics.
#     csv_reader = csv.DictReader(csv_file)
#     with open('testing_data_A.csv', 'w') as write_csv_file1:
#         fieldnames = ['Tweeter', 'Tweet ID', 'Tweet Time', 'Tweet Text', 'Topics']
#         writer1 = csv.DictWriter(write_csv_file1, fieldnames=fieldnames)
#         writer1.writeheader()
#
#         for line in csv_reader:
#             if line['Tweet ID'] not in development_id and training_counter < 45:
#                 development_id.add(line['Tweet ID'])
#                 training_counter += 1
#                 writer1.writerow(
#                     {'Tweeter': line['Tweeter'], 'Tweet ID': line['Tweet ID'], 'Tweet Time': line['Tweet Time'],
#                      'Tweet Text': line['Tweet Text'], 'Topics': line['Topics']})

topic_text_dict = dict()

dev_tweet_text = list()
development_labels = list()
development_id = list()

train_tweet_text = list()
train_labels = list()



counter = 0
# read development_data.csv
with open('development_data_B.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        labels = []
        if line['Topics'] == '':
            labels = ["no label"]
        else:

            labels = line['Topics'].strip().replace("“", "\"").replace("”", "\"")

            labels = labels.split('" "')
            labels = [l.strip('"') for l in labels]

        development_id.append(line['Tweet ID'])
        text = line['Tweet Text']
        result = re.sub(r"http\S+", "", text)

        if labels[0] == "''":
            labels[0] = ''
        # if labels[0] != '':
        #     development_labels.append(labels[0])
        #     dev_tweet_text.append(result)
        development_labels.append(labels[0])
        dev_tweet_text.append(result)


with open ('training_data_B.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        labels = []
        if line['Topics'] == '':
            labels = ["no label"]
        else:

            labels = line['Topics'].strip().replace("“", "\"").replace("”", "\"")

            labels = labels.split('" "')
            labels = [l.strip('"') for l in labels]

        if labels[0] == "''":
            labels[0] = ''
        text = line['Tweet Text']
        result = re.sub(r"http\S+", "", text)


        # if labels[0] != '':
        #     train_labels.append(labels[0])
        #     train_tweet_text.append(result)

        train_labels.append(labels[0])
        train_tweet_text.append(result)

print("Number of labels in development:",len(development_labels))
print("Development label list:", development_labels)
print("Number of development text", len(dev_tweet_text))
print("Number of training tweet text", len(train_tweet_text))
print("Training label list:", train_labels)
print("Percentage of Empty Labels:", label_distribution['']/sum(label_distribution.values()))
print(label_distribution[''], sum(label_distribution.values()))
# label_counter = 0
# text_counter = 0
# # read csv file
# labels = []


# training_counter = 0
# with open('testing_data_A.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         training_counter += 1
#     print("there are", training_counter, "testing data")
#
# training_counter = 0
# with open('training_data_A.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         training_counter += 1
#     print("there are", training_counter, "training data")
#
# training_counter = 0
# with open('development_data_A.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         training_counter += 1
#     print("there are", training_counter, "development data")




le = preprocessing.LabelEncoder()
train_tweet_topic_encoded = le.fit_transform(train_labels) # encode labels in the labels array to numbers
dev_tweet_topic_encoded = le.fit_transform(development_labels)


vectorizer = CountVectorizer(analyzer='word', ngram_range=(1, 4))
train_features = vectorizer.fit_transform(train_tweet_text) # extract features train tweet text
dev_features = vectorizer.transform(dev_tweet_text) # extract features from dev tweet text


clf = MultinomialNB()
clf.fit(train_features, train_tweet_topic_encoded) # fit NB according to features and encoded labels (training, training data) (lectures)

print(clf.predict(dev_features[0:367])) # generate a prediction (practice test, development)
print(clf.score(dev_features[0:367], dev_tweet_topic_encoded[0:367]))


predicted_labels = clf.predict(dev_features[0:367])
np.set_printoptions(threshold=5000)
print(confusion_matrix(dev_tweet_topic_encoded, predicted_labels))
# num_correct = 0
# for row_count, row in enumerate(confusion_matrix(dev_tweet_topic_encoded, predicted_labels)):
#     for col_count, col in row:
#         if row_count == col_count:
#             num_correct += confusion_matrix(dev_tweet_topic_encoded, predicted_labels)[row_count][col]
# #
# for idx, element in enumerate(clf.predict(dev_features[0:63])):
#     if element == 3:
#         print(idx)
#         print(dev_tweet_text[idx])
#         print(development_labels[idx])



# 80% training
# 10% test
# 10% set aside (validation, development)

# confusion matrix
# table
    # each row - one true label
    # each col - predicted label
    # cell - count of how many times a true label was 6 and I predicted 3

# experiment with different structures (training, development, and test) - overfitting
    # does well on training data, may not do well on separate data set
    # test set
    # check scikit learn multinomial nb documentation (regularization)
# confusion matrix, understand what it's getting wrong
# set up data sample for review
# multilabel case
# how many tweets are in certain label

# anything matches
    # intersection larger than 0
# everything matches
    # size of intersection = size of union
# how many labels are in the set
    # given a tweet, take both labels and put them in a set
    # how many did both of Charlie and Jonathan assign
    # size of intersection / size of union

# PRIORITY!!!!
# check distribution of labels
# compare results between Charlie and Jonathan


# gather more random tweets for development data
# ignore or combine labels if i have to
# add own feature,
    # for each label, does this label exist in the tweet