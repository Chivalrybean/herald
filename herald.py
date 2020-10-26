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
    def __init__(self, channel_id, channel_emoji=None, control_channel=False):
        self.channel_id = channel_id
        self.channel_id_emoji = channel_emoji
        self.control_channel = control_channel


def set_emoji(channel_id, emoji):
    """Choose an emoji that will send message to specified channel when message is reacted to with that emoji
    Arguments: 
    channel ID(int) - the Discord ID for the channel
    emoji(string) - The emoji reaction to trigger sending the message to the channel
    """
    new_setting = Channel_settings(channel_id, emoji)
    return new_setting


def set_control(channel_id):
    """Select a channel and set it to the channel the bot will send reacted messages from."""
    new_setting = Channel_settings(channel_id, None, True)
    return new_setting
