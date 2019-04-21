import requests
import os
url = "https://image.vorkers.com/resize/160x-/logo/company/1416-a05725c5cde1f15a3e83b0eca3b09ccc.png"
root = "/Users/mars007/git_repository/WebCrawlerAndInformationExtraction/week01/images/"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(path):
        os.mkdir(root)
    if not os.path.exists(path):
            r= requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("save file succesful")
    else:
        print("the file exists")
except:
    print("get file failed")