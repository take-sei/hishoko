# hishoko
Slack bot

- When you try to use this scripts, make a "slackbot_settings.py" file, and describe this.

```
# coding: utf-8
  """
  slack botの設定. tokenとか, 静的なあdefault replyとか, 読み込むpluginとかとか.
  """

# botアカウントのトークンを指定
  API_TOKEN = "#{SLACKBOT_API-TOKEN}"

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
  DEFAULT_REPLY = "...?"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
  PLUGINS = ['plugins']
```
