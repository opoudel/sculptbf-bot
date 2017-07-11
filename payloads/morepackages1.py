import json

def morepackages(recipient_id):
  return json.dumps({
          "recipient": {
              "id": recipient_id
          },
        "message": {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "list",
                "top_element_style": "compact",
                    "elements": [
                        {
                            "title": "ER Glass Fractional Laser ($2000 only)",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/ERGlass.png",
                            "subtitle": "Includes: \n\t2 Er. Fractional Laser, \n\tRestylane skin booster or Redensity (I)",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Email Now",
                                    "url": "http://sculptbf.co.nz/index.php/contact-us/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Malesma & Pigmentation ($1500 only)",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/MalesPigmt.png",
                            "subtitle": "Includes: \n\t3 Q-switch laser, \n\t1 Restylane skin booster or Redensity (I) and 1 LED treatment, \n\t1 home care products",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Email Now",
                                    "url": "http://sculptbf.co.nz/index.php/contact-us/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        }                 
                    ],
                 "buttons": [
                    {
                        "title": "Go Back",
                        "type": "postback",
                        "payload": "GET_STARTED_PAYLOAD"
                    }
                ]  
            }
        }
    }
 })

