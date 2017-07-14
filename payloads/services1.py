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
                            "title": "Platelet Rich Plasma (PRP)",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/platlet.png",
                            "subtitle": "Kiss those wrinkles goodbye",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "http://sculptbf.co.nz/index.php/platelet-rich-plasma-prp/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "I2pl Facial Rejuvenation",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/l2pl.png",
                            "subtitle": "Kiss those wrinkles goodbye",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "http://sculptbf.co.nz/index.php/facial-rejuvenation/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "LED",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/led.png",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "https://sculptbf.co.nz/index.php/led-light-treatment/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Facial Peel",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/facial_peel.png",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "https://sculptbf.co.nz/index.php/facial-peel/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        }                    
                    ],
                    "buttons": [
                        {
                            "title": "View More",
                            "type": "postback",
                            "payload": "MORE_SERVICES_2"                        
                        }
                    ]  
                }
            }
        }
     })

