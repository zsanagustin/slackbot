# from slackclient import SlackClient
 
# slack_client = SlackClient("xoxb-355943070582-mUxoCtns0lUhJ34XbD5VAjN5")
 
# api_call = slack_client.api_call("users.list")
# if api_call.get('ok'):
#     users = api_call.get('members')
#     for user in users:
#         print user.get('name')

import bot
bot.Bot()