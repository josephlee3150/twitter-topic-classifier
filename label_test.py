import csv
import matplotlib.pyplot as plt
import numpy as np

jonathan_labels = dict()
charlie_labels = dict()
tweets = dict()
with open('jonathan_labels_received.csv', 'r') as jonathan_file:
    csv_reader = csv.DictReader(jonathan_file)

    # Tweeter,Tweet ID,Tweet Time,Tweet Text,Topics.
    for line in csv_reader:
        label_set = set()
        labels = ''
        # obtain labels
        # print(line)
        tweets[line['Tweet ID']] = line['Tweet Text']
        if line['Topics'] == '1339009382147878912':
            print(line['Tweet Text'])
        if line['Topics'] == '':
            labels = ''
        else:
            # print(line['Topics'])
            labels = line['Topics'].strip().replace("“", "\"").replace("”", "\"")

            labels = labels[1:-1].split(', ')

            labels = [l.strip('"') for l in labels]
            labels = [l.lower() for l in labels]
            # print(labels)

        # print(labels)
        jonathan_labels[line['Tweet ID']] = set(labels)

with open('charlie_labels_received.csv', 'r') as jonathan_file:
    csv_reader = csv.DictReader(jonathan_file)

    # Tweeter,Tweet ID,Tweet Time,Tweet Text,Topics.
    for line in csv_reader:
        label_set = set()
        labels = ''
        # obtain labels
        # print(line)

        if line['Topics'] == '':
            labels = ''
        else:
            # print(line['Topics'])
            labels = line['Topics'].strip().replace("“", "\"").replace("”", "\"")
            labels = labels.split(', ')
            # print(labels)

        charlie_labels[line['Tweet ID']] = set(labels)


some_label_matches = 0
everything_matches = 0
nothing_matches = 0
proportion = 0
total = 0
for tweet in jonathan_labels:
    total += 1
    if len(jonathan_labels[tweet].intersection(charlie_labels[tweet])) > 0:
        some_label_matches += 1
    elif len(jonathan_labels[tweet].intersection(charlie_labels[tweet])) == len(jonathan_labels[tweet].union(charlie_labels[tweet])):
        everything_matches += 1
    elif len(jonathan_labels[tweet].intersection(charlie_labels[tweet])) == 0:
        nothing_matches += 1
    proportion += len(jonathan_labels[tweet].intersection(charlie_labels[tweet])) / len(jonathan_labels[tweet].union(charlie_labels[tweet]))
    # print("For tweet", labels, len(jonathan_labels[labels].intersection(charlie_labels[labels])) / len(jonathan_labels[labels].union(charlie_labels[labels])), "of the labels were assigned by both")
    if len(jonathan_labels[tweet].intersection(charlie_labels[tweet])) / len(jonathan_labels[tweet].union(charlie_labels[tweet])) == 0:
        print("TWEET:", tweets[tweet])
        print("JONATHAN'S LABELS", jonathan_labels[tweet])
        print("CHARLIE'S LABELS", charlie_labels[tweet], "\n")


print("Some label matched {}%".format(round((some_label_matches / total) * 100)))
print("Everything matched {}%".format(round((everything_matches / total) * 100)))
print("Nothing matched {}%".format(round((nothing_matches / total) * 100)))
print("On average {}% percent of labels were assigned by both in a single tweet".format(round((proportion / total) * 100)))

label_analysis = dict()
for tweet in jonathan_labels:
    union_set = jonathan_labels[tweet].union(charlie_labels[tweet])
    intersection_set = jonathan_labels[tweet].intersection(charlie_labels[tweet])
    print("UNION", union_set)
    print("INTERSECTION", intersection_set)
    for label in union_set:
        if label not in intersection_set:
            print(label)
            if label not in label_analysis:
                label_analysis[label] = 1
            else:
                label_analysis[label] += 1

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
            # tweet_text.append(result)  # obtain list of Tweet Text
            labels = ''
            # obtain labels
            # print(line)

            if line['Topics'] == '':
                labels = ''
            else:
                # print(line['Topics'])
                labels = line['Topics'].strip().replace("“", "\"").replace("”", "\"")
                # print(label)
                labels = labels[1:-1].split('" "')

            for label in labels:
                if label.lower() not in label_distribution:
                    label = label.lower()
                    label_distribution[label] = 1
                else:
                    label = label.lower()
                    label_distribution[label] += 1

# run on random labels (PRIORITY)
    # at least 100 tweets in test and development sets
# clustering (maybe)
# single graph with two bars (true labels, test labels)
# keep track of counts of how many times charlie and jonathan disagreed
# normalize the counts (divide by largest value)
    # look for patterns in most agreed/disagreed labels

# slides
    # 3 slides (2 minutes)
        # problem, what i did, what i learned
max_val_1 = 0
max_val_2 = 0
for label in label_analysis:
    max_val_1 += label_analysis[label]
    if label in label_distribution:
        max_val_2 += label_distribution[label]

print(max_val_1)
print(max_val_2)

x = []
y = []
z = []
for label in label_analysis:
    x.append(label)

for label in x:
    y.append(label_analysis[label] / max_val_1)
    # if label != "ruth bader ginsburg" and label != "encouragement" and label != "joe biden" and label != "acknowledgment" and label != "healthcare":
    #     z.append(label_distribution[label])
    if label not in label_distribution:
        z.append(0)
    else:
        z.append(label_distribution[label] / max_val_2)

print(len(x), len(y), len(z))
zipped = zip(x, y, z)
zipped = list(zipped)
res = sorted(zipped, key = lambda b: b[2], reverse=True)
x = []
y = []
z = []
for tuple in res:
    x.append(tuple[0])
    y.append(tuple[1])
    z.append(tuple[2])
w=0.4
fig, ax = plt.subplots()
bar1 = np.arange(len(x))
bar2 = [i+w for i in bar1]
plt.barh(bar1, y, w, label="Jonathan-Charlie Labels")
plt.barh(bar2, z, w, label="My Labels")
plt.xlabel("Labels")
plt.ylabel("Ratio of occurrences")
plt.title("Proportion of Disagreed Labels vs. Proportion of Original Labels")
plt.yticks(bar1 + w/2, x, size='medium', rotation='horizontal')
plt.tight_layout()
ax.invert_yaxis()
plt.legend()
plt.show()