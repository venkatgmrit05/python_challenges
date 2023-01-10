import requests

# send a request to the URL and retrieve the video data
url = "http://example.com/path/to/video.mp4"
url = "https://d.tube/#!/v/suleman00/QmScetbWyVDnUzHwJgEufmXTK58D4eNkbYybYDAiE17F2t"
response = requests.get(url)

# write the data to a file
with open("video.mp4", "wb") as f:
    f.write(response.content)
