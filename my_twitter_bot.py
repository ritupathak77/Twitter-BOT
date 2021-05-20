import tweepy
import time
print('this is ritu')


CONSUMER_KEY = 'fcX7rUvvDguiSKAwy8YwhMfzI'
CONSUMER_SECRET = 'SYPRM7QcaNmsrlabUAXO2iuiyUWCyldeoVl9co4syyEBJNbbgS'
ACCESS_KEY = '1394893505265238016-J4z0hbIncltdcqLrbVupLtceIzveRx'
ACCESS_SECRET = 'bIlmer8HxazjzURGrVm8qduFqExFQfFgux4aWOqheYdW9'

# using auth object using consumer key and consumer secret.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#using api to read and write from twitter. 
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

#store the api.mentions_timeline() in a variable
# type the variable in the shell to find out what class is it.
#It is of class tweepy.models.ResultSet
        
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
def reply_to_tweets():
    print('Trying it')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline( last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld!')
            print('responding back...')
            api.update_status('@'+ mention.user.screen_name + '#HelloWorld back to you dear!', mention.id)
            
            
while True:
    reply_to_tweets()
    time.sleep(2)
