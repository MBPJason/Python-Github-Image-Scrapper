import requests as request
from bs4 import BeautifulSoup as bs

# Made base Url for code dryness
baseUrl = "https://github.com/"
# Prompt user in terminal to give github name
github_user = input("Input GitHub User: ")
# Concatenated baseUrl and input from user prompt
url = baseUrl + github_user
# Send request for concat url
r = request.get(url)
# Set up soup variable with webpage response and parse through with python html parser
soup = bs(r.content, "html.parser")
# Grab user in webpage response image src link
profile_image = soup.find("img", {"alt": "Avatar"})["src"]
# Display in console
print(f"This is {github_user} profile image link: {profile_image}")

# Ask if user wants to get users who webpage user follows
getFollowers = input(f"Would you like to see who {github_user}'s follows? (Y/N): ")

# Function to get users
def displayFollowers():
    # Concat searched user url for followers
    following = url + "?tab=following"
    # Send request for concat following url
    f_request = request.get(following)
    # Grab html page of user following list
    f_soup = bs(f_request.content, "html.parser")
    # Parses the web page for all img tags with a width of 50
    f_image = f_soup.find_all("img", {"width": "50"})

    # Set up empty user list
    users = []
    # Loop through given soup response of filtered img tags in webpage
    for image in f_image:
        # Split the alt attribute to get username
        u_name = image["alt"].split("@")
        # Make user dictionary
        user = {
            "username": u_name[1],  # True user name from spilt
            "user_link": image.parent[
                "href"
            ],  # Go to the parent of the img tag and grab href value
            "user_img": image["src"],  # Img link grabbed from source
        }
        # Append info to user list variable
        users.append(user)

    # Display in console
    print(f"Here is the list of users {github_user} follows")
    # Loop through users print format them correctly and display them in terminal
    for u in users:
        print(
            f"Username: {u['username']} User Image: {u['user_img']} Userlink: {baseUrl + u['user_link']}\n"
        )


# Set up if/else statement
if getFollowers.lower() == "n":  # Check for no response
    print("Alright no users for you")
elif getFollowers.lower() == "y":  # Check for yes response
    displayFollowers()  # Call for function
else:
    print("Please choose 'Y' or 'N' next time")  # Print "error" response
