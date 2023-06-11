import xml.etree.ElementTree as ET

# Path to your Blogger XML file
xml_file_path = "./blog-06-11-2023.xml"

# Parse the XML file
tree = ET.parse(xml_file_path)

# Get the root element
root = tree.getroot()

# Retrieve image URLs
image_urls = []

# Access data in the Blogger XML file

# Example: Retrieve blog title
title_element = root.find(".//{http://www.w3.org/2005/Atom}title")
if title_element is not None:
    title = title_element.text
    print("Blog Title:", title)

# Example: Retrieve blog posts
for entry_element in root.findall(".//{http://www.w3.org/2005/Atom}entry"):
    post_title_element = entry_element.find(".//{http://www.w3.org/2005/Atom}title")
    post_published_element = entry_element.find(".//{http://www.w3.org/2005/Atom}published")

    content_element = entry_element.find(".//{http://www.w3.org/2005/Atom}content")
    media_content_element = entry_element.find(".//{http://search.yahoo.com/mrss/}content")
    
    if post_title_element is not None:
        post_title = post_title_element.text
        print("Post Title:", post_title)
        
    if post_published_element is not None:
        post_published = post_published_element.text
        print("Published:", post_published)


    # Check if content or media:content element exists
    if content_element is not None:
        image_url = content_element.get("src")
        if image_url is not None:
            image_urls.append(image_url)
    
    if media_content_element is not None:
        image_url = media_content_element.get("url")
        if image_url is not None:
            image_urls.append(image_url)

# Print the retrieved image URLs
for url in image_urls:
    print("Image URL:", url)