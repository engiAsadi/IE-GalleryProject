from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

from .models import Post

#from django.shortcuts import render

# Create your views here.


#def home(request):
#    return render(request, 'gallery/home.html')


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post, slug=slug)



#@login_required
def like_or_dislike(request, pk):
    # print(request.resolver_match)
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    post_likes_users = post.likes.all()
    count = post_likes_users.count()

    if user.is_anonymous:
        return JsonResponse({
            'likes': count,
            'status': 'not_login',
        })

    if user in post_likes_users:
        post.likes.remove(user)
        count -= 1
        user_in_likes = False
    else:
        post.likes.add(user)
        count += 1
        user_in_likes = True

    return JsonResponse({
        'status': user.is_authenticated,
        'likes': count,
        'user_in_likes': user_in_likes,
    })
