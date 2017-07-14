import json

def message(recipient_id):
	return json.dumps({
	        "recipient": {
	            "id": recipient_id
	        },
          "message": {
            "attachment": {
              "type": "template",
              "payload": {
                "template_type": "button",
                "text": "Welcome back to Body & Face Clinic! \nHow can I help you?\n",
                "buttons":[
                  {
                    "type":"postback",
                    "title": "Deals",
                    "payload":"VIEW_PACKAGES_PAYLOAD"
                  },
                  {
                    "type":"postback",
                    "title": "Shop",
                    "payload":"SHOPPING"
                  },
                  {
                    "type":"postback",
                    "payload":"GET_STARTED_PAYLOAD",
                    "title": "Main Menu"
                  }
                ]
              }
            }
          }
   })