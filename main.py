import json
import csv

# settings
csv_delimiter = ':'
output_csv = open('output.csv', 'w')
output_list = []

# get path (to be determined by crawler)
current_path = r'C:\Users\Brian\OneDrive\Python\cvs_convert\2017-09-10.json'
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
with output_csv:
    writer = csv.writer(output_csv)
    writer.writerows(output_list)

    # TODO: add delimiter to writer


# TODO: loop over files
for item in data:
    print(item['text'])

