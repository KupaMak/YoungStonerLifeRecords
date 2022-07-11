from django.db import models


class ManagerAuth(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=60)
	code_number = models.IntegerField()

	def __str__(self):
		return self.username

class UserAuth(models.Model):
	first_name =  models.CharField(max_length=80)
	last_name =  models.CharField(max_length=80)
	username = models.CharField(max_length = 80)
	password = models.CharField(max_length = 40)
	code_number = models.IntegerField()



class UserDetail(models.Model):
	GENDER = (
		('Male', 'Male'),
		('Female', 'Female'),
	)
	DEPARTMENT = (

		('Artist', 'Artist'),
		('Producer', 'Producer'),
		('Chief Executive Officer', 'Chief Executive Officer'),
		('Manager', 'Manager'),
		('Disk Jokey', 'Disk Jokey')

	)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	national_id = models.CharField(max_length=50, default='0000000')
	gender = models.CharField(max_length=50, choices=GENDER)
	department = models.CharField(max_length=30, choices=DEPARTMENT, default='Artist')
	phone_number = models.CharField(max_length=30)
	email = models.CharField(max_length=50)
	date_employed = models.DateField(auto_now_add=True)
	date_of_birth = models.CharField(max_length=50)
	address = models.CharField(max_length=60)
	account_number = models.CharField(max_length=50)
	stage_name = models.CharField(max_length=40, default='N/A')
	picture = models.ImageField(null=True, blank=True, upload_to='profile')

	def __str__(self):
		return self.stage_name

class UserAlbum(models.Model):
	CERTIFICATION = (
		('Gold', 'Gold'),
		('Platinum', 'Platinum'),
		('Diamond', 'Diamond'),
		('N/A', 'N/A')

	)

	album = models.CharField(max_length=40, default='N/A')
	artist_id = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
	no_of_tracks = models.CharField(max_length=50)
	first_week_sales = models.CharField(max_length=40, default='N/A')
	year = models.CharField(max_length=10)
	certification = models.CharField(max_length=20, choices=CERTIFICATION)
	cover_art = models.FileField(upload_to='cover_art')

	def __str__(self):
		return self.album

class UserPayroll(models.Model):
	MONTH = (
		('January', 'January'),
		('February', 'February'),
		('March', 'March'),
		('April', 'April'),
		('May', 'May'),
		('June', 'June'),
		('July', 'July'),
		('August', 'August'),
		('September', 'September'),
		('October', 'October'),
		('November', 'November'),
		('December', 'December'),
	)

	artist_id = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
	general_salary = models.CharField(max_length=50)
	show_tour_income = models.CharField(max_length=50)
	platforms_income = models.CharField(max_length=50)
	insurance = models.CharField(max_length=50)
	transport = models.CharField(max_length=50)
	accommodation = models.CharField(max_length=50)
	month = models.CharField(max_length=40, choices=MONTH)
	total_expenses = models.CharField(max_length=50)
	total_income = models.CharField(max_length=50)
	date_paid = models.DateField(auto_now_add=True)
	net_salary = models.CharField(max_length=50)

	def __str__(self):
		return self.net_salary

class Studio(models.Model):
	studio_name = models.CharField(max_length = 50)
	location =  models.CharField(max_length =  50)
	main_producer =  models.ForeignKey(UserDetail,on_delete=models.CASCADE)

	def __str__(self):
		return self.studio_name



class StudioSession(models.Model):


	start_time  = models.TimeField(max_length=10)
	end_time =  models.TimeField(max_length = 10)
	date = models.DateField(auto_now_add=True)
	studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
	artist = models.ForeignKey(UserDetail, related_name='Producer', on_delete=models.CASCADE)
	producer = models.ForeignKey(UserDetail, related_name='Artist', on_delete=models.CASCADE)







