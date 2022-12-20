from django.urls import path
from .views import HomePageView, collection_view, item_view, CollectionDetailView

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('collections/', collection_view, name='collection'),
	path('collections/<int:pk>', CollectionDetailView.as_view(), name='collection-detail'),
	path('items/', item_view, name='item'),
]
