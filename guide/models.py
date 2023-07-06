from django.db import models
from django.urls import reverse

class Post(models.Model):
    Game_Choices = [
        ('EscapeFromTarkov', 'Escape From Tarkov'),
        ('Test', "Test"),
    ]

    game = models.CharField(max_length=50, choices=Game_Choices)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True) # blank=True - поле не обязательное для заполнения
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    edited = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse('home')
    
#class Image(models.Model):
#    post = models.ForeignKey(Post, on_delete=models.CASCADE)
#    image = models.ImageField(upload_to='images/')