from django.urls import path
from . import views

# urlpatterns = [
#     path('index/', views.index, name='dashboard-index'),
#     path('products/', views.products, name='dashboard-products'),
#     path('products/delete/<int:pk>/', views.product_delete,
#          name='dashboard-products-delete'),
#     path('products/detail/<int:pk>/', views.product_detail,
#          name='dashboard-products-detail'),
#     path('products/edit/<int:pk>/', views.product_edit,
#          name='dashboard-products-edit'),
#     path('customers/', views.customers, name='dashboard-customers'),
#     path('customers/detail/<int:pk>/', views.customer_detail,
#          name='dashboard-customer-detail'),
#     path('order/', views.order, name='dashboard-order'),
# ]

urlpatterns = [
    # path('', views.index, name='customer-index'),
    #path('', views.index, name='index'),
    # path('all_emp', views.all_emp, name='all_emp'),
    # path('add_emp', views.add_emp, name='add_emp'),
    # path('remove_emp', views.remove_emp, name='remove_emp'),
    # path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_emp'),
    # path('filter_emp', views.filter_emp, name='filter_emp'),
    # #path('Cust_emp', views.Cust_emp1, name='Cust_emp'),
    path('index/', views.index, name='customer-index'),
    path('cust/', views.cust, name='customer-cust'),
    path('Cust_emp/', views.Cust_emp, name='customer-Cust_emp'),
    path('Comm_Cust/', views.Comm_Cust, name='customer-Comm_Cust'),
    path('Comp_Cust/', views.Comp_Cust, name='customer-Comp_Cust'),
    path('Govt_Cust/', views.Govt_Cust, name='customer-Govt_Cust'),
    path('Cust_Search/', views.showresults, name='customer-Cust_search'),
    path('view_all_cust/', views.view_all_cust, name='customer-view_all_cust'),
    path('view_all/', views.view_all, name='customer-view_all'),
    path('customer_update/<int:Cust_id>/', views.customer_update, name='customer-customer-update'),
    path('customer_updatepage/<int:Cust_id>/', views.customer_updatepage, name='customer-customer-updatepage'),
    path('Site_Technical_Details/', views.Site_Technical_Details, name='customer-Site_Technical_Details'),

]
