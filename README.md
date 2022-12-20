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
