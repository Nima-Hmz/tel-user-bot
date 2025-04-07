from telethon import TelegramClient, events
import socks

# Replace these with your actual credentials from my.telegram.org
api_id = 28921433
api_hash = 'f1adfe69f1f327b4ebceca39538ca389'

# 'session_name' will be used to store your session details locally
client = TelegramClient('session_name', api_id, api_hash)

# Force connection to a specific data center (e.g., DC2 using production configuration)
client.session.set_dc(2, '149.154.167.50', 443)

@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    # Check if the message is a direct (private) message
    if event.is_private:
        # Forward the message to your Saved Messages by sending it to 'me'
        await client.send_message('me', event.message)
        print("Forwarded a message to Saved Messages.")

# Start the client and run it until you stop the script
client.start()
print("Listening for new direct messages...")
client.run_until_disconnected()

