import discord

from messiah.biostorage import all_bios, get_bio, set_bio, update_bio
from messiah.nlp import get_offer_text, get_request_text, bio_similarity_to


class MessiahClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_reaction_add(self, reaction: discord.Reaction,
                              user: discord.abc.User):
        if reaction.me and user != self.user:
            message: discord.Message = reaction.message
            if offer_text := get_offer_text(message.content):
                bio = get_bio(user.mention)
                set_bio(user.mention, bio[0:-len(offer_text)-1])

    async def on_message(self, message: discord.Message):
        author: discord.abc.User = message.author
        mention: str = author.mention
        message_text: str = message.content

        if author == self.user:
            return

        if message_text.startswith("!messiah"):
            subcommand = message_text[9:]
            if subcommand.startswith("bio"):
                new_bio = subcommand[4:]
                if new_bio:
                    set_bio(mention, new_bio)
                    await message.reply("Your bio has been updated")
                else:
                    bio = get_bio(mention)
                    if bio:
                        await message.reply(bio)
                    else:
                        await message.reply("There's no bio on record for you")
            if subcommand == "forget":
                set_bio(mention, "")
                await message.reply("Your bio has been cleared")

        if question_text := get_request_text(message_text):
            similarity = bio_similarity_to(question_text)
            bios_to_check = [bio for bio in all_bios if bio["bio_text"]]
            best_match = max(bios_to_check, key=similarity)
            await message.channel.send(
                f"Hi {mention}, {best_match['mention']} should be able to "
                f"help you!")
        elif offer_text := get_offer_text(message_text):
            update_bio(mention, offer_text)
            await message.add_reaction("🛑")
