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
                            "title": "Eyelash Growth",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/eyelash.png",
                            "subtitle":"Enhance the look of luxurious eyelashes and brow hair",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "http://sculptbf.co.nz/index.php/eyelash-growth/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Hair Growth",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/hair-growth.png",
                            "subtitle":"Our multi modalities approach, combat hair thinning",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "http://sculptbf.co.nz/index.php/hair-growth/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Haircut",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/haircut.png",
                            "subtitle":"We provide affordable haircut",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "https://sculptbf.co.nz/index.php/haircut/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        }                    
                    ],
                    "buttons": [
                        {
                            "title": "View More",
                            "type": "postback",
                            "payload": "MORE_SERVICES_6"                        
                        }
                    ]  
                }
            }
        }
     })

