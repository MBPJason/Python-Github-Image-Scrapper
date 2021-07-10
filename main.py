from enum import unique
import requests as request
from bs4 import BeautifulSoup as bs

baseUrl = "https://github.com/"
github_user = input("Input GitHub User: ")
url = baseUrl + github_user
r = request.get(url)
soup = bs(r.content, "html.parser")
profile_image = soup.find("img", {"alt": "Avatar"})["src"]
print(f"This is {github_user} profile image link: {profile_image}")
getFollowers = input(f"Would you like to see who {github_user}'s follows? (Y/N): ")


def displayFollowers():
    following = url + "?tab=following"
    f_request = request.get(following)
    f_soup = bs(f_request.content, "html.parser")
    f_image = f_soup.find_all("img", {"width": "50"})
    users = []
    for image in f_image:
        u_name = image["alt"].split("@")
        user = {
            "username": u_name[1],
            "user_link": image.parent["href"],
            "user_img": image["src"],
        }
        users.append(user)
    print(f"Here is the list of users {github_user} follows")
    for u in users:
        print(
            f"Username: {u['username']} User Image: {u['user_img']} Userlink: {baseUrl + u['user_link']}\n"
        )
    # print(users)


if getFollowers.lower() == "n":
    print("Alright no users for you")
elif getFollowers.lower() == "y":
    displayFollowers()
else:
    print("Please choose 'Y' or 'N' next time")
