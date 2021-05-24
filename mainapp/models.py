from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
from django.utils import timezone

User = get_user_model()

def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


def get_product_url(obj, viewname):
    
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug })



class LatestProductManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products

class LatestProducts:

    objects = LatestProductManager()


class CategoryManager(models.Manager):

    CATEGORY_NAME_COUNT_NAME = {
        'Notebooklar': 'notebook__count',
        'Smartfonlar': 'smartphone__count'
    }


    def get_queryset(self):
        return super().get_queryset()
    
    def get_categories_for_left_sidebar(self):
        models = get_models_for_count('notebook', 'smartphone')
        qs = list(self.get_queryset().annotate(*models))
        data = [
            dict(name=c.name, url=c.get_absolute_url(), count=getattr(c, self.CATEGORY_NAME_COUNT_NAME[c.name]))
            for c in qs
            ]
        
        return data

class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Kategoriyalar nomi')
    slug = models.SlugField(unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Kategoriya', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Nomi')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Rasm')
    description = models.TextField(verbose_name='Tafsilotlar', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Narxi')

    def __str__(self):
        return self.title

    def get_model_name(self):
        return self.__class__.__name__.lower()

class Notebook(Product):

    diagonal = models.CharField(max_length=255, verbose_name="Diagonal")
    display_type = models.CharField(max_length=255, verbose_name="Displey turi")
    processor_freq = models.CharField(max_length=255, verbose_name="Chastotasi")
    ram = models.CharField(max_length=255, verbose_name="Tezkor xotira")
    rom = models.CharField(max_length=255, null=True, verbose_name="Asosiy xotira" )
    videokart = models.CharField(max_length=255, verbose_name="Videokarta")
    time_without_charge = models.CharField(max_length=255, verbose_name="Akkumulyator ishlash vaqti")

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Smartphone(Product):

    diagonal = models.CharField(max_length=255, verbose_name="Diagonal")
    display_type = models.CharField(max_length=255, verbose_name="Displey turi")
    resolution = models.CharField(max_length=255, verbose_name="Ekran o'lchamlari")
    accum_volume = models.CharField(max_length=255, verbose_name="Akkumulyator hajmmi")
    ram = models.CharField(max_length=255, verbose_name="Tezkor xotira")
    rom = models.CharField(max_length=255, null=True, verbose_name="Asosiy xotira")
    sd = models.BooleanField(default=True, verbose_name="SD karta mavjudligi")
    sd_volume_max = models.CharField(
        null = True, blank = True, max_length=255, verbose_name="Maksimal tashqi xotira"
        )
    main_cam_mp = models.CharField(max_length=255, verbose_name="Asosiy kamera")
    front_cam_mp = models.CharField(max_length=255, verbose_name="Frontal kamera")

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    
    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')



class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Mijoz', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Savatcha', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Umumiy narx')

    def __str__(self):
        return "Maxsulot {} (savatga)".format(self.content_object.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)


class Cart(models.Model):

    owner = models.ForeignKey('Customer', null=True, verbose_name='Egasi', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=13, default=0, decimal_places=2, verbose_name='Umumiy narx')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):

        return str(self.id)

    

class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Foydalanuvchi', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Telefon raqami', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Manzil', null=True, blank=True)
    orders = models.ManyToManyField('Order', verbose_name='Mijoz buyurtmalari', related_name='related_customer')

    def __str__(self):

        return "Mijoz: {} {} ".format(self.user.first_name, self.user.last_name)

class Order(models.Model):
    
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Yangi buyurtma'),
        (STATUS_IN_PROGRESS, 'Buyurtma tayyorlanmoqda'),
        (STATUS_READY, 'Buyurtma tayyor'),
        (STATUS_COMPLETED, 'Buyurtma bajarildi')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF,  'Olib ketish'),
        (BUYING_TYPE_DELIVERY,  'Yetkazib berish')
    )

    customer = models.ForeignKey(Customer, verbose_name='Mijoz', related_name='related_orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Ism') 
    last_name = models.CharField(max_length=255, verbose_name='Familiya')
    phone = models.CharField(max_length=25, verbose_name='Tel raqam')
    cart = models.ForeignKey(Cart, verbose_name='Savat', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=1000, verbose_name='Manzil', null=True, blank=True)
    status = models.CharField(
        max_length=100, 
        verbose_name='Buyurtma holati', 
        choices=STATUS_CHOICES, 
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=100,
        verbose_name='Buyurtma turi',
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    comment = models.TextField(verbose_name='Buyurtma haqida izoh', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Buyurtma qilingan vaqt')
    order_date = models.DateField(verbose_name='Buyurtma qabul qilish vaqti', default=timezone.now)

    def __str__(self):
        return str(self.id)