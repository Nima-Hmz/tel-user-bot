from telethon import TelegramClient, events
import asyncio

# Replace these with your actual credentials from my.telegram.org
api_id = 28921433
api_hash = 'f1adfe69f1f327b4ebceca39538ca389'

# Your phone number with country code (e.g., +15551234567)
phone = '+989229150579'

# Authentication code callback - replace with the code you receive
async def code_callback():
    # Replace this with the verification code you receive on your phone
    return "12345"  # ⚠️ REPLACE WITH YOUR ACTUAL CODE ⚠️

# Create the client
client = TelegramClient('name', api_id, api_hash)

async def main():
    try:
        # Start the client with phone and code callback
        await client.start(phone=phone, code_callback=code_callback)
        
        # Send a message to "Saved Messages"
        await client.send_message('me', 'Hello, myself!')
        
        # Download your profile picture
        profile_pic = await client.download_profile_photo('me')
        print(f"Profile photo saved to: {profile_pic}")
        
        # Message handler for messages containing "Hello"
        @client.on(events.NewMessage(pattern='(?i).*Hello'))
        async def handler(event):
            await event.reply('Hey!')
            
        print("Client started successfully! Listening for messages...")
        # Keep the client running
        await client.run_until_disconnected()
    except Exception as e:
        print(f"Error: {e}")

# Run the client without using the "with" context manager
if __name__ == "__main__":
    asyncio.run(main())

