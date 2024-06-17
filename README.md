# YouTube_uploader_with_subtitle
## Demo
* [Usage](https://youtu.be/tQhnm6lCdGU?si=DpdP1KxgF3I4P17h)
## How to build
* Environment：python3
## How to run
* Put multiple client_secret_0.json, client_secret_1.json...... in client_secret folder, check reference first!
* Put the video that needs to be uploaded in the upload folder.
```
-upload/videofolder1/a.mp4 upload/videofolder1/a.srt(optional)
-upload/videofolder2/b.mp4 upload/videofolder2/b.srt(optional)
```
1. Generate command
```python command.py > command.txt```

~~2. copy command to run.sh~~
2. Directly run ```./run.sh```
## Other
* run.sh will remove upload_video.py-oauth2.json after a client_secret exceeds the quota of the YouTube Data API.
## Reference
* [Python3 Tutorial - Upload Videos using the YouTube Data API](https://youtu.be/eq-mjehACe4?si=jg11rcC1EKT6V6M6)
* [client_secret](https://developers.google.com/api-client-library/dotnet/guide/aaa_client_secrets)
* [Youtube api-samples](https://github.com/youtube/api-samples/blob/master/python/captions.py)
* [Understanding YouTube API Quota Limits](https://github.com/ThioJoe/YT-Spammer-Purge/wiki/Understanding-YouTube-API-Quota-Limits)
