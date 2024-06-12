from django.shortcuts import render
from pytube import YouTube
from django.http import HttpResponse

def home(request):
    return render(request, 'downloader/home.html')

def download_video(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        try:
            yt = YouTube(video_url)
            video = yt.streams.get_highest_resolution()
            video.download()
            return HttpResponse(f'Successfully downloaded: {yt.title}')
        except Exception as e:
            return HttpResponse(f'Error: {e}')
    return HttpResponse('Invalid request')
