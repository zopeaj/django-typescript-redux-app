from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from video.models import Video
# Create your views here.

@login_required
def like_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    hasRated = False
    for ratedUser in video.ratedUsers.all():
        if ratedUser.username == request.user.username:
            hasRated = True
            break
    if hasRated == False:
        video.likes = video.likes + 1
        video.ratedUsers.add(request.user)
        video.save()
    else:
        print("HAS ALREADY VOTED!")

    return redirect('/video_details/' + str(video_id))


@login_required
def dislike_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    hasRated = False
    for ratedUser in video.ratedUsers.all():
        if ratedUser.username == request.user.username
            hasRated = True
            break
    if hasRated == False:
        video.dislikes = video.dislikes + 1
        video.ratedUsers.add(request.user)
        video.save()
    else:
        print("HAS ALREADY VOTED!")

    return redirect('/video_details/' + str(video_id))

