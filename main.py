from telethon import TelegramClient, events
import asyncio

# Replace these with your actual credentials from my.telegram.org
api_id = 28921433
api_hash = 'f1adfe69f1f327b4ebceca39538ca389'

# Your phone number with country code (e.g., +15551234567)
phone = '+989229150579'


with TelegramClient('name', api_id, api_hash) as client:
   client.send_message('me', 'Hello, myself!')
   print(client.download_profile_photo('me'))

   @client.on(events.NewMessage(pattern='(?i).*Hello'))
   async def handler(event):
      await event.reply('Hey!')

   client.run_until_disconnected()

