from rest_framework.pagination import PageNumberPagination

class ListProductPagination(PageNumberPagination):
    page_size=1
    page_query_param='product'
    max_page_size=100