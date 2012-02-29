from django.db import models

# Create your models here.

DIVISION = ( ("International","International"), ("Bushin Kan","Bushin Kan") )

COUNTRY = ( ("USA","United States"), ("Japan","Japan"), ("Canada","Canada"), ("UK","United Kingdom"), ("France","France"), ("Belgium","Belgium"),
		("Russia","Russia"), ("Chile","Chile"), ("Malta","Malta"), ("Spain","Spain"), ("Isreal","Isreal"), ("Greece","Greece"),
		("Austrailia","Austrailia"), ("Italy","Italy"), ("Portugal","Portugal"), ("Hungary","Hungary"), ("Germany","Germany"),
		("Armenia","Armenia") ) 


STATE = ( ("VA","Virginia"), ("WA","Washington"), ("DC","Washington DC"), ("AL","Alabama"), ("FL","Florida"), ("GA","Georgia"),
	  ("LA","Louisiana"), ("MS","Mississippi"), ("SC","South Carolina"), ("NC","North Carolina"), ("MD","Maryland"), ("DE","Delaware"),
	  ("PA","Pennsylvania"), ("NJ","New Jersey"), ("NY","New York"), ("CT","Connecticut"), ("MA","Massachusetts"), ("VT","Vermont"),
	  ("NH","New Hampshire"), ("RI","Rhode Island"), ("ME","Maine"), ("OH","Ohio"), ("KY","Kentucky"), ("TN","Tennessee"), ("TX","Texas"),
	  ("AR","Arkansas"), ("KS","Kansas"), ("OK","Oklanhoma"), ("ND","North Dakota"), ("SD","South Dakota"), ("AK","Alaska"), ("HI","Hawaii"), 		  ("CA","California"), ("WY","Wyoming"), ("NE","Nebraska"), ("MO","Missouri"), ("MN","Montana"), ("NV","Nevada"), ("NM","New Mexico"),
	  ("AZ","Arizona"), ("ID","Idaho"), ("CO","Colorado"), ("IN","Indiana"), ("IA","Iowa"), ("IL","Illinois"), ("OR","Oregon"),
	  ("UT","Utah"), ("MN","Minnisota"), ("MI","Michigan"), ("WI","Wisconsin"), ("PR","Puerto Rico") )


class Bushinkan_dojo(models.Model):
	#dojo_logo = models.CharField(max_length=5)
	dojo_name = models.CharField(max_length=64)
	dojo_head = models.CharField(max_length=50)
	address = models.CharField(max_length=24)
	city = models.CharField(max_length=20)
	state_province = models.CharField(max_length=18, choices=STATE)
	zip_code = models.CharField(max_length=10)
	country = models.CharField(max_length=32, choices=COUNTRY)
	website = models.URLField(max_length=50)
	email = models.EmailField(blank=True)
	dojo_programs = models.CharField(max_length=64)
	
	def _unicode_(self):
		return self.name
	
	
class Id_dojo(models.Model):
	#dojo_logo = models.CharField(max_length=5)
	dojo_name = models.CharField(max_length=64)
	dojo_head = models.CharField(max_length=50)
	address = models.CharField(max_length=64)
	city = models.CharField(max_length=20)
	state_province = models.CharField(max_length=18, choices=STATE, blank=True)
	zip_code = models.CharField(max_length=10)
	country = models.CharField(max_length=24, choices=COUNTRY)
	website = models.URLField(max_length=50)
	email = models.EmailField(blank=True)
	dojo_programs = models.CharField(max_length=64)
	
	def _unicode_(self):
		return self.name
	

