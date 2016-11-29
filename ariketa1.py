import os

for filename in os.listdir('/home/antonlarrazabal/Deskargak'):
     if (os.path.getsize(os.path.join('/home/antonlarrazabal/Deskargak', filename))>=5242880 and os.path.isfile(os.path.join('/home/antonlarrazabal/Deskargak', filename))):
	print filename+' 5 mega baino handiagoa da'

     else:
	print filename+' ez da 5 mega baino handiagoa'
