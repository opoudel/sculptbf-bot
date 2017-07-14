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
                            "title": "Lytera Brightening Complex",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/lytera.png",
                            "subtitle": "Price: $198",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/lytera-brightening-complex/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Skin Medica Retinol Complex 0.5",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/retinol.png",
                            "subtitle": "Price: $108",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/skin-medica-retinol-complex-0-5/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Skin Medica TNS Eye Repair Cream",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/tns.png",
                            "subtitle": "Price: $150",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/skin-medica-tns-eye-repair-cream/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Skin Medica Moistuizer with SPF 30+",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/moistarizer.png",
                            "subtitle": "Price: $65",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/skin-medica-moisturizer-with-spf-30/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        }                    
                    ],
                    "buttons": [
                        {
                            "title": "View More",
                            "type": "postback",
                            "payload": "MORE_SHOPPING_4"                        
                        }
                    ]  
                }
            }
        }
     })

