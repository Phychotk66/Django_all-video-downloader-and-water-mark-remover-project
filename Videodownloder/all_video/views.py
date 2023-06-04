from django.shortcuts import render, redirect
from .models import Video
from moviepy.editor import VideoFileClip

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        Video.objects.create(title=title, url=url)
        return redirect('home')

    videos = Video.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'videos': videos})

def download_video(request, video_id):
    video = Video.objects.get(id=video_id)
    # Code to download video file using the video.url
    # For example, you can use a library like youtube-dl
    return redirect('home')

def remove_watermark(request, video_id):
    video = Video.objects.get(id=video_id)
    video_path = 'path/to/video/file.mp4'  # Replace with the actual path to the downloaded video file

    # Remove watermark using moviepy
    clip = VideoFileClip(video_path)
    # Code to remove the watermark from the video clip
    # For example, you can use the .subclip() method to remove a specific portion with the watermark

    # Save the processed video
    output_path = 'path/to/output/file.mp4'  # Replace with the desired output path and filename
    clip.write_videofile(output_path)

    # Update the watermark_removed field in the database
    video.watermark_removed = True
    video.save()

    return redirect('home')
