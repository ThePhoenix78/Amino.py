import amino

client = amino.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')

@client.event("on_text_message")
def on_text_message(data):
    print(f"{data.message.author.nickname}: {data.message.content}")