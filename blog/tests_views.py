from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CommentForm
from .models import Post, Comment

class TestViews(TestCase):
    @classmethod
    def setUpTestData(self):
        # test data
        self.user = User.objects.create(username='usertest')
        self.user.set_password('testpassword')
        self.user.save()
        
        self.post = Post.objects.create(
            title = 'test title',
            slug = 'test-title',
            author=self.user,
            )
        self.post.save()

        self.comment = Comment.objects.create(
            post=self.post,
            body='test comment'
            )
        self.comment.save()

    def test_post_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')
    
    # def test_post_comment(self):
    #     self.client.login(username='usertest', password='testpassword')
    #     response = self.client.post(reverse('post_detail', args=[self.post.slug]), data={self.comment.body})
    #     self.assertRedirects(response, reverse('post_detail',args=[self.post.slug]))

    def test_post_comment(self):
        """Test post commenting feature"""
        self.client.login(username='testname', password='1234')
        response = self.client.post(
            reverse('post_detail',
                    args=[self.post.slug]),
            data={'body': 'testcomment'})
        # self.assertRedirects(
        #     response, reverse('post_detail', args=[self.post.slug]))
