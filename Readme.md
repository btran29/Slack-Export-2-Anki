## Slack-Export-2-Anki
Useful for converting large numbers of text messages in slack into a CSV for import into Anki, a flash card program, for review.

Format of message as it appears in Slack:
> **First Field**:Second Field

> **Diastolic heart failure**:presents as normal left ventricular ejection fraction, with increased LV filling pressures


JSON format from Slack export:
 
>{
        "type": "message",
        "user": "U70RREU02",
        "text": "*Diastolic heart failure*: presents as normal left ventricular ejection fraction, with increased LV filling pressures",
        "ts": "1523469868.000343"
    },
    

CSV output:

| First Field  | Second Field |
| ------------- | ------------- |
| Diastolic heart failure  | presents as normal left ventricular ejection fraction, with increased LV filling pressures  |
