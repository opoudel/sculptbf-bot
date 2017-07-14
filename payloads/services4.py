import json

def services4(recipient_id):
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
                        }
                    ]  
                }
            }
        }
     })

