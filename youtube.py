from pytube import YouTube
YouTube('<link>').streams.first().download('<download location>')
print('Downloading is done..')
