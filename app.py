import logging 
import os
import re

from flask import Flask, request

from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

from pprint import pprint

# Set up Bolt app
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

logger = logging.basicConfig(level=logging.DEBUG)

# Set up Flask app
flask_app = Flask(__name__)
handler = SlackRequestHandler(app)
logging.basicConfig(level=logging.DEBUG)

flask_app.config['DEBUG'] = True
flask_app.config.from_envvar('FLASK_SETTINGS')

class IntegrationClient(object):
    # Stub out integration to share with Slack support
    def send_message(self, message):
        # TODO
        pprint(message)


@app.message(re.compile("(bonjour|hello|merhaba)"))
def listen_for_keywords(context, logger, body):
    # regular expression matches are inside of context.matches
    copy_matched = context['matches'][0]
    # do some stuff with the info from the matched message
    client = IntegrationClient()
    client.send_message(copy_matched)
    logger.info(f"Attempted to make call to integration based on {copy_matched}")


# Bolt needs a default action to do with messages or it errors
@app.event("message")
def handle_message_events(logger):
    logger.info("fell back to default")


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    # Perhaps I need to use this to form the response with signature?
    # https://slack.dev/bolt-python/api-docs/slack_bolt/adapter/flask/handler.html
    return handler.handle(request)




# Start your app
if __name__ == "__main__":
    logging.info("Starting app...")
    app.start(port=3000)