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
                "text": "Select from following available menu!!!\n",
                "buttons":[
                  {
                    "type":"postback",
                    "title":"Services",
                    "payload":"SERVICES"
                  },
                  {
                    "type":"postback",
                    "title":"Specials",
                    "payload":"SPECIAL"
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