import json

def message(recipient_id):
	return json.dumps({
	        "recipient": {
	            "id": recipient_id
	        },
	        "message": {
	            "text": "Woot Woot!"
	        }
	    })