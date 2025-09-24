from django.db.models import Model, CharField, TextField


class Register(Model):
    full_name = CharField(max_length=255)
    tg_username = CharField(max_length=255, help_text='Telegram username kiriting')
    business = CharField(max_length=255)
    phone_number = CharField(max_length=255, help_text='Telegram phone number kiriting')
    address = CharField(null=True, blank=True, max_length=255, help_text='Manzilingizni kiriting')
    description = TextField(null=True, blank=True, help_text='Kompanya xaqida malumot kiriting !!!')