class Bushinkan_yudansha(models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	address = models.CharField(max_length=64)
	city = models.CharField(max_length=20)
	state_province = models.CharField(max_length=18, choices=STATE, blank=True)
	zip_code = models.CharField(max_length=10)
	country = models.CharField(max_length=24, choices=COUNTRY)
	email = models.EmailField(blank=True)
	dojo_name = models.CharField(max_length=64)
	dojo_leader = models.CharField(max_length=3)
	budo_type = models.CharField(max_length=64)
	current_rank = models.CharField(max_length=16)	
	admin_title = models.CharField(max_length=10)
	admin_date = models.CharField(max_length=8)
	prof_title = models.CharField(max_length=8)
	prof_date = models.CharField(max_length=8)
	membership_current = models.CharField(max_length=7)
	start_date = models.CharField(max_length=8)
	yellow_date = models.CharField(max_length=8)
	green_date = models.CharField(max_length=8)
	blue_date = models.CharField(max_length=8)
	sankyu_date = models.CharField(max_length=8)
	nikyu_date = models.CharField(max_length=8)
	itkyu_date = models.CharField(max_length=8)
	karishodan_date = models.CharField(max_length=8)
	shodan_date = models.CharField(max_length=8)
	nidan_date = models.CharField(max_length=8)
	sandan_date = models.CharField(max_length=8)
	yondan_date = models.CharField(max_length=8)
	godan_date = models.CharField(max_length=8)
	rokudan = models.CharField(max_length=8)
	shichi_date = models.CharField(max_length=8)
	hachi_date = models.CharField(max_length=8)
	member_documents = models.CharField(max_length=64, blank=True)
	member_notes = models.CharField(max_length=250, blank=True)
	
	def _unicode_(self):
		return u'%s %s' % (self.first_name, self.last_name)
	
class Bushinkan_yukyusha(models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	address = models.CharField(max_length=64)
	city = models.CharField(max_length=20)
	state_province = models.CharField(max_length=18, choices=STATE)
	zip_code = models.CharField(max_length=10)
	country = models.CharField(max_length=24, choices=COUNTRY)
	email = models.EmailField(blank=True)
	dojo_name = models.CharField(max_length=64)
	budo_type = models.CharField(max_length=64)
	current_rank = models.CharField(max_length=16)
	membership_current = models.CharField(max_length=7)
	start_date = models.CharField(max_length=8)
	yellow_date = models.CharField(max_length=8)
	green_date = models.CharField(max_length=8)
	blue_date = models.CharField(max_length=8)
	sankyu_date = models.CharField(max_length=8)
	nikyu_date = models.CharField(max_length=8)
	itkyu_date = models.CharField(max_length=8)
	karishodan_date = models.CharField(max_length=8)
	member_documents = models.CharField(max_length=64, blank=True)
	member_notes = models.CharField(max_length=250, blank=True)
	
	def _unicode_(self):
		return u'%s %s' % (self.first_name, self.last_name)


class Id_yudansha(models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	address = models.CharField(max_length=64)
	city = models.CharField(max_length=20)
	state_province = models.CharField(max_length=18, choices=STATE, blank=True)
	zip_code = models.CharField(max_length=10)
	country = models.CharField(max_length=24, choices=COUNTRY)
	email = models.EmailField(blank=True)
	dojo_name = models.CharField(max_length=64)
	dojo_leader = models.CharField(max_length=3)
	budo_type = models.CharField(max_length=64)
	current_rank = models.CharField(max_length=16)
	admin_title = models.CharField(max_length=10)
	admin_date = models.CharField(max_length=8)
	prof_title = models.CharField(max_length=8)
	prof_date = models.CharField(max_length=8)
	country_coordinator = models.CharField(max_length=3)
	membership_current = models.CharField(max_length=7)
	start_date = models.CharField(max_length=8)
	yellow_date = models.CharField(max_length=8)
	green_date = models.CharField(max_length=8)
	blue_date = models.CharField(max_length=8)
	sankyu_date = models.CharField(max_length=8)
	nikyu_date = models.CharField(max_length=8)
	itkyu_date = models.CharField(max_length=8)
	karishodan_date = models.CharField(max_length=8)
	shodan_date = models.CharField(max_length=8)
	nidan_date = models.CharField(max_length=8)
	sandan_date = models.CharField(max_length=8)
	yondan_date = models.CharField(max_length=8)
	godan_date = models.CharField(max_length=8)
	rokudan = models.CharField(max_length=8)
	shichi_date = models.CharField(max_length=8)
	hachi_date = models.CharField(max_length=8)
	membership_type = models.CharField(max_length=10)
	member_documents = models.CharField(max_length=64, blank=True)
	member_notes = models.CharField(max_length=250, blank=True)
	
	def _unicode_(self):
		return u'%s %s' % (self.first_name, self.last_name)
	
class Id_yukyusha(models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	address = models.CharField(max_length=64)
	city = models.CharField(max_length=20)
	state_province = models.CharField(max_length=18, choices=STATE, blank=True)
	zip_code = models.CharField(max_length=10)
	country = models.CharField(max_length=24, choices=COUNTRY)
	email = models.EmailField(blank=True)
	dojo_name = models.CharField(max_length=64)
	budo_type = models.CharField(max_length=64)
	current_rank = models.CharField(max_length=16)
	membership_current = models.CharField(max_length=7)
	start_date = models.CharField(max_length=8)
	yellow_date = models.CharField(max_length=8)
	green_date = models.CharField(max_length=8)
	blue_date = models.CharField(max_length=8)
	sankyu_date = models.CharField(max_length=8)
	nikyu_date = models.CharField(max_length=8)
	itkyu_date = models.CharField(max_length=8)
	karishodan_date = models.CharField(max_length=8)
	membership_type = models.CharField(max_length=10)
	member_documents = models.CharField(max_length=64, blank=True)
	member_notes = models.CharField(max_length=250, blank=True)
	
	def _unicode_(self):
		return u'%s %s' % (self.first_name, self.last_name)





