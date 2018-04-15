import json
import csv
import os

# settings
output_csv = open('output.csv', 'w')
source_directory = r'C:\Users\Brian\Documents\GitHub\Slack-Export-2-Anki\Messages'


# Convert default json text field into front and and back, based on delimiter in slack message
def parse_slack_text(input_text, csv_delimiter):
    output_dict = {}
    if csv_delimiter in input_text:
        # due to there being multiple usages of the default delimiter, ':'
        parsed = item['text'].replace(csv_delimiter, "|", 1)  # first find only

        # remove bold formatting from first bolded set of words
        parsed = parsed.replace("*", "", 2)

        # replace html specific quirks
        parsed = parsed.replace("&lt;", "<")
        parsed = parsed.replace("&gt;", ">")

        # split into dictionary value
        parsed = parsed.split('|')
        output_dict["back"] = parsed[0]
        output_dict["front"] = parsed[1]
        print(parsed)
    else:
        # if no delimiter, just map entire text to back
        output_dict["back"] = item['text']
        output_dict["front"] = 'Empty'
    return output_dict


# Travel through directory
files = os.listdir(source_directory)

# Declare a list to store parsed text
output_list = []

for file in files:
    current_path = os.path.join(source_directory, file)
    data = json.load(open(current_path))

    for item in data:
        output_list.append(parse_slack_text(item['text'], ':'))


# write to CSV
with open('output.csv', 'w', newline='') as output_file:
    keys = output_list[0].keys()
    writer = csv.DictWriter(output_file, fieldnames=keys)
    writer.writerows(output_list)
    output_csv.close()

