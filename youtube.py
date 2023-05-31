from pytube import YouTube
from pytube.exceptions import VideoUnavailable ,RegexMatchError
import os
a=True 
while(a==True):
    try:
        link = input("Enter the YouTube video URL : ") 
        yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        a = input("360 as 1 or 720 as 2 or 1080 as 3 : ") 
        stream=False
        match a:
            case "1":
                stream = yt.streams.filter(res="360p", progressive=True, file_extension='mp4').first()
            case "2":
                stream = yt.streams.filter(res="720p",progressive=True, file_extension='mp4').first()
            case "3":
                stream = yt.streams.filter(res="1080p",progressive=True, file_extension='mp4').first()
            case _:
                print("1 or 2 or 3")
        stream.download('C:\\Users\\wasim\\Downloads')
    except VideoUnavailable:
        print('\nVideoUnavailable\n')
        a=True
    except KeyboardInterrupt:
        print('\nOkay\nsee you later bay bay')
        exit(0)
        a=False
    except InterruptedError:
        print('Interrupted Error')
        exit(0)
        a=False
    except RegexMatchError:
        print('Interrupted Error')
        exit(0)
        a=False
    except AttributeError:
        print('Attribute Error')
        exit(0)
        a=False
    else:
        print('Done')
        a=True
