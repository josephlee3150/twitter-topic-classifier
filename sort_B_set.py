import csv

line_counter = 0
#
# with open ('B_training_set.csv', 'r') as B_set, open ('training_data_B.csv', 'w') as training_data_B:
#     fieldnames = ['Tweeter','Tweet ID','Tweet Time','Tweet Text','Topics']
#     csvReader = csv.DictReader(B_set)
#     csvWriter = csv.DictWriter(training_data_B, fieldnames=fieldnames)
#     csvWriter.writeheader()
#     for line in csvReader:
#         if line_counter < 367:
#             csvWriter.writerow({'Tweeter': line['Tweeter'], 'Tweet ID': line['Tweet ID'], 'Tweet Time': line['Tweet Time'], 'Tweet Text': line['Tweet Text'], 'Topics': line['Topics']})
#         line_counter += 1

# with open ('B_training_set.csv', 'r') as B_set, open ('testing_data_B.csv', 'w') as testing_data_B:
#     fieldnames = ['Tweeter', 'Tweet ID', 'Tweet Time', 'Tweet Text', 'Topics']
#     csvReader = csv.DictReader(B_set)
#     csvWriter = csv.DictWriter(testing_data_B, fieldnames=fieldnames)
#     csvWriter.writeheader()
#     for line in csvReader:
#         if line_counter >= 367 and line_counter < 413:
#             csvWriter.writerow({'Tweeter': line['Tweeter'], 'Tweet ID': line['Tweet ID'], 'Tweet Time': line['Tweet Time'], 'Tweet Text': line['Tweet Text'], 'Topics': line['Topics']})
#         line_counter += 1

with open ('B_training_set.csv', 'r') as B_set, open ('training_data_B.csv', 'w') as training_data_B:
    fieldnames = ['Tweeter', 'Tweet ID', 'Tweet Time', 'Tweet Text', 'Topics']
    csvReader = csv.DictReader(B_set)
    csvWriter = csv.DictWriter(training_data_B, fieldnames=fieldnames)
    csvWriter.writeheader()
    for line in csvReader:
        if line_counter >= 413 and line_counter < 459:
            csvWriter.writerow({'Tweeter': line['Tweeter'], 'Tweet ID': line['Tweet ID'], 'Tweet Time': line['Tweet Time'], 'Tweet Text': line['Tweet Text'], 'Topics': line['Topics']})
        line_counter += 1

# with open ('B_training_set.csv', 'r') as B_set:
#     csvReader = csv.DictReader(B_set)
#     for line in csvReader:
#         line_counter += 1
print(line_counter)


# PRIORITY
# put together the presentation
    # talk about intuition (problems in data)
    # what graph would show this intuition
    # look at the examples where there's a lot of disagreement
    # compare annotations (where do they disagree the most, where's the source of the disagreement)
