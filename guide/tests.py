from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = 'testuser',
            password = '12345678'
        )

        cls.post = Post.objects.create(
            game = 'test game',
            title = 'good title',
            body = 'somebody',
            img = r'C:\Users\Jenn\Pictures\Donut.png',
        )

    def test_homepage(self):
        self.assertEqual(self.post.game, 'test game')
        self.assertEqual(self.post.title, 'good title')
        self.assertEqual(self.post.body, 'somebody')
        self.assertEqual(self.post.img, r'C:\Users\Jenn\Pictures\Donut.png')

    def test_homepage_lsitview(self):
        responce = self.client.get('/')

        self.assertEqual(responce.status_code, 200)
        self.assertTemplateUsed(responce, 'base.html')
        self.assertTemplateUsed(responce, 'home.html')
        self.assertTemplateNotUsed(responce, 'nothing.html')

        self.assertContains(responce, 'good title')
        self.assertContains(responce, 'test game')

    def test_postcreate_createview(self):
        responce = self.client.post(
            reverse('post_create'),
            {
            'game': 'new game',
            'title': 'new good title',
            'body': 'new somebody',
            }
        )

        self.assertEqual(responce.status_code, 302)
        self.assertEqual(Post.objects.last().game, 'new game')
        self.assertEqual(Post.objects.last().title, 'new good title')
        self.assertEqual(Post.objects.last().body, 'new somebody')

    def test_postdetail_detailview(self):
        responce = self.client.get(reverse('post_detail', kwargs={"pk": self.post.pk}))
        no_responce = self.client.get("/post/10000")

        self.assertEqual(responce.status_code, 200)
        self.assertEqual(no_responce.status_code, 404)

    def test_postdelete_deleteview(self):
        responce = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(responce.status_code, 302)
        