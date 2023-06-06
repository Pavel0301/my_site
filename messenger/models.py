from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.


ROOM_NAME_MAX_LENGTH = 128



class MessageManager(models.Manager):
    """Manager for massage model"""

    def create(self, **obj_data):
        """
        """
        message = super().create(**obj_data)
        message.read_users.set([message.user])
        return message

def validate_room_name(value_to_validate):
    """Validate room name doesn't conflict with urlpatterns.

    Args:
        value_to_validate: room name to validate.

    Returns:
        validated room name.

    Raises:
        ValueError: if room name conflicts with urlpatterns.
    """
    if value_to_validate in {'direct', 'create'}:
        raise ValueError('You cannot create room named "create" or "direct".')
    return value_to_validate



class RoomType(models.TextChoices):
    """Class with choices of room type."""

    direct_messages = 1, 'Direct Messages'
    common_channel = 2, 'Common Channel'



class Room(models.Model):
    """Model of room objects"""
    name = models.CharField(max_length=ROOM_NAME_MAX_LENGTH, unique=True, validators=[validate_room_name])
    user = models.ManyToManyField(User, blank=False)
    type = models.CharField(max_length=2, choices=RoomType.choices)

    @property
    def members_count(self):
        """Get number of participants of the room.

        Returns:
            Number of participants of the room.
        """
        return self.user.count()

    def __str__(self):
        """Return string representation of the Room model.

        Returns:
            Room name and number of users online.
        """
        if self.type == RoomType.direct_messages:
            users = [part.username for part in self.user]
            return f'Direct: {" ".join.users}'
        return f'{self.name} ({self.members_count})'

class Message(models.Model):
    """Model of message objects"""
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='messages_creator')
    room = models.ForeignKey(Room,
                             on_delete=models.CASCADE)
    text = models.CharField(max_length=1024,
                            blank=False,
                            null=False)
    read_users = models.ManyToManyField(User, related_name='messages_read_users')
    date = models.DateTimeField(default=datetime.now, blank=True)


    # переопределение менеджера
    objects = MessageManager()





    #class Meta:
        #ordering = ['-timestamp']


    def __str__(self):
        return f'{self.user.username}:{self.text} [{self.timestamp}]'



class OnlineUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username