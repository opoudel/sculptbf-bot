import json

def services3(recipient_id):
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
                            "title": "Body Fat Reduction",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/body_fat.png",
                            "subtitle": "Kiss those wrinkles goodbye",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "http://sculptbf.co.nz/index.php/body-sculpting/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Cellulite Reduction",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/cellulite.png",
                            "subtitle": "Kiss those wrinkles goodbye",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "http://sculptbf.co.nz/index.php/cellulite-reduction/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Acne & Acne Scar",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/acne.png",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "https://sculptbf.co.nz/index.php/acne-acne-scar/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Malesma/ Pigmentation",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/malesma.png",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "https://sculptbf.co.nz/index.php/malesmapigmentation/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        }                    
                    ],
                    "buttons": [
                        {
                            "title": "View More",
                            "type": "postback",
                            "payload": "MORE_SERVICES_4"                        
                        }
                    ]  
                }
            }
        }
     })

