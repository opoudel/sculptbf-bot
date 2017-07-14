import json

def aboutus(recipient_id):
  return json.dumps({
          "recipient": {
              "id": recipient_id
          },
          "message": {
            "attachment": {
              "type": "template",
              "payload": {
                "template_type": "generic",
                "elements":[
                  {
                    "title":"Welcome to Body & Face Clinic",
                    "image_url":"https://sculptbf-bot.herokuapp.com/static/makeup-brush.png",
                    "subtitle":"We are located at: Unit D,248 Marua Road,\nMount Wellington,\n1051 Auckland.",
                    "buttons":[
                      {
                        "type":"phone_number",
                        "title":"Call Expert",
                        "payload": "+645250911"
                      },
                      {
                        "type":"postback",
                        "title": "Special",
                        "payload":"SPECIAL"
                      },
                      {
                        "type":"postback",
                        "payload":"GET_STARTED_PAYLOAD",
                        "title": "Go back"
                      }                                    
                    ]
                  }
                ]
              }
            }
          }
      })
