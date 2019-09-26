import heapq
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_tweet = {}
        self.follower = {}
        self.tweet_time = 1

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        """
        if userId not in self.user_tweet:
            self.user_tweet[userId] = [(self.tweet_time, tweetId)]
        else:
            self.user_tweet[userId].append((self.tweet_time, tweetId))
        self.tweet_time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId in self.follower:
            user_set = self.follower[userId] | {userId}
        else:
            user_set = {userId}
        
        queue = []
        for userid in user_set:
            if userid in self.user_tweet:
                for tweet in self.user_tweet[userid]:
                    heapq.heappush(queue, tweet)
                    if len(queue) > 10:
                        heapq.heappop(queue)
        
        output = []
        while queue != []:
            _, twt_id = heapq.heappop(queue)
            output.append(twt_id)
        return output[::-1]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.follower:
            self.follower[followerId] = {followeeId}
        else:
            self.follower[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follower and followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)