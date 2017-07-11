import json

def morepackages(recipient_id):
  return json.dumps({
          "recipient": {
              "id": recipient_id
          },
        "message": {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "list",
                "elements": [
                    {
                        "title": "3 X Face or Neck Treatment",
                        "image_url": "https://sculptbf-bot.herokuapp.com/static/3xfaceneck.png",
                        "subtitle": "Price: $1800... includes: 6 Syringes of Restylane Skin Booster or Redensity (I) with Vital Injection, 3 x LED Therapy, Can add Pelleve Face OR Neck Lift & Tightening only $150 per Session",
                        "buttons": [
                            {
                                "type": "web_url",
                                "title": "Email Now",
                                "url": "https://sculptbf.co.nz/index.php/contact-us/",
                                "webview_height_ratio": "tall"
                            }
                        ]            
                    }
                  ],
                 "buttons": [
                    {
                        "title": "Go Back",
                        "type": "postback",
                        "payload": "GET_STARTED_PAYLOAD"
                    }
                ]  
            }
        }
    }
 })

