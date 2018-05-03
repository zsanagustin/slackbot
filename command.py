import tweepy

consumerKey = "********"
consumerSecret = "*********"
accessToken = "*********"
accessTokenSecret = "********" 

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

status = "Testing!"

trends1 = api.trends_place(1) 
data = trends1[0] 
trends = data['trends']
names = [trend['name'] for trend in trends]
trendsName = ' '.join(names)
# print(trendsName.encode("utf-8"))

namesstr = "\n"+names[0]+"\n"+names[1]+"\n"+names[2]+"\n"+names[3]+"\n"+names[4]+"\n"+names[5]+"\n"+names[6]+"\n"+names[7]+"\n"+names[8]+"\n"+names[9]

class Command(object):

    def __init__(self):
        self.commands = { 
            "hi" : self.hi,
            "trends" : self.trends,
            "help" : self.help
        }
	 	
    def handle_command(self, user, command):
        response = "<@" + user + ">: "
     
        if command in self.commands:
            response += self.commands[command]()
        else:
            response += "Sorry I don't understand the command: " + command + ". " + self.help()
         
        return response
    
    def hi(self):
        return "hello"

    def trends(self):
		return namesstr

    def help(self):
        response = "Currently I support the following commands:\r\n"
         
        for command in self.commands:
            response += command + "\r\n"
             
        return response