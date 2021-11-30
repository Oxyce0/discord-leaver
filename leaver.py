import discord
import asyncio


client = discord.Client()
token = "" # Discord hesabınızın tokeni
prefix = "." # Herhangi bir prefix
command = "gl" # Başlatmak için kullanacağınız komut

@client.event
async def on_ready():
    print("Token Kabul Edildi! " + prefix + "" + command + " Başarıyla Gruplardan Çıkılmaya Başlanıyor!")

@client.event
async def on_message(message):
    if message.author == client.user:
        cmd = str(message.content).split(' ')
        if cmd[0] == prefix + command:
            await message.delete()
            count = 0
            for channel in client.private_channels:
                if isinstance(channel, discord.GroupChannel):
                    if channel.id != message.channel.id:
                        count = count + 1
                        await channel.leave()
                        print("Çıkıldı: " + str(channel.id)) # Print group ID in console.
            await message.channel.send("``Toplam [" + str(count) + "] gruptan çıkıldı!``")
            await client.close()

client.run(token, bot=False)
input("Entere bas ve çıkış yap.")