from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5

class PostDetail(View):
    def get(self,request,slug,*args,**kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        comment_count = post.comments.filter(approved=True).count()
        # liked = False
        # if post.likes.filter(id=self.request.user.id).exists():
        #     liked=True
        
        return render(
            request,
            'post_detail.html',
            {
                'post':post,
                'comments':comments,
                'commented':False,
                # 'liked':liked,
                'comment_form':CommentForm()
            }
        )

    def post(self,request,slug,*args,**kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).count()
        # liked = False
        # if post.likes.filter(id=self.request.user.id).exists():
        #     liked=True
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.first_name=request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post':post,
                'comments':comments,
                'commented':True,
                # 'liked':liked,
                'comment_form':CommentForm()
            }
        )
class Edit(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Comment
    template_name = 'comment_edit.html'
    form_class = CommentForm

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('post_detail', kwargs={'slug': slug})
    
    def form_valid(self, form):
        form.instance.first_name = self.request.user.username
        return super().form_valid(form)
    
    def test_func(self):
        comment = self.get_object()
        if self.request.user.username == comment.first_name:
            return True
        return False    


class Delete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    form_class = CommentForm
    # success 
    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('post_detail', kwargs={'slug': slug})

    def form_valid(self, form):
        form.instance.first_name = self.request.user.username
        return super().form_valid(form)

    # check if logged in user is the writer of comment
    def test_func(self):
        comment = self.get_object()
        if self.request.user.username == comment.first_name:
            return True
        return False   




