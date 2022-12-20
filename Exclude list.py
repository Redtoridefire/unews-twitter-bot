# Use the Google Search API to search for the title within the "example.com" domain
# Replace "YOUR_GOOGLE_API_KEY" with your own API key
# This exclude file is not needed to run the bot all excluding can be done by editing the main code, this is for those who like things seperate
params = {
    'q': title,
    'key': 'YOUR_GOOGLE_API_KEY',
    'siteSearch': 'example.com',
}
r = requests.get('https://www.googleapis.com/customsearch/v1', params=params)
results = r.json()['items']
