from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q,F
from django.db.models.aggregates import Sum,Count,Min,Max
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail,BadHeaderError
from store.models import Product , Customer , Collection,OrderItem,Order
from tags.models import TaggedItem


def say_hello(request):
    # data = Product.objects.filter(Q(inventory__lt= 10) | Q(unit_price__gt=10))
    # data = Product.objects.order_by('-title')[0:10]
    # data = Product.objects.filter(id__in= OrderItem.objects.values('product_id').distinct())
    # data = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # temp= Order.objects.aggregate(Count('id'))
    #temp = OrderItem.objects.filter(product__id=1).aggregate(count=Sum('quantity'))
    #temp = Order.objects.filter(customer__id=1).aggregate(count=Count('id'))
    temp = Product.objects.filter(collection__id=3).aggregate(count=Count('unit_price' ), sum=Sum('unit_price'),min=Min('unit_price'),Max=Max('unit_price'))
    #data = Customer.objects.annotate(order_count = Max('order__id'))
    #data = Collection.objects.annotate(order_count = Count('product'))
    #data = Customer.objects.annotate(order_count = Count('order')).filter(order_count__gt=5)
    #data = Customer.objects.annotate(order_count = Sum(F('order__orderitem__unit_price') * F('order__orderitem__quantity') ))
    #data = Customer.objects.annotate(order_count = Sum(F('order__orderitem__unit_price') * F('order__orderitem__quantity') )).order_by('-order_count')[:5]
    data = TaggedItem.objects.get_tags_for(Product,1)
    try:
        send_mail('subject','description','karmbadkhshany@gmail.com',['karmbadkhshany@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'products':list(data),'temp':temp})
