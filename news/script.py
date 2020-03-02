import requests
import json


def news():
    req = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=4f7910cc41594d8ea006483ca9ba6e9b"
    )
    data = req.text
    parsed_data = []
    # endpoints ==> /v2/top-headlines
    #               /v2/everything
    #               /v2/sources - returns information (including name, description, and category) about the most notable sources we index
    # country ==> The 2-letter ISO 3166-1 code of the country
    # category ==> business entertainment general health science sports technology
    for d in json.loads(data)["articles"]:
        parsed_data.append(d)
    if parsed_data != "":
        return json.dumps(parsed_data)
        # status = json_data['status']
        # total_results = json_data['totalresults']
        # articles = json_data['articles']

