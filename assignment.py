import requests
api_key = "e0f2b482eac71a0ac957deeca39d76b0"

"""
endpoint
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=e0f2b482eac71a0ac957deeca39d76b0

"""

movie_id = 2000
api_base_url = "https://api.themoviedb.org/3/"
api_version = 3
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&page=1"
print(endpoint)
##r = requests.get(endpoint)
##print(r.status_code)
##print(r.text)


api_base_url = "https://api.themoviedb.org/3/"
endpoint_path = f"search/movie"
search_query = "The Goonies"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
r = requests.get(endpoint)
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        movie_ids = set()
        for result in results:
            _id = result['id']
            print(result['title'], _id)
            movie_ids.add(_id)