import json
import csv

# settings
csv_delimiter = ':'
output_csv = open('output.csv', 'w')
output_list = []

# get path (to be determined by crawler)
current_path = r'C:\Users\Brian\Documents\GitHub\Slack-Export-2-Anki\Slack-Export-2-Anki\2017-09-10.json'
data = json.load(open(current_path))

# replace first ':' with the special delimiter character
for item in data:
    if csv_delimiter in item['text']:
        parsed = item['text'].replace(csv_delimiter, "~", 1)  # first find only
        output_list.append(parsed)
        # print(parsed)
    else:
        output_list.append(item['text'])
        # print(item['text'])

# create data output variable


# write to CSV
with open('output.csv', 'wb'):
    writer = csv.writer(output_csv, delimiter='~', quoting=csv.QUOTE_ALL)
    writer.writerow(output_list)

# TODO: fix writing issue


# TODO: loop over files
for item in data:
    print(item['text'])

