# unews-twitter-bot

This code first authenticates the API keys and access tokens using the tweepy library. It then follows a particular account using the create_friendship function provided by the tweepy library.

Next, it uses the requests library to send a GET request to the Google search API with the search query as a parameter. The search query includes the -site: operator to exclude certain websites from the search results.

The code then parses the response from the Google search API to extract the titles and URLs of the articles and stores them in a list. Finally, it uses the update_status function provided by the tweepy library to post a tweet with the titles and URLs of the first 3 articles in the list as a comment.

Code allows you to exclude certain websites or domains of your choosing from the search results. To do this, you can use the -site: operator in your search query.

For example, if you want to exclude all results from the website example.com, you can use the search query SEARCH_QUERY -site:example.com, where SEARCH_QUERY is the search query you want to use.

You can also exclude multiple websites or domains by including multiple -site: operators in your search query. For example, to exclude results from example.com and example.net, you can use the search query SEARCH_QUERY -site:example.com -site:example.net.

You can include the websites you want to search in the code by specifying them in your search query.

For example, if you want to search for articles on the websites example.com and example.net, you can use the search query site:example.com OR site:example.net SEARCH_QUERY, where SEARCH_QUERY is the search query you want to use.

This will search for articles that are published on either example.com or example.net and match the SEARCH_QUERY criteria.

Alternatively, you can also use the inurl: operator in your search query to search for articles that have a particular string in their URL. For example, to search for articles on example.com and example.net that have the string article in their URL, you can use the search query inurl:article (site:example.com OR site:example.net).

Make sure you tweepy requestsinstalled

To run the code I provided, you will need to have the following files:

A Python file: This is where you will write and run the code. You can name the file anything you like, such as twitter_bot.py.

API keys and access tokens: You will need to obtain API keys and access tokens for your Twitter Developer account. These will allow you to authenticate your bot and access the Twitter API. You can find more information on how to obtain these here: https://developer.twitter.com/en/docs/twitter-api/getting-started/authentication

A Google API key and CX: You will also need to obtain a Google API key and CX to use the Google search API. You can find more information on how to obtain these here: https://developers.google.com/custom-search/v1/overview

Libraries: The code I provided uses the tweepy and requests libraries. These libraries provide functions that allow you to access and interact with the Twitter and Google APIs, respectively. Make sure you have these libraries installed in your Python environment by running the following command:
