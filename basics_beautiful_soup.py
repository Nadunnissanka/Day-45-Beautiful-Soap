from bs4 import BeautifulSoup

with open(file="website.html", mode="r") as webpage:
    content = webpage.read()
    print(content)

soup = BeautifulSoup(content, "html.parser")
# To get the webpage title with tag
print(soup.title)
# To get the webpage title tag
print(soup.title.name)
# To get webpage title content as a string
print(soup.title.string)

# To get all the anchor tags
all_anchor_tags = soup.find_all(name="a")
# this will make a list call all_anchor_tags
print(all_anchor_tags)
# you can loop through all_anchor_tags list
for tag in all_anchor_tags:
    # to get text of all a tags in all_anchor_tags list
    print(tag.getText())
    # to get a specific html attributes like eg: href
    print(tag.get("href"))

# select html lines based on its attributes
heading = soup.find(name="h1", id="name")
print(heading)
print(heading.getText())

# [Selecting a Class] select html line based on its tag name and class name
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.getText())
print(section_heading.get("class"))

# using css selector method inside beautiful soup
# selector="p a" means anchor tag is inside a paragraph tag
link = soup.select(selector="p a")
print(link)

# selecting based on id selector
name = soup.select(selector="#name")
print(name)
