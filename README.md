# messiah-bot
Messiah is a Discord bot that learns who in your server is good at helping with tasks, and when someone asks for help, it will redirect them to someone best suited to helping them out.

## Commands
* `!messiah bio` to read your bio
* `!messiah bio <bio>` to replace your bio
* `!messiah forget` to empty your bio and disable your being pinged

Messiah picks up on several different conversational cues to naturally pick up who's who. The specifics are in the `messiah.nlp` module.
For example, the following message would teach Messiah that you can help someone with your organization's payment.

> Hi, I'm Aanand! I can help out with payments

> I need help with my paycheck this month!
