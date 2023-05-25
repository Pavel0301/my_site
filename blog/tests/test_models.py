from blog.models import Post
from django.db import models
import pytest



# далее разобраться что тестировать, а что нет.
# Если то не сработало, добавьте так
# @pytest.mark.django_db(transaction=True)


@pytest.mark.django_db(transaction=True)
def test_title_create():
    article = Post.objects.create(title="article")
    assert article.title == "article"

@pytest.mark.django_db(transaction=True)
def test_content_create():
    article1 = Post.objects.create(content="article1")
    assert article1.content == "article1"


