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
                "template_type": "generic",
                "text": "Welcome back to Body & Face Clinic! \nHow can I help you?\n",
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
                    "type":"postback",
                    "title": "Clinic Special",
                    "payload":"CLINIC_SPECIAL_PAYLOAD"
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