from django.shortcuts import render
from .forms import *
from django.http import JsonResponse
from .models import *


def login(request):
	form = ManagerLoginForm()

	if request.POST:

		username = request.POST['username']
		password = request.POST['password']
		code_number = request.POST['code_number']

		validate = ManagerAuth.objects.filter(username=username, password=password, code_number=code_number)

		if validate.count() == 1:

			return JsonResponse({'valid': 'True', 'manager-id': validate[0].id})
		else:

			return JsonResponse({'valid': 'False'})

	context = {'form': form}

	return render(request, 'ManagerAccounts/login.html', context)


def dashboard(request):
	artists = UserDetail.objects.all()
	albums = UserAlbum.objects.all()
	artist_details = UserDetail.objects.all().order_by('-id')[:4]
	studios = Studio.objects.all()

	context = {'artists_count': artists.count(), 'albums': albums.count(), 'studios': studios.count(),
	           'artists': artist_details}

	return render(request, 'ManagerAccounts/index.html', context)


def artists(request):
	artists = UserDetail.objects.all()

	form = AddArtistForm()

	
	context = {'artists': artists, 'form': form}



	return render(request, 'ManagerAccounts/artists.html', context)


def new_artist(request):

	if request.POST:

		form = AddArtistForm(request.POST, request.FILES)

		if form.is_valid():

			form.save()

			return JsonResponse({"saved": "Yes"})
		else:

			return JsonResponse({"saved": "No"})


def view_artist(request, pk):
	return render(request, 'ManagerAccounts/view-profile.html')


def update_artist(request, pk):
	artist = UserDetail.objects.get(id=pk)
	form = AddArtistForm(instance=artist)

	if request.method == "POST" or request.method == "FILES":

		myform = AddArtistForm(request.POST, request.FILES, instance=artist)

		if myform.is_valid():
			myform.save()

			return JsonResponse({"saved": "Yes"})
		else:
			return JsonResponse({"saved": "No"})

	context = {'form': form, 'pk': pk}

	return render(request, 'ManagerAccounts/update-profile.html', context)


def delete_artist(request):
	pk = request.POST['pk']
	artist = UserDetail.objects.get(id=pk)
	if request.POST:
		artist.delete()
		if artist:

			return JsonResponse({"deleted": "Yes"})

		else:
			return JsonResponse({"deleted": "No"})
	else:

		return JsonResponse({"post":False})
def studios(request):
	my_studios = Studio.objects.all()
	
	form = AddStudioForm(request.POST)


	context = {'studios':my_studios, 'form':form}

	return render(request, 'ManagerAccounts/studios.html', context)

def new_studio(request):

	if request.POST:
		form =  AddStudioForm(request.POST)
		if form.is_valid():

			form.save()

			return JsonResponse({"saved":"Yes"})
		else:
			return JsonResponse({"saved":"No"})		
	


def update_studio(request,pk):
	studio = Studio.objects.get(id=pk)
	form = AddStudioForm(instance = studio)

	if request.POST:
		my_form = AddStudioForm(request.POST, instance=studio)
		if my_form.is_valid():
			my_form.save()

			return JsonResponse({"saved":"Yes"})
		else:
			return JsonResponse({"saved":"No"})


	context = {'form':form, 'pk':pk}


	return render(request,'ManagerAccounts/update-studio.html', context)

def delete_studio(request):
	pk = request.POST['pk']
	studio = Studio.objects.get(id=pk)
	if request.POST:
		studio.delete()
		if studio:

			return JsonResponse({"deleted": "Yes"})

		else:
			return JsonResponse({"deleted": "No"})
	else:

		return JsonResponse({"post":False})


def studio_sessions(request):

	form =  AddStudioSessionForm()



	context = {'form':form}


	return render(request,'ManagerAccounts/studio-sessions.html',context)