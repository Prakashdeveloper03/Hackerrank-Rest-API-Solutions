import requests
import json

#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#


def getNumDraws(year):
    url1 = f"https://jsonmock.hackerrank.com/api/football_matches?year={str(year)}"
    response1 = requests.get(url1)
    result1 = json.loads(response1.content)
    curr_1 = 1
    total_page_url_1 = result1["total_pages"]
    total = 0
    for i in range(12):
        url1 = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1goals={1}&team2goals={1}".format(
            year, i, i
        )
        response1 = requests.get(url1)
        result1 = json.loads(response1.content)
        print(result1["total"])
        total += result1["total"]
    return total
