"""
implemention file of response.py
"""

import json

def send_attachment(msg, content):
  """
    send_attachment(msg, content)
    msgオブジェクトと, 送るjsonを指定すれば送るよ
  """
  msg.react("eyes")
  temp = json.dumps([content])
  msg.send_webapi('', temp)#aryの中に入ったJSONを表示

def open_config(config, msg_name):
  """
  open json file with config file obj and, msg name
  """
  return json.load(open(config[msg_name]["path"]))
