from telethon import TelegramClient, events

# Replace these with your actual credentials from my.telegram.org
api_id = 28921433
api_hash = 'f1adfe69f1f327b4ebceca39538ca389'

# Your phone number with country code (e.g., +15551234567)
phone = '09229150579'

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

# Define a function to handle login
async def main():
    # This will automatically prompt for login if required
    # For non-interactive environments, we need to handle it here
    if not await client.is_user_authorized():
        try:
            await client.start(phone=phone)
            print("Client authorized successfully.")
        except Exception as e:
            print(f"Authentication error: {e}")
            return

    print("Listening for new direct messages...")
    
    # This keeps the client running until you interrupt it
    await client.run_until_disconnected()

# Start the client without the interactive prompt
with client:
    client.loop.run_until_complete(main())

