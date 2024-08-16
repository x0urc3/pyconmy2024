import base64
import requests
from IPython.display import Image, display

def mermaid_ink(graph, filename = None):
    graphbytes = graph.encode("utf8")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")

    image_url = "https://mermaid.ink/img/" + base64_string

    if filename:
        # Fetch the image and save it as a PNG file
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed to retrieve the image. Status code: {response.status_code}")
    else:
        display(Image(url=image_url))

