import os
import requests
import sys

# Replace with your own API key and Canvas URL
#API_KEY = "12445~NaV5iCmN4pC9dHO8jwXyGftxyW3g3tzDotuxfDLeyFL0MYymVwyaVGPgz082Bhvu"
API_KEY = "12445~EYvs41866mImNCy0cmifubPWvV6yiYDXsl12B7IBMq2hoMkFA4LvEcZhOIwROghA"
CANVAS_URL = "https://canvas.msstate.edu/api/v1"

# Get the course ID from the command line argument
if len(sys.argv) != 2:
    print("Usage: python canvas_downloader.py COURSE_ID")
    sys.exit(1)
course_id = sys.argv[1]

# Make API request to get all the modules for the course
response = requests.get(f"{CANVAS_URL}/courses/{course_id}/modules", headers={"Authorization": f"Bearer {API_KEY}"})
if response.status_code != 200:
    print(f"Error: API request failed with status code {response.status_code}")
    print(response.content)
    sys.exit(1)
modules = response.json()
print(modules)
# Loop through each module and download the files in the module
for module in modules:
    # Make API request to get all the items in the module
    response = requests.get(module["items_url"], headers={"Authorization": f"Bearer {API_KEY}"})
    items = response.json()

    # Create a folder for the module
    module_folder = f"{module['name']} ({module['id']})"
    os.makedirs(module_folder, exist_ok=True)

    # Loop through each item in the module and download its attachments
    for item in items:
        # Make API request to get the item details
        response = requests.get(item["url"], headers={"Authorization": f"Bearer {API_KEY}"})
        item_details = response.json()

        # Loop through each attachment and download it
        for attachment in item_details.get("attachments", []):
            attachment_url = attachment["url"]
            file_name = attachment["filename"]

            # Download the file and save it in the module folder
            response = requests.get(attachment_url, headers={"Authorization": f"Bearer {API_KEY}"})
            with open(os.path.join(module_folder, file_name), "wb") as f:
                f.write(response.content)