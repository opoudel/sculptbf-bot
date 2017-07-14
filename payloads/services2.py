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
                            "title": "Microdermabrasion",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/microdermabrasion.png",
                            "subtitle": "Diamond tips touches, your skin and resurface it",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "http://sculptbf.co.nz/index.php/microdermabrasion/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Collagen Induction Therapy CIT",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/collagen.png",
                            "subtitle": "Stimulates production of your own natural collagen",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "http://sculptbf.co.nz/index.php/collagen-induction-therapy-cit/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Vascular Treatment",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/vascular.png",
                            "subtitle":"Ellipse offers the ability to treat many skin conditions",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "https://sculptbf.co.nz/index.php/vascular-treatment/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        },
                        {
                            "title": "Face & Brow Lift",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/face_blow_lift.png",
                            "subtitle":"Non-invasive, pain free Radio-Frequency (RF) treatment",
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "title": "Detail",
                                    "url": "https://sculptbf.co.nz/index.php/face-eyebrow-lift/",
                                    "webview_height_ratio": "tall"
                                }
                            ]                
                        }                    
                    ],
                    "buttons": [
                        {
                            "title": "View More",
                            "type": "postback",
                            "payload": "MORE_SERVICES_3"                        
                        },
                    {
                        "type":"postback",
                        "payload":"GET_STARTED_PAYLOAD",
                        "title": "Go back"
                    }
                    ]  
                }
            }
        }
     })

