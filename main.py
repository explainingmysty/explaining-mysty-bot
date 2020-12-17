import random
import twitter
import asyncio
import vocabulary
import markov

# Bots created by @thearrowace_ and @blueberriemilo.

explains = twitter.Bot(user="ExplainingMysty")
cerise = twitter.Bot(user="WILBURCRIME")
diana = twitter.Bot(user="dianasmiIes")

async def send_tweet_cerise():
    await cerise.wait_until_ready()
    while not cerise.is_closed():
        action = random.randint(0, 1)
        if action == 0:
            for i in range(8):
                await cerise.retweet(random.choice(random.choice(cerise.followers).tweets))
                await asyncio.sleep(900000)
        else:
            output = markov.generate('cerise', k=2, n=random.randint(1, 50))
            await cerise.send(output)
            await asyncio.sleep(28800000)

async def send_tweet_diana():
    await cerise.wait_until_ready()
    while not cerise.is_closed():
        action = random.randint(0, 1)
        if action == 0:
            for i in range(8):
                await diana.retweet(random.choice(random.choice(diana.followers).tweets))
                await asyncio.sleep(900000)
        else:
            output = markov.generate('diana', k=2, n=random.randint(1, 50))
            await diana.send(output)
            await asyncio.sleep(7200000)

@explains.event
async def on_tweet(tweet):
    if tweet.author == twitter.User(user="MysticatLive"):
        word_list = tweet.content.split()
        output = "In this tweet, Mysticat {}".format(random.choice(vocabulary.synonym('says')))
        for word in word_list:
            if word not in vocabulary.filler_word_list:
                continue
            elif word in vocabulary.common_word_list:
                output += random.choice(vocabulary.synonym('says'))
            elif word in vocabulary.future_smp:
                output += "{}, friend and fellow member of the Future SMP, ".format(word)
            else:
                output += "{}, which means {}, ".format(word, vocabulary.definition(word))
        await explains.send(output)

print("if someone's actually reading this, u've prob realized by now that")
print("this bot doesnt do shit and idk how to code a twitter bot")
print("also this code is ugly af but it needs to look complicated so L")

cerise.loop.create_task(send_tweet_cerise())
diana.loop.create_task(send_tweet_diana())

explains.run(password='PzgxsHETna5ppNLH')
cerise.run(password='SxpZzEt2tnaXRAVz')
diana.run(password='TdDEXE2F9GWZbsZU')
