from django.shortcuts import render
from .models import Tweet
from .forms import Tweetform
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Tweet_View(request):
    tweets= Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweetview.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method=='POST':
        form= Tweetform(request.POST, request.FILES)
        if form.is_valid():
            tweet= form.save(commit=False)
            tweet.user= request.user
            tweet.save()
            return redirect('Tweet_View')
    else:
        form=Tweetform()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    tweet= get_object_or_404(Tweet, pk=tweet_id, user= request.user)
    if request.method== 'POST':
        form= Tweetform(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet= form.save(commit=False)
            tweet.user= request.user
            tweet.save()
            return redirect('Tweet_View')
    else:
        form=Tweetform(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    tweet= get_object_or_404(Tweet, pk=tweet_id, user= request.user)
    if request.method== 'POST':
        tweet.delete()
        return redirect('Tweet_View')
    return render(request, 'tweet_deleteconf.html', {'tweet': tweet})