import json

def morepackages(recipient_id):
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
                            "title": "3 Face or Neck Treatment ($1800 only)",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/3xfaceneck.png",
                            "subtitle": "Includes: \n\t6 Syringes of Restylane or Redensity, \n\t3 x LED Therapy, \n\tCan add Pelleve Face OR Neck Lift & Tightening only $150 per Session",
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
                            "title": "Face or Neck, PRP Treatment ($2400 only)",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/PRPfaceneck.png",
                            "subtitle": "Includes: \n\t3 x PRP with Matrix HA Tube & THT Tabe, \n\t3 x LED Therapy, \n\tCan add Pelleve Face OR Neck Lift & Tightening only $150 per Session",
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
                            "title": "Body Sculpting + Fat Reduction ($3000 only)",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/bodysculptfat.png",
                            "subtitle": "Includes: \n\t3 x Treatment of Choice (Flanks, Upper OR Lower Abdomen)\n\t3 x Pelleve Body Tightening",
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
                            "title": "Acne Scar Treatment ($2700 only)",
                            "image_url": "https://sculptbf-bot.herokuapp.com/static/AcneScar.png",
                            "subtitle": "Includes: \n\t1 home care pdcts \n\t1 Er Fractional laser treatment\n\tPlateletes Rich Plasma (PRP) and LED\n\tRestylane skin booster or Redensity (I) and LED\n\tPelleve tightening",
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
                        "payload": "VIEW_MORE_PACKAGES1_PAYLOAD"
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

