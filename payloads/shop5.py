import json

def shop(recipient_id):
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
                            "title": "Cosmedix Clarity Serum",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/clarity.png",
                            "subtitle": "Price: $60",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/cosmedix-clarity-serum/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Aspect Dr. SMC Cream",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/aspect.png",
                            "subtitle": "Price: $80",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/aspect-dr-smc-cream/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Color Science Press Mineral Powder",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/color.png",
                            "subtitle": "Price: $80",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/color-science-press-mineral-powder-foundation/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Sierra Bees Lip Balm",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/bees.png",
                            "subtitle": "Price: $5",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/sierra-bees-lip-balm/",
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

