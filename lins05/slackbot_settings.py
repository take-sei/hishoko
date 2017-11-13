# coding: utf-8
"""
slack botの設定. tokenとか, 静的なあdefault replyとか, 読み込むpluginとかとか.
"""
import toml

META_CONFIG = toml.load("./plugins/config.toml")["meta"]

# botアカウントのトークンを指定
API_TOKEN = META_CONFIG["APIkey"]

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "...?"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
