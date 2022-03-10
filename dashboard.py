import json
from urllib.request import urlopen


def read_json(commit_hash):
    json_file = f"./benchmark/json/{commit_hash}.json"


def fetch_commits():
    commitsLink = "https://api.github.com/repos/NethermindEth/warp-ts/commits"
    f = urlopen(commitsLink)
    commits = json.loads(f.readline())
    commit_hashes = [commit["sha"] for commit in commits]
    return commit_hashes[-1::-1]
