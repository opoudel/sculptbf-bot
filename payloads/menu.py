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
                "text": "Select from available menu where you want to go from here?\n",
                "buttons":[
                  {
                    "type":"postback",
                    "title": "About Us",
                    "payload":"ABOUT_US_PAYLOAD"
                  },
                  {
                    "type":"postback",
                    "title": "Packages",
                    "payload":"VIEW_PACKAGES_PAYLOAD"
                  },
                  {
                    "type":"postback",
                    "title": "Shop",
                    "payload":"SHOP_PAYLOAD"
                  },
                  {
                    "type":"phone_number",
                    "payload":"+64095250911",
                    "title": "Call Clinician"
                  }
                ]
              }
            }
          }
      })