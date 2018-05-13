## Slack-Export-2-Anki
A script for converting large numbers of formatted text messages in slack into a CSV for import into Anki, a flash card program, for review.

Format of an example message as it appears in Slack:
> **Diastolic heart failure**: presents as normal left ventricular ejection fraction, with increased LV filling pressures


JSON format from Slack export:
 
    {
        "type": "message",
        "user": "U70RRJK02",
        "text": "\*Diastolic heart failure*: presents as normal left ventricular ejection fraction, with increased LV filling pressures",
        "ts": "1523469868.000343"    
    },
    

CSV output:

| First Field  | Second Field |
| ------------- | ------------- |
| Diastolic heart failure  | presents as normal left ventricular ejection fraction, with increased LV filling pressures  |
