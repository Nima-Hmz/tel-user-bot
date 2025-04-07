from telethon import TelegramClient, events
import asyncio

# Replace these with your actual credentials from my.telegram.org
api_id = 28921433
api_hash = 'f1adfe69f1f327b4ebceca39538ca389'

# Your phone number with country code (e.g., +15551234567)
phone = '09229150579'

# Hardcoded verification code callback function
# This will return the specified code when requested
async def code_callback():
    # You'll need to replace this with the actual code you receive
    # This is just a placeholder and won't work until you put your real code here
    return "12345"  # Replace with the verification code you receive

# Password callback in case 2FA is enabled
# async def password_callback():
#     # If you have two-factor authentication enabled, put your password here
#     return "your_2fa_password_here"  # Replace if you have 2FA

# Create the client but don't start it yet
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

# The non-interactive way to start Telethon
async def main():
    try:
        print("Starting client...")
        
        # Connect to Telegram servers
        await client.connect()
        
        # Check if we're already authorized
        if not await client.is_user_authorized():
            print("Not authorized, signing in...")
            # This will use the phone and code_callback
            await client.sign_in(phone=phone, code_callback=code_callback)
            print("Successfully signed in!")
        else:
            print("Already authorized")
        
        print("Listening for new direct messages...")
        # Keep the client running
        await client.run_until_disconnected()
    except Exception as e:
        print(f"Error: {e}")

# Run the client without using a context manager
if __name__ == "__main__":
    asyncio.run(main())

