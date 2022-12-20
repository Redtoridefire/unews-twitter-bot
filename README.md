# unews-twitter-bot

This code first authenticates the API keys and access tokens using the tweepy library. It then follows a particular account using the create_friendship function provided by the tweepy library.

Next, it uses the requests library to send a GET request to the Google search API with the search query as a parameter. The search query includes the -site: operator to exclude certain websites from the search results.

The code then parses the response from the Google search API to extract the titles and URLs of the articles and stores them in a list. Finally, it uses the update_status function provided by the tweepy library to post a tweet with the titles and URLs of the first 3 articles in the list as a comment.

I hope this code helps you get started with creating your Twitter bot. Let me know if you have any questions or need further guidance.
