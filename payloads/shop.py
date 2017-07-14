# -*- coding: utf-8 -*-
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
                    "elements": [
                        {
                            "title": "Skin care products are highly discounted...",
                            "subtitle": "Review products you can purchase from us",
                            "image_url":"https://sculptbf-bot.herokuapp.com/static/beauty.png",
                            "default_action": {
                                "type": "web_url",
                                "url": "http://sculptbf.co.nz/index.php/shop/",
                                "webview_height_ratio": "full"
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "View",
                                    "url": "http://sculptbf.co.nz/index.php/shop/",
                                    "webview_height_ratio": "full"
                                }
                            ]
                        },
                        {
                            "title": "Oxygenetix Oxygenating Foundation or Moisturizer",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/oxygenetex.png",
                            "subtitle": "Price: $110",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/oxygenetix-oxygenating-foundation-or-moisturizer/",
                                    "webview_height_ratio": "full"
                                }
                            ]                
                        },
                        {
                            "title": "Home Roller",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/home_roller.png",
                            "subtitle": "Price: $30",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/home-roller/",
                                    "webview_height_ratio": "full"
                                }
                            ]                
                        },
                        {
                            "title": "Compression stocking -Class A",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/compression_stocking.png",
                            "subtitle": "Price: $45",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/below-knee-medical-stocking-class-a/",
                                    "webview_height_ratio": "full"
                                }
                            ]                
                        }                    
                    ],
                    "buttons": [
                        {
                            "title": "View More",
                            "type": "postback",
                            "payload": "MORE_SHOPPING_1"                        
                        }
                    ]  
                }
            }
        }
     })

