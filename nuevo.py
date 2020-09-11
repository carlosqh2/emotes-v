from fbchat import log, Client

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onLoggedIn(self,email=None):
        print('Loggeado!')
    def onLoggingIn(self,email=None):
        print('Loggeando...')
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        # if author_id != self.uid:
            # self.send(message_object, thread_id=thread_id, thread_type=thread_type)
        if (message_object.text == 'crema') or (message_object.text == 'Crema'):
            self.sendRemoteFiles('https://i.redd.it/8nh61eetdtn01.jpg',thread_id=thread_id, thread_type=thread_type)

client = EchoBot(LOGIN, PASSWORD)
client.listen()

