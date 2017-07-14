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
                    "top_element_style": "compact",
                    "elements": [
                        {
                            "title": "Phloe - Bowel Health",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/phloe.png",
                            "subtitle": "Price: $34",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/phloe-bowel-health/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Copper Peptide Shampoo and Conditioner",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/copper.png",
                            "subtitle": "Price: $50",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/copper-peptide-shampoo-and-conditioner/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Body wash - Natural instinct",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/body_wash.png",
                            "subtitle": "Price: $50",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/body-wash-natural-instinct/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Natural Lipsticks - Karen Murell",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/lipstick.png",
                            "subtitle": "Price: $25",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/natural-lipsticks-karen-murell/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        }                    
                    ],
                    "buttons": [
                        {
                            "title": "View More",
                            "type": "postback",
                            "payload": "MORE_SHOPPING_2"                        
                        }
                    ]  
                }
            }
        }
     })

