from store.models import Customer

def create_customer_for_new_user(sender, **kwargs):
    if kwargs['created']:
        Customer.objects.create(user=kwargs['instance'])