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
                                "webview_height_ratio": "compact"
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Email Now",
                                    "url": "http://sculptbf.co.nz/index.php/our-prices-offers/",
                                    "webview_height_ratio": "compact"
                                }
                            ]
                        },
                        {
                            "title": "Our affordable packaged plans designed just for you...",
                            "subtitle": "Select plan that best suit your need",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Email Now",
                                    "url": "http://sculptbf.co.nz/index.php/our-prices-offers/",
                                    "webview_height_ratio": "compact"
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

