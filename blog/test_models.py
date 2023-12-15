from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class TestViews(TestCase):
    @classmethod
    def setUpTestData(self):
        # test data
        self.user = User.objects.create(username='usertest')
        self.user.set_password('testpassword')
        self.user.save()

        self.post = Post.objects.create(
            title='test title',
            slug='test-title',
            author=self.user,
        )
        self.post.save()

        self.comment = Comment.objects.create(
            post=self.post,
            body='test comment'
        )
        self.comment.save()
