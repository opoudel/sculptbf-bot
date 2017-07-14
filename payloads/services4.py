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
                            "title": "Surgical & Stretch Mark",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/surgical.png",
                            "subtitle":"The treatment has minimal downtime and can be used on any skin type",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "http://sculptbf.co.nz/index.php/surgical-scar-stretch-mark/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Hair Removal",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/hair-removal-2.png",
                            "subtitle":"Get rid of unnecessary hair using square pluse technology",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "http://sculptbf.co.nz/index.php/hair-removal-2/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Mole Check & Removal",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/mole_check.png",
                            "subtitle":"We use Pellevé S5 surgical to remove mole",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "https://sculptbf.co.nz/index.php/mole-check-removal/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Tatoo Removal",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/tatoo_removal.png",
                            "subtitle":"Using Q-Switched YAG laser for tattoo removal have low risk of scarring",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "https://sculptbf.co.nz/index.php/tatoo-removal/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        }                    
                    ],
                    "buttons": [
                        {
                            "title": "View More",
                            "type": "postback",
                            "payload": "MORE_SERVICES_5"                        
                        },
                    {
                        "type":"postback",
                        "payload":"GET_STARTED_PAYLOAD",
                        "title": "Go back"
                    }
                    ]  
                }
            }
        }
     })

