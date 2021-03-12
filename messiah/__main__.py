from messiah import MessiahClient
import os

os.environ["messiah_bot"]="ODE5NDYzMTgwMjc4NTYyODQ3.YEm-jw.AAx2Ntc_RizLOOmED9NmjnAbMaI"


if __name__ == '__main__':
    client = MessiahClient()
    # noinspection SpellCheckingInspection
    client.run(os.getenv("messiah_bot"))
