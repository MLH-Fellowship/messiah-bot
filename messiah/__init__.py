import discord
from messiah.nlp import is_bio_declaration, is_help_request, get_bio


class MessiahClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message: discord.Message):
        if is_bio_declaration(message.content):
            bio = get_bio(message.content)
            print(
                f"Received the following biography: {bio} from {message.author}")
        if is_help_request(message.content):
            pass
