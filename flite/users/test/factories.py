import factory


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    id = factory.Faker('uuid4')
    username = factory.Sequence(lambda n: f'testuser{n}')
    password = factory.Faker('password', length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False

user = UserFactory()

class TransactionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.Transaction'
        django_get_or_create = ('owner',)
    
    id = factory.Faker('uuid4')
    owner = user
    status = 'successful'
    reference = factory.Sequence(lambda n: f'12345678{n}{n}')
    amount = 0.0
    new_balance = 0.0
