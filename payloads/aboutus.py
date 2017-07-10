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
                    "image_url":"https://cdn.pixabay.com/photo/2013/07/13/12/50/beauty-160456_1280.png",
                    "subtitle":"We are located at: Unit D,248 Marua Road, Mount Wellington,1051 Auckland",
                    "default_action": {
                      "type":"web_url",
                      "url":"http://sculptbf.co.nz/index.php/our-prices-offers",
                      "webview_height_ratio": "tall",
                      "fallback_url": "http://www.sculptbf.co.nz"
                    },
                  "buttons":[
                    {
                      "type":"phone_number",
                      "payload":"+18576360350",
                      "title": "Call"
                    }
                  ]
                  }
                ]
              }
            }
          }
      })
