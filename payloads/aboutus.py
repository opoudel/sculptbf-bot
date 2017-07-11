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
                    "subtitle":"We are located at: Unit D,248 Marua Road, Mount Wellington,1051 Auckland.",
                    "buttons":[
                      {
                        "type":"web_url",
                        "title":"Our Services",
                        "subtitle": "Go online for detail...",
                        "url":"http://sculptbf.co.nz/index.php/our-prices-offers"
                      },
                      {
                        "type":"postback",
                        "payload":"VIEW_PACKAGES_PAYLOAD",
                        "title": "Packages & Deals"
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
