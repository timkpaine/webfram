import requests

data = {'term': 'dog park'}
resp = requests.get('https://api.yelp.com/v3/businesses/search')

# /businesses/search
# This endpoint returns up to 1000 businesses based on the provided search criteria. It has some basic information about the business. To get detailed information and reviews, please use the business id returned here and refer to /businesses/{id} and /businesses/{id}/reviews endpoints.

# Note: at this time, the API does not return businesses without any reviews.

# Request
# GET https://api.yelp.com/v3/businesses/search
# Parameters
# These parameters should be in the query string.

# Name    Type    Description
# term    string  Optional. Search term (e.g. "food", "restaurants"). If term isn’t included we search everything. The term keyword also accepts business names such as "Starbucks".
# location    string  Required if either latitude or longitude is not provided. Specifies the combination of "address, neighborhood, city, state or zip, optional country" to be used when searching for businesses.
# latitude    decimal Required if location is not provided. Latitude of the location you want to search nearby.
# longitude   decimal Required if location is not provided. Longitude of the location you want to search nearby.
# radius  int Optional. Search radius in meters. If the value is too large, a AREA_TOO_LARGE error may be returned. The max value is 40000 meters (25 miles).
# categories  string  Optional. Categories to filter the search results with. See the list of supported categories. The category filter can be a list of comma delimited categories. For example, "bars,french" will filter by Bars and French. The category identifier should be used (for example "discgolf", not "Disc Golf").
# locale  string  Optional. Specify the locale to return the business information in. See the list of supported locales.
# limit   int Optional. Number of business results to return. By default, it will return 20. Maximum is 50.
# offset  int Optional. Offset the list of returned business results by this amount.
# sort_by string  Optional. Sort the results by one of the these modes: best_match, rating, review_count or distance. By default it's best_match. The rating sort is not strictly sorted by the rating value, but by an adjusted rating value that takes into account the number of ratings, similar to a bayesian average. This is so a business with 1 rating of 5 stars doesn’t immediately jump to the top.
# price   string  Optional. Pricing levels to filter the search result with: 1 = $, 2 = $$, 3 = $$$, 4 = $$$$. The price filter can be a list of comma delimited pricing levels. For example, "1, 2, 3" will filter the results to show the ones that are $, $$, or $$$.
# open_now    boolean Optional. Default to false. When set to true, only return the businesses open now. Notice that open_at and open_now cannot be used together.
# open_at int Optional. An integer represending the Unix time in the same timezone of the search location. If specified, it will return business open at the given time. Notice that open_at and open_now cannot be used together.
# attributes  string  Optional. Additional filters to restrict search results. Possible values are:
# hot_and_new - Hot and New businesses
# request_a_quote - Businesses that have the Request a Quote feature
# waitlist_reservation - Businesses that have an online waitlist
# cashback - Businesses that offer Cash Back
# deals - Businesses that offer Deals
# gender_neutral_restrooms - Businesses that provide gender neutral restrooms
# You can combine multiple attributes by providing a comma separated like "attribute1,attribute2". If multiple attributes are used, only businesses that satisfy ALL attributes will be returned in search results. For example, the attributes "hot_and_new,cashback" will return businesses that are Hot and New AND offer Cash Back.
# Note
# Using the offset and limit parameters, you can get up to 1000 businesses from this endpoint if there are more than 1000 results. If you request a page out of this 1000 business limit, this endpoint will return an error.

# Response Body
# {
#   "total": 8228,
#   "businesses": [
#     {
#       "rating": 4,
#       "price": "$",
#       "phone": "+14152520800",
#       "id": "four-barrel-coffee-san-francisco",
#       "is_closed": false,
#       "categories": [
#         {
#           "alias": "coffee",
#           "title": "Coffee & Tea"
#         }
#       ],
#       "review_count": 1738,
#       "name": "Four Barrel Coffee",
#       "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
#       "coordinates": {
#         "latitude": 37.7670169511878,
#         "longitude": -122.42184275
#       },
#       "image_url": "http://s3-media2.fl.yelpcdn.com/bphoto/MmgtASP3l_t4tPCL1iAsCg/o.jpg",
#       "location": {
#         "city": "San Francisco",
#         "country": "US",
#         "address2": "",
#         "address3": "",
#         "state": "CA",
#         "address1": "375 Valencia St",
#         "zip_code": "94103"
#       },
#       "distance": 1604.23,
#       "transactions": ["pickup", "delivery"]
#     },
#     // ...
#   ],
#   "region": {
#     "center": {
#       "latitude": 37.767413217936834,
#       "longitude": -122.42820739746094
#     }
#   }
# }
# Name    Type    Description
# total   int The total number of business Yelp finds based on the search criteria. Sometimes, the value may exceed 1000. In such case, you still can only get up to 1000 businesses. total may be limited to 40 for non-default sorts such as "distance" and "review_count".
# businesses  object[]    A list of business Yelp finds based on the search criteria.
# businesses[x].categories    object[]    A list of category title and alias pairs associated with this business.
# businesses[x].categories[x].alias   string  Alias of a category, when searching for business in certain categories, use alias rather than the title.
# businesses[x].categories[x].title   string  Title of a category for display purpose.
# businesses[x].coordinates   object  The coordinates of this business.
# businesses[x].coordinates.latitude  decimal The latitude of this business.
# businesses[x].coordinates.longitude decimal The longitude of this business.
# businesses[x].display_phone string  Phone number of the business formatted nicely to be displayed to users. The format is the standard phone number format for the business's country.
# businesses[x].distance  decimal The distance in meters from the search location. This returns meters regardless of the locale.
# businesses[x].id    string  Yelp id of this business.
# businesses[x].image_url string  URL of photo for this business.
# businesses[x].is_closed bool    Whether business has been (permanently) closed
# businesses[x].location  object  The location of this business, including address, city, state, zip code and country.
# businesses[x].location.address1 string  Street address of this business.
# businesses[x].location.address2 string  Street address of this business, continued.
# businesses[x].location.address3 string  Street address of this business, continued.
# businesses[x].location.city string  City of this business.
# businesses[x].location.country  string  ISO 3166-1 alpha-2 country code of this business.
# businesses[x].location.display_address  string[]    Array of strings that if organized vertically give an address that is in the standard address format for the business's country.
# businesses[x].location.state    string  ISO 3166-2 (with a few exceptions) state code of this business.
# businesses[x].location.zip_code string  Zip code of this business.
# businesses[x].name  string  Name of this business.
# businesses[x].phone string  Phone number of the business.
# businesses[x].price string  Price level of the business. Value is one of $, $$, $$$ and $$$$.
# businesses[x].rating    decimal Rating for this business (value ranges from 1, 1.5, ... 4.5, 5).
# businesses[x].review_count  int Number of reviews for this business.
# businesses[x].url   string  URL for business page on Yelp.
# businesses[x].transactions  string[]    A list of Yelp transactions that the business is registered for. Current supported values are "pickup", "delivery", and "restaurant_reservation".
# region  dict    Suggested area in a map to display results in.
# region.center   dict    Center position of map area.
# region.center.latitude  decimal Latitude position of map bounds center.
# region.center.longitude decimal Longitude position of map bounds center.
