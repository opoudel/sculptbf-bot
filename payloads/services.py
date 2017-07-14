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
                    "elements": [
                        {
                            "title": "Our professional services are highly appretiatedcustomers",
                            "subtitle": "Choose service you like",
                            "image_url":"https://sculptbf-bot.herokuapp.com/static/beauty.png",
                            "default_action": {
                                "type": "web_url",
                                "url": "http://sculptbf.co.nz/index.php/our-services/",
                                "webview_height_ratio": "tall"
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "View",
                                    "url": "http://sculptbf.co.nz/index.php/our-services/",
                                    "webview_height_ratio": "tall"
                                }
                            ]
                        },
                        {
                            "title": "Botox, Dysport and Xeomin",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/botox.png",
                            "subtitle": "Kiss those wrinkles goodbye",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "http://sculptbf.co.nz/index.php/botox-fillers/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Dermal Fillers",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/dermal.png",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "https://sculptbf.co.nz/index.php/dermal-filler/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Skin Hydration",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/screen_hydration.png",
                            "subtitle": " ",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "https://sculptbf.co.nz/index.php/skin-hydration/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        }                    
                    ],
                    "buttons": [
                        {
                            "title": "View More",
                            "type": "postback",
                            "payload": "MORE_SERVICES_1"                        
                        }
                    ]  
                }
            }
        }
     })

