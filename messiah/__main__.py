from messiah import MessiahClient
import os


if __name__ == '__main__':
    client = MessiahClient()
    # noinspection SpellCheckingInspection
    client.run(os.getenv("messiah_bot"))
