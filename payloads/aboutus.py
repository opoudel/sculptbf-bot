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
                    "subtitle":"We are located at: Unit D,248 Marua Road, Mount Wellington,1051 Auckland"
                    "url":"http://www.sculptbf.co.nz"
                  },
                  "buttons":[
                    {
                      "type":"phone_number",
                      "payload":"+18576360350",
                      "title": "Call"
                    }
                  ]
                ]
              }
            }
          }
      })
