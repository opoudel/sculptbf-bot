# -*- coding: utf-8 -*-
import json

def services(recipient_id):
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
                            "title": "Nailcare & Makeup",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/nail_care.png",
                            "subtitle":"Either fungi nails or mackup, we are here for you",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "https://sculptbf.co.nz/index.php/nail-care-2/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },                        
                        {
                            "title": "Eye Dark Circle",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/eye_dark_circle.png",
                            "subtitle":"Redensity [II] an inredensity injectable gel, keeps hydration of skin",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "http://sculptbf.co.nz/index.php/eye-dark-circle/",
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

