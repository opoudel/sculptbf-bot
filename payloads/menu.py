import json

def menu(recipient_id):
  return json.dumps({
          "recipient": {
              "id": recipient_id
          },
          "message": {
            "attachment": {
              "type": "template",
              "payload": {
                "template_type": "button",
                "text": "Tell us where we can take you from here?\n",
                "buttons":[
                  {
                    "type":"postback",
                    "title":"Services",
                    "payload":"SERVICES"
                  },
                  {
                    "type":"postback",
                    "title":"Shop",
                    "payload":"SHOPPING"
                  },
                  {
                    "type":"postback",
                    "title": "About Us",
                    "payload":"ABOUT_US_PAYLOAD"
                  }                  
                ]
              }
            }
          }
      })