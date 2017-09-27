from datetime import *
import os
from django.conf import settings
import boto 
from boto.s3.key import Key
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

class functions:	

	@staticmethod
	def path_and_rename(path,prefix):
		def wrapper(instance, filename):			
			filename, file_extension = os.path.splitext(filename)			
			# get filename
			fecha=datetime.now()
			filename = '{}_{}{}{}{}{}{}{}'.format(prefix,fecha.year,fecha.month,fecha.day,fecha.hour,fecha.minute,fecha.second, file_extension)		

			return os.path.join(path, filename)
		return wrapper	

			
	@staticmethod
	def descargarArchivoS3(ruta_relativa, ruta_descarga, nombre_archivo=None):
			conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID,settings.AWS_SECRET_ACCESS_KEY)	
			bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)	
			key = bucket.get_key(settings.MEDIAFILES_LOCATION+'/'+ruta_relativa)
			filename=os.path.basename(key.key)	
			print key.key
			key.get_contents_to_filename(ruta_descarga + (nombre_archivo if nombre_archivo else filename))
			key.set_contents_from_filename(ruta_descarga + (nombre_archivo if nombre_archivo else filename))
			

	@staticmethod
	def exportarArchivoS3(ruta_relativa):
			conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID,settings.AWS_SECRET_ACCESS_KEY)	
			bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)	
			key = bucket.get_key(settings.MEDIAFILES_LOCATION+'/'+ruta_relativa)
			print os.path.basename(key.key)
			filename=os.path.basename(key.key)
			
			response_headers = {
		    'response-content-type': 'application/force-download',
		    'response-content-disposition':'attachment;filename="%s"'%filename
		    }
			url = key.generate_url(
						60, 
						'GET',				
						response_headers=response_headers,
		 				force_http=True)

			return HttpResponseRedirect(url)




