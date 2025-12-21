from django.urls import path

from .REST.views.requests_API_views import CollectionRequestManager

from .REST.views.profile_API_views import *
from .REST.views.collections_API_views import *
from .REST.views.trade_API_views import *
from .REST.views.requests_API_views import * 




urlpatterns = [
    # API trades
    path('api/trades/', TradeList.as_view(), name='api-all-trades'), # all trades
    path('api/trades/create/', TradeListCreateView.as_view(), name='api-create-trade'), # all trades
    path('api/trades/<pk>/', IndividualTradeDetail.as_view(), name='api-one-trade'), # specific trade
    path('api/trades/<pk>/comments/', TradeCommentDetail.as_view(), name='api-one-trade-comments'), # specific trade
    path('api/trades/<pk>/attachments/', TradeAttachmentsDetail.as_view(), name='api-one-trade-attachments'), # specific trade
    path('api/<uuid:user_id>/trades/', UserTradeList.as_view(), name='api-user-trades'), # trades of a user
    path('api/<uuid:user_id>/bookmarked/', UserBookmarkTradeList.as_view(), name='api-user-bookmarks'), # bookmarked trades of a user
    path('api/trades/<str:trade_id>/edit_bookmark/', EditBookmarksView.as_view(), name='api-bookmark-toggle'), #user can add/remove own bookmarks

    # API collections/items view-only urls:
    path('api/collections/', CollectionList.as_view(), name='all collections'),
    path('api/collections/mine/', MyCollectionList.as_view(), name='all my collections'),
    path('api/collections/<uuid:collection_id>/', SingleCollection.as_view(), name='single collection'),
    path('api/collections/<uuid:collection_id>/mine/', MySingleCollection.as_view(), name='my single collection'),
    path('api/item/<uuid:item_id>/', ItemDetailView.as_view(), name='item detail'),
    path('api/all_my_items/', AllMyItems.as_view(), name='my single collection'),

    #API collections/items editing:
    path('api/collect/<uuid:user_id>/<uuid:item_id>/', EditMyItemsView.as_view(), name='collect more'),
    path('api/new_item/', AddItemView.as_view()),
    path('api/new_collection/', AddCollectionView.as_view()),

    # API for request: 
    path('api/request/collection/', AddNewCollectionRequest.as_view(), name="add new collection request"),
    path('api/request/item/', AddNewItemRequest.as_view(), name="Add new Item Request"),
    path('api/request/collection/<uuid:id>/', CollectionRequestManager.as_view(), name="Approved Collection for new Collection"),
    path('api/request/item/<uuid:id>/', ItemRequestManager.as_view(), name="Approved Request for new Item"),
    path('api/request/<uuid:id>/', CollectionRequestManager.as_view(), name="testing"),

    #viewing all profile info:
    path('api/profile/<str:username>/', ProfileAPIView.as_view(), name='any-profile'),
    path('api/feedback/<uuid:receiver_id>/', GiveFeedbackView.as_view(), name='give-feedback'),

    #backup pattern, to catch incorrect urls..:
#    path('*', WrongURLView.asView(),)
]

