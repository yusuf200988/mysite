from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


User = get_user_model()


class PostTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username = 'yusuf1',
            password = 'yusuf2009'
        )

        self.post = Post.objects.create(
            user = self.user,
            title = 'this is a title',
            description = 'this is description'
        )

    def test_string_model(self):
        post = Post(title='title for post')
        self.assertEqual(str(post), post.title)

    def test_post_model(self):
        self.assertEqual(f'{self.post.title}', 'this is a title')
        self.assertEqual(f'{self.post.description}', 'this is description')
        self.assertEqual(f'{self.post.user}', 'yusuf1')

    def test_post_list(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/post-list.html')

    def test_post_detail(self):
        response = self.client.get('/1')