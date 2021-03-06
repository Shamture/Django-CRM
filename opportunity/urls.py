from django.urls import path
from opportunity.views import (
    OpportunityListView, CreateOpportunityView, OpportunityDetailView, UpdateOpportunityView,
    DeleteOpportunityView, GetContactView, GetOpportunitiesView, AddCommentView,
    UpdateCommentView, DeleteCommentView, AddAttachmentsView)


app_name = 'opportunity'


urlpatterns = [
    path('list/', OpportunityListView.as_view(), name='list'),
    path('create/', CreateOpportunityView.as_view(), name='save'),
    path('<int:pk>/view/', OpportunityDetailView.as_view(), name="opp_view"),
    path('<int:pk>/edit/', UpdateOpportunityView.as_view(), name="opp_edit"),
    path('<int:pk>/delete/', DeleteOpportunityView.as_view(), name="opp_remove"),

    path('contacts/', GetContactView.as_view(), name="contacts"),
    path('get/list/', GetOpportunitiesView.as_view(), name="get_opportunity"),

    path('comment/add/', AddCommentView.as_view(), name="add_comment"),
    path('comment/edit/', UpdateCommentView.as_view(), name="edit_comment"),
    path('comment/remove/', DeleteCommentView.as_view(), name="remove_comment"),

    path('attachment/add/', AddAttachmentsView.as_view(), name="add_attachment"),
    path('attachment/remove/', DeleteCommentView.as_view(),
         name="remove_attachment"),
]
