import json

# File paths
output_file_path = "alpha/posts.json"

# Initialize an empty list to hold each post as a dictionary
posts = []

# Read the content of the posts.txt file
with open('alpha/posts.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Split the content of the file using the separator between posts ("--------------------")
post_contents = content.split("--------------------")

# Create a dictionary for each post and add it to the list
for post in post_contents:
    # Remove leading/trailing whitespaces and check if the post is not empty
    post = post.strip()
    
    if post == "Media/Other Content":
        continue
    
    if post:
        posts.append({"content": post})

# Write the list of posts into a JSON file
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(posts, json_file, ensure_ascii=False, indent=4)

print(f"Posts have been successfully saved to {output_file_path}")
