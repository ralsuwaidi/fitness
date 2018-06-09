import praw
from datetime import datetime

class reddit_post:
    def __init__(self, user, post, date, link):
        self.user=user
        self.post=post
        self.date=date
        self.link=link

    

def pop_reddit():

    reddit = praw.Reddit(client_id='T1mKRsAWXfGfzA',
                         client_secret='9I0sxWA2kmIDi4TIaP7LLvON0zA',
                         user_agent='my user agent')


    stickies = [reddit.subreddit("writingprompts").sticky(
        i).id for i in range(1, 4)]

    count = 4


    for submission in reddit.subreddit('fitness').top('all', limit=50):
        if submission.id not in stickies:

            title=submission.title[:50]
            title=title.replace(" ","_")
            title=str(submission.score)+"__"+ ''.join(e for e in title if e.isalnum() or e=="_")+".md"
            date = datetime.utcfromtimestamp(submission.created_utc)
            f=open(title, "w+")
            f.write(submission.selftext)
            f.close

pop_reddit()
                #Writingprompt.objects.update_or_create(comment=top_comment,
                 #                                  defaults={'score': submission.score, 'title': submission.title.replace("[WP] ",""), 'pub_date': date, 'url': submission.url}, )


