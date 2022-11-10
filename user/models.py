from django.db import models
from pytils.translit import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now


class Film(models.Model):

    film_name = models.CharField(
        max_length=48,
        verbose_name='Название фильма'
    )
    film_id = models.IntegerField(
        verbose_name='id фильма на кинопоиске',
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    actors_in_film = models.ManyToManyField(
        'Staff',
        default=None
    )
    # directors_in_film = models.ManyToManyField(
    #     'Staff',
    #     default=None
    # )
    film_poster = models.ImageField(
        verbose_name='Постер',
        upload_to='images',
        blank=True
    )
    release_year = models.SmallIntegerField(
        verbose_name='Год выпуска'
    )
    slug = models.SlugField(
        blank=True,
        unique=True,
        verbose_name='URL'
    )

    class Meta:
        verbose_name = 'Название фильма'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.film_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.film_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('film', kwargs={'film_slug': self.slug})


class Post(models.Model):

    title = models.CharField(
        max_length=24,
        verbose_name='title'
    )
    subtitle = models.CharField(
        max_length=24,
        verbose_name='subtitle'
    )
    text = models.TextField(
        verbose_name='text'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='is published'
    )
    date_published = models.DateTimeField(
        default=now,
        verbose_name='date published'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='author'
    )
    slug = models.SlugField(
        blank=True,
        unique=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        db_table = 'blog_posts'
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ('date_published', )


class Staff(models.Model):

    staff_name = models.CharField(
        max_length=48,
        verbose_name='Имя актера'
    )
    staff_id = models.IntegerField(
        verbose_name='Id человека на кинопоиске',
        unique=True
    )
    year_of_birth = models.SmallIntegerField(
        verbose_name='Год рождения'
    )
    slug = models.SlugField(
        blank=True,
        unique=True,
        verbose_name='URL'
    )

    class Meta:
        verbose_name = 'Человека'
        verbose_name_plural = 'Люди'

    def __str__(self):
        return self.staff_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.staff_name)
        super().save(*args, **kwargs)
