import os
import sys
import json

import requests
import payloads
import payloads.aboutus
import payloads.menu
import payloads.packages
import payloads.morepackages
import payloads.morepackages1

import payloads.special

import payloads.services
import payloads.services1
import payloads.services2
import payloads.services3
import payloads.services4
import payloads.services5
import payloads.services6

import payloads.shop
import payloads.shop1
import payloads.shop2
import payloads.shop3
import payloads.shop4



from flask import Flask, request

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello Face and Body Clinic", 200


@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):  # someone sent us a message
                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    send_message(sender_id, payloads.message(sender_id))
                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    sender_id = messaging_event["sender"]["id"]
                    recipient_id = messaging_event["recipient"]["id"]
                    if messaging_event["postback"]["payload"] == "GET_STARTED_PAYLOAD":
                        send_message(sender_id, payloads.menu.menu(sender_id))
                    if messaging_event["postback"]["payload"] == "ABOUT_US_PAYLOAD":
                        send_message(sender_id, payloads.aboutus.aboutus(sender_id))
                    if messaging_event["postback"]["payload"] == "VIEW_PACKAGES_PAYLOAD":
                        send_message(sender_id, payloads.packages.packages(sender_id))
                    if messaging_event["postback"]["payload"] == "VIEW_MORE_PACKAGES_PAYLOAD":
                        send_message(sender_id, payloads.morepackages.morepackages(sender_id))
                    if messaging_event["postback"]["payload"] == "VIEW_MORE_PACKAGES1_PAYLOAD":
                        send_message(sender_id, payloads.morepackages1.morepackages(sender_id))
                    if messaging_event["postback"]["payload"] == "SERVICES":
                        send_message(sender_id, payloads.services.services(sender_id))
                    if messaging_event["postback"]["payload"] == "MORE_SERVICES_1":
                        send_message(sender_id, payloads.services1.services(sender_id))
                    if messaging_event["postback"]["payload"] == "MORE_SERVICES_2":
                        send_message(sender_id, payloads.services2.services(sender_id))
                    if messaging_event["postback"]["payload"] == "MORE_SERVICES_3":
                        send_message(sender_id, payloads.services3.services(sender_id))
                    if messaging_event["postback"]["payload"] == "MORE_SERVICES_4":
                        send_message(sender_id, payloads.services4.services(sender_id))
                    if messaging_event["postback"]["payload"] == "MORE_SERVICES_5":
                        send_message(sender_id, payloads.services5.services(sender_id))
                    if messaging_event["postback"]["payload"] == "MORE_SERVICES_6":
                        send_message(sender_id, payloads.services6.services(sender_id))
                    if messaging_event["postback"]["payload"] == "SHOPPING":
                        send_message(sender_id, payloads.shop.shop(sender_id))
                    if messaging_event["postback"]["payload"] == "MORE_SHOPPING_1":
                        send_message(sender_id, payloads.shop1.shop(sender_id))
                    if messaging_event["postback"]["payload"] == "MORE_SHOPPING_2":
                        send_message(sender_id, payloads.shop2.shop(sender_id))
                    if messaging_event["postback"]["payload"] == "MORE_SHOPPING_3":
                        send_message(sender_id, payloads.shop3.shop(sender_id))
                    if messaging_event["postback"]["payload"] == "MORE_SHOPPING_4":
                        send_message(sender_id, payloads.shop4.shop(sender_id))
                    if messaging_event["postback"]["payload"] == "SPECIAL":
                        send_message(sender_id, payloads.special.special(sender_id))
    return "ok", 200
 
def send_message(recipient_id, data):
    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = data
    r = requests.post("https://graph.facebook.com/v2.9/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def log(message):
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)