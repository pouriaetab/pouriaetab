"""Mirror the repos pinned on the GitHub profile into the README, as cards.

GitHub always renders its own Pinned section below the README; this keeps a copy
of it near the top. Runs in the daily workflow. Only the text between the
PINNED:START and PINNED:END markers is ever rewritten.
"""
import html
import json
import os
import re
import urllib.request

README = "README.md"
START, END = "<!-- PINNED:START -->", "<!-- PINNED:END -->"
QUERY = """query($login: String!) {
  user(login: $login) {
    pinnedItems(first: 6, types: REPOSITORY) {
      nodes { ... on Repository { name url description primaryLanguage { name color } } }
    }
  }
}"""


def fetch_pinned():
    if os.environ.get("NODES_JSON"):  # local testing without a token
        return json.loads(os.environ["NODES_JSON"])
    body = json.dumps({"query": QUERY, "variables": {"login": os.environ["LOGIN"]}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}",
                 "Content-Type": "application/json"},
    )
    data = json.load(urllib.request.urlopen(req))
    return data["data"]["user"]["pinnedItems"]["nodes"]


def card(repo):
    name = html.escape(repo["name"])
    desc = html.escape(repo.get("description") or "")
    lang = repo.get("primaryLanguage") or {}
    badge = ""
    if lang.get("name"):
        label = lang["name"].replace("-", "--").replace(" ", "_")
        color = (lang.get("color") or "#8b949e").lstrip("#")
        badge = (f'<img src="https://img.shields.io/badge/{label}-{color}?style=flat-square" '
                 f'alt="{html.escape(lang["name"])}" />')
    return (f'<td width="50%" valign="top">\n'
            f'<a href="{repo["url"]}"><b>📌 {name}</b></a><br>\n'
            f'<sub>{desc}</sub><br><br>\n{badge}\n</td>')


def render(repos):
    if not repos:
        return ""
    rows = []
    for i in range(0, len(repos), 2):
        rows.append("<tr>\n" + "\n".join(card(r) for r in repos[i:i + 2]) + "\n</tr>")
    return "### Pinned\n\n<table>\n" + "\n".join(rows) + "\n</table>\n\n---\n"


def main():
    text = open(README, encoding="utf-8").read()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        raise SystemExit("PINNED markers not found in README.md")
    block = f"{START}\n{render(fetch_pinned())}{END}"
    new = pattern.sub(lambda _: block, text)
    if new != text:
        open(README, "w", encoding="utf-8").write(new)
        print("README.md updated")
    else:
        print("pinned repos unchanged")


if __name__ == "__main__":
    main()
