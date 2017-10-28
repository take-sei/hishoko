# coding: utf-8

"""
slackbotの一般的な受け答え関係の実装
# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           現状正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない

# message.send_webapi('', json.dumps(ary)) aryの中に入ったJSONを表示
# text = message.body['text']     # メッセージを取り出す

reference:
    qiita: qiita.com/hypermkt/items/b2ffaf610ac92235c4d6
    qiita: qiita.com/daikiojm/items/759ea40c00f9b539a4c8
    Slack_API: https://api.slack.com/docs/message-attachments
    Slack_API: https://api.slack.com/docs/message-buttons
"""

import json
import toml
# import re

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

MSG_CONFIG = toml.load("./plugins/config.toml")["msg"]
reply_list = MSG_CONFIG.key()



def send_attachment(msg, content):
  """
    send_attachment(msg, content)
    msgオブジェクトと, 送るjsonを指定すれば送るよ
  """
  msg.react("eyes")
  temp = json.dumps(content)
  msg.send_webapi('', temp)#aryの中に入ったJSONを表示

@default_reply()
def default_func(message):
  """
  デフォルト返信
  """
  cash = open(MSG_CONFIG["default"]["path"])
  content = json.load(cash)
  send_attachment(message, [content])
