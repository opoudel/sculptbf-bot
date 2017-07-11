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
                            "image_url":"https://cdn.pixabay.com/photo/2013/07/13/12/50/beauty-160456_1280.png",
                            "default_action": {
                                "type": "web_url",
                                "url": "http://sculptbf.co.nz/index.php/our-prices-offers/",
                                "webview_height_ratio": "tall"
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "View",
                                    "url": "http://sculptbf.co.nz/index.php/our-prices-offers/",
                                    "webview_height_ratio": "tall"
                                }
                            ]
                        },
                        {
                            "title": "Dermal Pigmentation or Freckles ($600 only)",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/FacialPeel-1.png",
                            "subtitle": "Includes: \n\t3 X Clarity Peel, \n\t3 x Lactic Peel, \n\t1 Set of Home Care Product",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Email Now",
                                    "url": "http://sculptbf.co.nz/index.php/contact-us/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Photo Rejuvenation Deal ($450 only)",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/photoReju.png",
                            "subtitle": "Includes: \n\tI2PL Plus x 6 Session (Face Only)\n\t1 Hair cut Free ",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Email Now",
                                    "url": "https://sculptbf.co.nz/index.php/contact-us/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Photo Rejuvenation Microdermabrasion ($169 only)",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/photorejumicro.png",
                            "subtitle": "Includes: \n\t3 x Microdermabrasion with TNS Mask \n\t3 X LED Face Mask",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Email Now",
                                    "url": "https://sculptbf.co.nz/index.php/contact-us/",
                                    "webview_height_ratio": "tall"
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

