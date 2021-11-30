# Slack Bolt Flask Bot

## About

Maintained by Github user mandagill, Slack handle @amanda.gilmore

This is a lightweight bot created to allow Slack users to create listeners for a specific term in a given Slack channel. It uses Flask to allow the bot to be deployed on Kubernetes, which requires a healthcheck. 

## Development

This bot relies on three Slack secrets and one Flack configuration variable to work. Necessary secrets to export are:

```
SLACK_BOT_TOKEN=<found in your Slack app's configuration page> 
SLACK_APP_TOKEN=<found in your Slack app's configuration page> 
SLACK_SIGNING_SECRET=<found in your Slack app's configuration page> 
FLASK_SETTINGS=./settings.cfg
```
Slack token docs are here: https://api.slack.com/authentication/token-types

After starting the server with `python app.py`, start an `ngrok` proxy with `ngrok 80 http`. Paste the https URL in to your Slack app configuration as described in the [Slack docs](https://slack.dev/bolt-python/tutorial/getting-started-http#sending-and-responding-to-actions).

## Deployment

After deploying the code, you need to **add the bot to the channel you'd like to listen to specific terms in.** To do this, use the `/invite` slash command or @ mention the bot in the channel you'd like to listen in.


### A note on unit testing:

To keep the scope of our mocks tightly focused, I recommend testing the **application logic** of our bot separately from its interface into Slack. Put another way, the functions that listen for and respond to Slack events should be as lightweight as possible, and **only call functions that we write.** This way we can more easily test the functions without needing to mock up the Slack API.