# coding: utf-8

"""
@respond_to('string')     bot宛のメッセージ  stringは正規表現が可能 「r'string'」
@listen_to('string')      チャンネル内のbot宛以外の投稿 正規表現可
                          @botname: では反応せず, 他人へのメンションには反応
@default_reply()          DEFAULT_REPLY と同じ働き 現状正規表現は危険

message.reply('string')   @発言者名: string でメッセージを送信
message.send('string')    string を送信
message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する, ":"は不要

message.send_webapi('', json.dumps(ary)) aryの中に入ったJSONを表示
message.body['text']     # メッセージを取り出す

reference:
    qiita: qiita.com/hypermkt/items/b2ffaf610ac92235c4d6
    qiita: qiita.com/daikiojm/items/759ea40c00f9b539a4c8
    Slack_API: https://api.slack.com/docs/message-attachments
    Slack_API: https://api.slack.com/docs/message-buttons
"""

from functools import partial
import toml
# import re

from slackbot.bot import respond_to, listen_to, default_reply     # @botname: で反応するデコーダ
from plugins import implemention as im

MSG_CONFIG = toml.load("./plugins/config.toml")["msg"]
open_json = partial(im.open_config, MSG_CONFIG) #open_json("msg_name"), open msg obj


@default_reply()
def default_func(message):
  "default reply"
  content = open_json("default")
  im.send_attachment(message, [content])
