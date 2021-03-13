import os

from messiah import MessiahClient

if __name__ == '__main__':
    client = MessiahClient()
    bot_token = os.getenv("messiah_bot")
    client.run(bot_token)
