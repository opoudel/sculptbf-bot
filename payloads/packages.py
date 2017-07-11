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
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Email Now",
                                    "url": "http://sculptbf.co.nz/index.php/our-prices-offers/",
                                    "webview_height_ratio": "tall",
                                    "fallback_url": "http://sculptbf.co.nz"
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

