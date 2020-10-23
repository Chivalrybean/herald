import local_settings as ls
# token = bot token
# control_channel = channel to store reaction settings and messages
# bot_users = [users allowed to perform bot actions and send messages]
import discord
import pickle


class Data_storage:
    def __init__(self, servers):
        self.servers = servers


class Server:
    def __init__(self, server_id, channels):
        self.server_id = server_id
        self.channels = channels


class Channel_settings:
    def __init__(self, channel_id, channel_emoji):
        self.channel_id = channel_id
        self.channel_id_emoji = channel_emoji
