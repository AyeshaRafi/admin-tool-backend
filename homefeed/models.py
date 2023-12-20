from django.db import models
from django.db.models import Max

from utils.models import ModelWithUUID

# Model for Homefeed elements (To-do and Call to Action)
class HomefeedElement(ModelWithUUID):
    TODO = 1
    CALL_TO_ACTION = 2
    ELEMENT_TYPES = [
        (TODO, 'Todo'),
        (CALL_TO_ACTION, 'Call to Action'),
    ]
    
    element_type = models.IntegerField(
        choices=ELEMENT_TYPES,
        default=TODO,
    )
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    image_url = models.URLField(blank=True, null=True)  # Only for Call to Action
    link_url = models.URLField(default='https://google.com')  # Only for Call to Action
    
    class Meta:
        ordering = ['order']
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new object (not yet saved in the database)
            last_order = HomefeedElement.objects.aggregate(Max('order')).get('order__max')
            self.order = (last_order or 0) + 1  # Increment the last order by 1
        super(HomefeedElement, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_element_type_display()} - {self.title}"
