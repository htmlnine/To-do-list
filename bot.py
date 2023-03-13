import discord
import responses


async def send_msg(message, user_message, is_private):
    try:
        respnse = responses.handlemessage(user_message)
        await message.author.send(respnse) if is_private else await message.channel.send(respnse)
    except Exception as e:
        print(e)

    
    def runbot():
        TOKEN = ""
        client = discord.client()


        @client.event
        async def on_ready():
            print(f'{client.user}is running')

        client.run(TOKEN)