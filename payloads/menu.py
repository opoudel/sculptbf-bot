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
                "text": "Select from available menu where you want to go from here?",
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"http://www.sculptbf.co.nz",
                    "title": "Website"
                  },
                  {
                    "type":"postback",
                    "title": "Packages & Deals",
                    "payload":"VIEW_PACKAGES_PAYLOAD"
                  },
                  {
                    "type":"phone_number",
                    "payload":"+18576360526",
                    "title": "Call Representative"
                  }
                ]
              }
            }
          }
      })