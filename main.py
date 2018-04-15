import json
import csv
import os

# settings
output_csv = open('output.csv', 'w', newline='')
source_directory = r'C:\Users\Brian\Documents\GitHub\Slack-Export-2-Anki\Messages'


# Convert default json text field into front and and back, based on delimiter in slack message
def parse_slack_text(input_text, csv_delimiter):
    output_dictionary = {}
    if csv_delimiter in input_text:
        # due to there being multiple usages of the default delimiter, ':'
        parsed = message['text'].replace(csv_delimiter, "|", 1)  # first find only

        # remove bold formatting from first bolded set of words
        parsed = parsed.replace("*", "", 2)

        # replace html specific quirks
        parsed = parsed.replace("&lt;", "<")
        parsed = parsed.replace("&gt;", ">")

        # split into dictionary value
        parsed = parsed.split('|')
        output_dictionary["back"] = parsed[0]
        output_dictionary["front"] = parsed[1]
        print(parsed)
    else:
        # if no delimiter in message, just map entire text to back
        output_dictionary["back"] = message['text']
        output_dictionary["front"] = 'Empty'
    return output_dictionary


# Write to CSV
def write_to_csv(data_in, csv_out):
    with csv_out as output_file:
        keys = data_in[0].keys()
        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writerows(data_in)
        csv_out.close()
    return

# Main method
files = os.listdir(source_directory)
parsed_list = []    # To store parsed text across files

for file in files:
    current_path = os.path.join(source_directory, file)
    current_slack_file = json.load(open(current_path))

    for message in current_slack_file:
        parsed_list.append(parse_slack_text(message['text'], ':'))

write_to_csv(parsed_list, output_csv)
