"""
ここからslackobotを呼び出す,
"""
from slackbot.bot import Bot

def main():
  "main thread"
  bot = Bot()
  bot.run()

if __name__ == "__main__":
  print('start slackbot')
  main()
