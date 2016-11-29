import shutil, os
os.makedirs('/home/antonlarrazabal/Deskargak/tmp/kopia')
for filename in os.listdir('/home/antonlarrazabal/Deskargak'):
     if os.path.getsize(os.path.join('/home/antonlarrazabal/Deskargak', filename))>=10240 and os.path.getsize(os.path.join('/home/antonlarrazabal/Deskargak', filename))<= 10485760 and os.path.isfile(os.path.join('/home/antonlarrazabal/Deskargak', filename)):
	shutil.copy('/home/antonlarrazabal/Deskargak/'+filename, '/home/antonlarrazabal/Deskargak/tmp/kopia/'+filename)
        print("sartu da: " + filename)

     else:
	print filename+' ez dago 10kb eta 10 mega artean'
