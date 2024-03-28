from django.contrib import admin
from .models import customer , Collection

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['given_name', 'last_name', 'Membership']
    list_editable = ['Membership']
    ordering=['given_name','last_name']

# admin.site.site_header = 'Storefront Admin'
# admin.site.index_title = 'Admin'
# admin.site.register(customer, CustomerAdmin)

# # class ProductAdmin(admin.ModelAdmin):
# #     list_display = ['title', 'price', 'order_item', 'collection_feature']
# #     list_editable = ['price']
# #     list_per_page = 10

# #     def order_item(self, product):
# #         if product.price > 20:a
# #             return 'Only'
# #         else:
# #             return 'Stock'

# #     def collection_feature(self, product):
         
# #         collection = product.collection_id
# #         return collection.feature_product if collection else '+'


# # admin.site.register(Product, ProductAdmin)


# class collectionAdmin(admin.ModelAdmin):
#     list_display=['title']
    
# admin.site.register(Collection,collectionAdmin)
    
            

