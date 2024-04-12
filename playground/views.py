from django.shortcuts import render
# The render() function takes the request object as its first argument, a template name as its
# second argument and a dictionary as its optional third argument. It returns an HttpResponse
# object of the given template rendered with the given context.
from django.http import HttpResponse
from store.models import Product, order_Item , Order , customer
from django.db.models import F , Func
from django.db.models.functions import Concat 
from django.db.models.aggregates import Count, Max,Min,Sum
from django.db.models import Value,ExpressionWrapper,DecimalField
from django.contrib.contenttypes.models import ContentType



# view : request -> responce , Action

def ask(request):
    # Your view logic here
    return HttpResponse('Asalam o alaikum')  # This is the mapping method


def temp(request):
    query_set = Product.objects.filter(price__gte=20)
    return render (request , "index.html", )

    # This is a method to see the value of one column
    # query_set = Product.objects.values('title')

    # Filter products with price greater than or equal to 20
    # query_set = Product.objects.filter(price__gte=20)

    # An F() object represents the value of a model fied, transformed value of a model field, or annotated column
    
    
    # query_set = Product.objects.filter(price=F('slug'))    // for creating again 
    # return render(request, "index.html", {'name': 'Salim', 'products': list(query_set)})

    # Retrieve all product IDs associated with order items
    # product_ids = order_Item.objects.values_list("product_ids")

    # products = Product.objects.filter(id__in=product_ids)
    # # product = Product.objects.filter(order_item__isnull=False)
    # return render(request, "index.html", {'product_ids':(products)})

    # product_ids= order_Item.objects.values("product_id")

    # query_set = product.objects.filter()

    # For Assignment
    # product_item = Product.objects.values("order_item")
    # return render(request, "index.html ", {'title':list(query_set)})
    # return render(request, "index.html", {'name': 'Salim', 'products': list(query_set)})

    # For Assignment
    # query_set = Order.objects.select_related("customer").order_by("-placed_at")[:5]
    # return render(request, "index.html", {'name': 'Salim', 'orders': list(query_set)})    

#<--------------------------------------------------------------------------------------->#



    
 

def hey_me(request):
    # return HttpResponse("We Creating Something New")
                       #Aggregate
    # results=Product.objects.aggregate(count_order=Count("order_item"))
    # results=Product.objects.filter(collection_id=3).aggregate(Max_price=Max("price"))
    # return render( request, "index.html",{"result":results})

#              Annotating
        query_set = order_Item.objects.annotate(is_new=Value(True))
        return render(request, "index.html", {"result": query_set})
#           Calling Database Function 

    # query_set= customer.objects.annotate(
    #     full_name= Concat('given_name', Value(' '),'last_name'))
    # return render(request, "index.html", {"result": query_set})
    
#             Expression Wrapper 
   
    # discounted_price = ExpressionWrapper(F("price") * 0.8, output_field=DecimalField())
    # query_set = Product.objects.annotate(discounted_price=discounted_price)
    # return render(request, "index.html", {"result": query_set})

#             Querying Generic Relationship
    # content_Type =  ContentType.objects.get_for_model(Product)
    # query_set =
      
#------------ Create the Object -------------------
    # Product_title = Product()
    # Product_title.title = "New Item"
    # Product_title.price= 250
    # Product_title.save()
    # return render(request, "index.html", {"result": Product_title})

#-----------Updating the Object -------------------

    # query_set=Product.objects.filter(pk=612).update(title="update_item")
    # return render(request, "index.html", {"result": query_set})

#----------Deleting the object -------------------

    # query_set=Product.objects.get(pk=613).delete()
    # return render(request, "index.html", {"result": query_set})
    
    
    