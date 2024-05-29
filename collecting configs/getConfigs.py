import asyncio
from flask import Flask, jsonify
from flask_cors import CORS
from telethon import TelegramClient, events
import threading
import time

# Replace 'API_ID' and 'API_HASH' with your actual Telegram API credentials
API_ID = '12345678'
API_HASH = '12345678abcdefg'
CHANNEL_USERNAME = '@channel-id'


client = TelegramClient('session_name', API_ID, API_HASH)
messages = [] #messages will be stored here


#will fetch the last 15 messages of the channel
async def fetch_messages():
    global messages
    try:
        new_messages = []
        async for message in client.iter_messages(CHANNEL_USERNAME, limit=15):
            if message.message:
                new_messages.append(message.message)
        new_messages.reverse()  # To get the messages in chronological order
        messages[:] = new_messages  # Update the global messages list
        print(f"Fetched {len(messages)} messages.")
    except Exception as e:
        print("Error fetching messages:", e)


#this will get the new messages
@client.on(events.NewMessage(chats=CHANNEL_USERNAME))
async def new_message_handler(event):
    global messages
    if len(messages) >= 15:
        messages.pop(0) 
    messages.append(event.message.message)
    print("New message received:", event.message.message)


#athorization
async def authorize_client():
    await client.start()
    me = await client.get_me()
    print(f"Logged in as {me.username}")


#loop the fetching process so it runs forever
def auto_refresh(interval=30):
    while True:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(fetch_messages())
        loop.close()
        time.sleep(interval)

#this will run the client
def run_telegram_client():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(authorize_client())
    loop.run_until_complete(fetch_messages())
    client.run_until_disconnected()

#creating the app
app = Flask(__name__)
CORS(app)  #enabling cors

#API endpoint
@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    #start the Telegram client thread:
    telegram_thread = threading.Thread(target=run_telegram_client)
    telegram_thread.start()

    #auto-refresh function thread:
    refresh_thread = threading.Thread(target=auto_refresh, args=(30,))  # Refresh every 30 seconds
    refresh_thread.start()

    #run the app
    app.run(host='0.0.0.0', port=5000)
