"""
slack bot, python-client lib used version.
"""

import os
import json
import toml
from functools import partial
from slackclient import SlackClient

SLACK_API_TOKEN = toml.load("./config.toml")["meta"]["token"]
SLACK_OAUTH = toml.load("./config.toml")["meta"]["oauth_access"]
BOT_OAUTH = toml.load("./config.toml")["meta"]["bot_oauth"]
MSG_CONFIG = toml.load("./config.toml")["msg"]

client = SlackClient(BOT_OAUTH)
print(BOT_OAUTH)

client.api_call(
  "chat.postMessage",
  channel="#debug",
  text="はじめましてー, botの秘書子でーす, よろしくね :tada:"
)
