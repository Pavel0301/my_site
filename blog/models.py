from enum import unique

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField

from django.utils.text import slugify

from my_site.settings import TIME_ZONE

# signals dev
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from django.template.defaultfilters import slugify as django_slugify
alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):

    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


# Create your models here.


class Post(models.Model):
    # позже удалить null
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=150, db_index=True, help_text="Title of the post, 150 symbols max", verbose_name="Заголовок")
    content = RichTextField(max_length=5000, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now) #auto_now_add=True,)
    date_updated = models.DateTimeField(auto_now=True)
    # в url использование slug обязательно добавляем id + get_absolute_url()
    slug = models.SlugField(max_length=50, unique=True)

    likes = models.ManyToManyField(User, related_name="posts_likes", blank=True, )
    reply = models.ForeignKey('self', null=True, blank=True, related_name='feedback', on_delete=models.CASCADE)
    saves_posts = models.ManyToManyField(User, related_name="blog_posts_save", blank=True, verbose_name='Сохранённые посты пользователя')


    def get_absolute_url(self):
        return reverse('blog_urls:post-detail', kwargs={'slug': self.slug})#'slug': self.slug

    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'


    def get_total_likes(self):
        return self.likes.count()

    def total_saves_posts(self):
        return self.saves_posts

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)





    def __str__(self):
        return self.title


    # signals

@receiver(pre_save, sender=Post)
def prepopulated_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)







