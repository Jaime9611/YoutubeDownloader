from pytube import YouTube


# Give the link:
# link = 'https://www.youtube.com/watch?v=2Vv-BfVoq4g'

def download_video(link):
    try:
        yt = YouTube(link) # YouTube object
    except:
        print('Connection Error.')

    stream = yt.streams.filter(progressive=True).first()


    try:
        stream.download()
    except:
        print('Some Error.')

    print('Download Completed...')
