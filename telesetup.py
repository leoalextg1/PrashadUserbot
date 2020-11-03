#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details""")
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
      print("")
      session = client.session.save()
      client.send_message("me", f"**Here is your TELEGRAM STRING SESSION**👇\n(tap to copy) \n\n `{session}`")
      print("You Telegram String session has been successfully stored in your Telegram Saved Messages. Please check your Saved Messages!")
      print("Store it safe!!")
  except:
   print ("")
   print ("Wrong phone number \n Make sure it's with correct Country Code")
   print ("")
   continue
  break