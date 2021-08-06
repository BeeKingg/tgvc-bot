"""
tgvc-userbot, Telegram Voice Chat Userbot
Copyright (C) 2021  Dash Eclipse

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from os import environ

# import logging
from pyrogram import Client, idle

API_ID = int(environ["API_ID"5658345"])
API_HASH = environ["API_HASH"bad0d2770acaf3a673d42dbe52c4cfee"]
SESSION_NAME = environ["SESSION_NAME"BQALQ-tVTNr74hCvsKFEFhmRwtqDRBnCcU3EAmV49EDDpbaM-N2fZTbGbcjwMWZag0jN1Hr6xnjmnQyJg61bsfDq8zs1Op-lbQPqqATlapy7L4bIIWAkpwC4lCntD8870_vERCZXph7NPonlcGv6aDMu5eiLjbazGtcp-Yo9v3iRkYzlb1A7xsgpldxvi6tM7qKkAetGCptQ8Y-4mWD0oV8T7wGTqCAAmhWJlLDSYafWrgugyM8bhf3XxdT8gWfGzf5_a03GfQypYv2cDygIJkqG88TZ2RQk0QYSFoxwoyoapYFKLTmMYGjYUHDeB28XiSblcYpm_p78jnzahmUBC42ocuUs4wA"]

PLUGINS = dict(
    root="plugins",
    include=[
        "vc." + environ["PLUGIN"],
        "ping",
        "sysinfo"
    ]
)

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=PLUGINS)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
