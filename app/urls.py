from django.urls import path, include
from .views import home,prodDetail,registerV,loginV, logoutV,pay,customerData,delete_user,create_order,order_history,edit_user, contact, addProduct,listProduct,modifyProduct,deleteProduct, ProductViewset, view_cart, add_to_cart, update_cart_item, remove_cart_item, change_cart_item_quantity, paypal_complete, download_invoice
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', ProductViewset)
#localhost:8000/api/product

urlpatterns = [
    path('', home , name="home"),
    path('product/<int:id>', prodDetail, name='prodDetail'),
    path('register', registerV, name='register'),
    path('login', loginV, name='login'),
    path('logout', logoutV, name='logout'),
    path('pay', pay, name='pay'),
    path('customerData', customerData, name='customerData'),
    path('delete_user', delete_user, name='delete_user'),
    path('edit_user', edit_user, name='edit_user'),
    path('create_order/', create_order, name='create_order'),
    path('order_history/', order_history, name='order_history'),
    path('contact', contact, name='contact'),
    path('addProduct', addProduct, name='addProduct'),
    path('listProduct', listProduct, name='listProduct'),
    path('modifyProduct/<id>/', modifyProduct, name='modifyProduct'),
    path('deleteProduct/<int:id>', deleteProduct, name="deleteProduct"),
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', remove_cart_item, name='remove_cart_item'),
    path('cart/change/<int:item_id>/<str:action>/', change_cart_item_quantity, name='change_cart_item_quantity'),
    path('paypal/complete/', paypal_complete, name='paypal_complete'),
    path('order/<int:order_id>/invoice/', download_invoice, name='download_invoice'),
    path('api/',include(router.urls))
]