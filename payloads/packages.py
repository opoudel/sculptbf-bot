import json

def packages(recipient_id):
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
                        "title": "Our affordable packaged plans designed just for you...",
                        "subtitle": "Select plan that best suit your need",
                        "default_action": {
                            "type": "web_url",
                            "url": "http://sculptbf.co.nz/index.php/our-prices-offers",
                            "webview_height_ratio": "tall",
                            "fallback_url": "http://sculptbf.co.nz"
                        },
                        "buttons": [
                            {
                                "title": "View",
                                "type": "web_url",
                                "url": "http://sculptbf.co.nz/index.php/our-prices-offers/",
                                "webview_height_ratio": "tall",
                                "fallback_url": "http://sculptbf.co.nz"
                            }
                        ]
                    },
                    {
                        "title": "Dermal Pigmentation or Freckles",
                        "image_url": "https://sculptbf-bot.herokuapp.com/static/FacialPeel-1.png",
                        "subtitle": "Price: $600... includes: 3 X Clarity Peel, 3 x Lactic Peel & 1 Set of Home Care Product",
                        "default_action": {
                            "type": "web_url",
                            "url": "http://sculptbf.co.nz/index.php/contact-us/",
                            "webview_height_ratio": "tall",
                            "fallback_url": "http://sculptbf.co.nz"
                        },
                        "buttons": [
                            {
                                "title": "Email Now",
                                "type": "web_url",
                                "url": "http://sculptbf.co.nz/index.php/contact-us/",
                                "webview_height_ratio": "tall",
                                "fallback_url": "http://sculptbf.co.nz"
                            }
                        ]                
                    },
                    {
                        "title": "Photo Rejuvenation Deal",
                        "image_url": "https://sculptbf-bot.herokuapp.com/static/photoReju.png",
                        "subtitle": "Price: $450... includes: I2PL Plus x 6 Session (Face Only), 1 Hair cut Free ",
                        "default_action": {
                            "type": "web_url",
                            "url": "http://sculptbf.co.nz/index.php/contact-us/",
                            "webview_height_ratio": "tall",
                            "fallback_url": "http://sculptbf.co.nz"
                        },
                        "buttons": [
                            {
                                "title": "Email Now",
                                "type": "web_url",
                                "url": "http://sculptbf.co.nz/index.php/contact-us/",
                                "webview_height_ratio": "tall",
                                "fallback_url": "http://sculptbf.co.nz"
                            }
                        ]                
                    },
                    {
                        "title": "Photo Rejuvenation Microdermabrasion",
                        "image_url": "https://sculptbf-bot.herokuapp.com/static/photorejumicro.png",
                        "subtitle": "Price: $169... includes: 3 x Microdermabrasion with TNS Mask, 3 X LED Face Mask",
                        "default_action": {
                            "type": "web_url",
                            "url": "http://sculptbf.co.nz/index.php/contact-us/",
                            "webview_height_ratio": "tall",
                            "fallback_url": "http://sculptbf.co.nz"
                        },
                        "buttons": [
                            {
                                "title": "Email Now",
                                "type": "web_url",
                                "url": "http://sculptbf.co.nz/index.php/contact-us/",
                                "webview_height_ratio": "tall",
                                "fallback_url": "http://sculptbf.co.nz"
                            }
                        ]                
                    }
                ],
                 "buttons": [
                    {
                        "title": "View More",
                        "type": "postback",
                        "payload": "VIEW_MORE_PACKAGES_PAYLOAD"                        
                    }
                ]  
            }
        }
    }
 })

