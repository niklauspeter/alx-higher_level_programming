#!/usr/bin/python3
"""Script lists the 10 most recent commits made on a given GitHub repository.
start by importing the required requests and sys packages.
Get the repository name and owner name from the command line arguments
using the sys module.
Set the API endpoint URL using format method
to insert the repo and owner names into the URL string.
Make an API call using the requests.get method
and passing the URL as a parameter.
Chheck the response status code
to ensure the API call was successful.
If the API call was successful,
iterate over the first 10 commits in the response (JSON)
and display the commit hash, author name, and date.
If the API call was not successful, display the error status code.
"""
import requests
import sys


if __name__ == "__main__":
    # url = "https://api.github.com/repos/{}/{}/commits".format(
    #     sys.argv[2], sys.argv[1])

    # response = requests.get(url)
    # commits = response.json()
    # try:
    #     for i in range(10):
    #         print("{}: {}".format(
    #             commits[i].get("sha"),
    #             commits[i].get("commit").get("author").get("name")))
    # except IndexError:
    #     pass

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits?author={owner_name}&per_page=10"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        exit()

    commits = response.json()

    for commit in commits:
        sha = commit["sha"]
        author = commit["commit"]["author"]["name"]
        print(f"{sha}: {author}")
