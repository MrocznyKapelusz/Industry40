cities = """
Amsterdam Athens    Barcelona Berlin   Bucarest  Budapest Brussels Copenhagen
Dublin    Edinburgh Gibraltar Helsinki Istanbul  Kiev     Lisbon   London
Madrid    Milan     Moscow    Munich   Nantes    Oslo     Paris    Prague
Reykjavik Riga      Rome      Sofia    Stockholm Toulouse Vilnius  Warsaw
"""

cities = cities.split()
n = len(cities) # 32

print(n)

import googlemaps

proxy_dict = {}  # from home

# if you need to set the proxy
# proxy_dict = { 'proxies': {"http": ">>>> fill here <<<<",
#                            "https": ">>>> fill here <<<<"} }

# Be careful, your API key is:
#   - is exactly 40 characters long
#   - starts with AIza
client = googlemaps.Client(key=">>>> fill in your API key <<<<",
                           requests_kwargs=proxy_dict)

coords = [client.geocode(c) for c in cities]
coords = [c[0]['geometry']['location'] for c in coords]

# Quick check...
coords[:3]