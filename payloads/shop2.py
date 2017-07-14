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
                            "title": "Lypo - Spheric Vitamin C",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/lypo.png",
                            "subtitle": "Price: $48",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/lypo-spheric-vit-c/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "ASAP Moisturizer Sun Screen 50+",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/asap.png",
                            "subtitle": "Price: $65",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/asap-moisturizer-sun-screen-50/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Cosmedix Purity Clean",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/cosmedix.png",
                            "subtitle": "Price: Not in Stock!!",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/cosmedix-purity-clean/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Skin Medica TNS Essential Serum",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/skin_medica.png",
                            "subtitle": "Price: $250",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Buy",
                                    "url": "http://sculptbf.co.nz/index.php/product/skin-medica-tns-essential-serum/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        }                    
                    ],
                    "buttons": [
                        {
                            "title": "View More",
                            "type": "postback",
                            "payload": "MORE_SHOPPING_3"                        
                        }
                    ]  
                }
            }
        }
     })

