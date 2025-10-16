import factory
from django.conf import settings
from pgallery.models import Gallery, Photo


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f"user_{n}")
    email = factory.Sequence(lambda n: f"user_{n}@example.com")

    class Meta:
        model = settings.AUTH_USER_MODEL


class GalleryFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    slug = factory.Sequence(lambda n: f"gallery_{n}")

    class Meta:
        model = Gallery


class PhotoFactory(factory.django.DjangoModelFactory):
    gallery = factory.SubFactory(GalleryFactory)
    author = factory.LazyAttribute(lambda obj: obj.gallery.author)
    image = factory.django.ImageField(width=1024, height=768)

    class Meta:
        model = Photo
