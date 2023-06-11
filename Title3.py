import os
import re
import xml.etree.ElementTree as ET

# Path to your Blogger XML file
xml_file_path = "./blog-06-11-2023.xml"

# Parse the XML file
tree = ET.parse(xml_file_path)

# Get the root element
root = tree.getroot()

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

    if post_title_element is not None and post_title_element.text is not None:
        post_title = post_title_element.text
        print("Post Title:", post_title)

        if post_published_element is not None:
            post_published = post_published_element.text
            print("Published:", post_published)

        if content_element is not None:
            post_description = content_element.text
            print("Description:", post_description)

        # Create the parent directory if it doesn't exist
        parent_folder = "sample"  # Specify the parent folder name
        if not os.path.exists(parent_folder):
            os.makedirs(parent_folder)

        # Create a valid file name by replacing invalid characters
        valid_title = re.sub(r"[^\w\s-]", "", post_title).strip().lower()
        valid_title = re.sub(r"[-\s]+", "_", valid_title)

        # Create a markdown file
        file_name = f"{valid_title}.md"
        file_path = os.path.join(parent_folder, file_name)

        with open(file_path, "w") as f:
            f.write(f"# {post_title}\n\n")
            f.write(f"Published: {post_published}\n\n")
            f.write(f"Description: {post_description}\n\n")
            f.write("Write your content here...")

        print(f"Markdown file created: {file_path}")
    else:
        print("Skipping entry without a valid title")
