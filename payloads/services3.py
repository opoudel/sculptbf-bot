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
                            "title": "Body Fat Reduction",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/body_fat.png",
                            "subtitle": "FDA-cleared non-invasive lipolysis of almost all part of body",
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
                            "subtitle": "The result: firmer, tighter younger looking skin",
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
                            "subtitle":"We are expert in removing acne scar",
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
                            "subtitle":"No more gray-brown patches on the face",
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

