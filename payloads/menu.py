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
                    "type":"web_url",
                    "title":"Clinic Special",
                    "url":"http://sculptbf.co.nz/index.php/clinic-special/"
                  },
                  {
                    "type":"web_url",
                    "title":"Services",
                    "url":"http://sculptbf.co.nz/index.php/our-prices-offers"
                  }
                ]
              }
            }
          }
      })