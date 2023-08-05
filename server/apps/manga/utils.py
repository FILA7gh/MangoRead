from rest_framework.pagination import PageNumberPagination


class MangaPagination(PageNumberPagination):
    page_size = 12


class GenrePagination(PageNumberPagination):
    page_size = 10
