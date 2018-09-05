import json
import requests

# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
webhook_url = 'https://hooks.slack.com/services/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'
slack_data = {"text": "<https://rfgricoh.sharepoint.com/sites/ZJS_ZJA_OFFICE/Lists/Information/Attachments/599/13F%E3%80%80%EF%BD%B3%EF%BD%A8%EF%BD%B0%EF%BD%B8%EF%BE%98%EF%BD%B0%EF%BE%92%EF%BE%86%EF%BD%AD%EF%BD%B09.3.xlsx|【横浜仲町台】防災訓練実施について>"}

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
)
