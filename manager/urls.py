from django.urls import path
from . import views

urlpatterns = [

	path('login/', views.login, name ='manager-login'),
	path('create-account/', views.login , name='manager-create-account'),
	path('dashboard/', views.dashboard, name='manager-dashboard'),
	path('artists/', views.artists, name='artists'),
	path('newartist/', views.new_artist, name='new-artist'),
	path('studios/', views.studios, name='studios'),
	path('newstudio/', views.new_studio, name='new-studio'),
	path('updatestudio/<str:pk>', views.update_studio, name='update-studio'),
	path('deletestudio/', views.delete_studio, name='delete-studio'),
	path('albums/', views.dashboard, name='albums'),
	path('studiosessions/', views.studio_sessions, name='studio-sessions'),
	path('showstours/', views.dashboard, name='shows-tours'),
	path('payroll/', views.dashboard, name='payroll'),
	path('viewartist/<str:pk>',views.view_artist, name='view-artist'),
	path('deleteartist/', views.delete_artist, name='delete-artist'),
	path('updateartist/<str:pk>', views.update_artist, name='update-artist'),




]
