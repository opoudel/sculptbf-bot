import json

def message(recipient_id):
	return json.dumps({
	        "recipient": {
	            "id": recipient_id
	        },
          "message": {
            "attachment": {
              "type": "template",
              "payload": {
                "template_type": "generic",
							  "get_started":{
							    "payload":"GET_STARTED_PAYLOAD"
							  }                
              }
            }
          }
   })