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
                            "title": "Eye Dark Circle",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/eye_dark_circle.png",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "http://sculptbf.co.nz/index.php/eye-dark-circle/",
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

