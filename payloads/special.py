import json

def special(recipient_id):
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
                            "title": "Winter Special 2017",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/snow-man.png",
                            "subtitle": "Contour your body and rejuvenate the skin before this Christmas!",
                            "default_action": {
                                "type": "web_url",
                                "url": "http://sculptbf.co.nz/index.php/clinic-special/",
                                "webview_height_ratio": "tall"
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "View",
                                    "url": "http://sculptbf.co.nz/index.php/clinic-special/",
                                    "webview_height_ratio": "tall"
                                }
                            ]
                        },
                        {
                            "title": "Emerge treatment just $500 for 3 session",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/emerge.png",
                            "subtitle": u"EMERGE™ Fractional Laser is the \nlatest laser skin resurfacing technology",
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
                            "title": "Pellevé: Put a fresh face forward",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/pelleve1.png",
                            "subtitle": "Periorbital $150 \n Face $500 \nboth 3 sessions ",
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

