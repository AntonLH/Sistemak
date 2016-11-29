import os

for filename in os.listdir('/home/antonlarrazabal/Deskargak/tmp/kopia'):
     if (os.path.getsize(os.path.join('/home/antonlarrazabal/Deskargak/tmp/kopia', filename))>=52428800 and os.path.isfile(os.path.join('/home/antonlarrazabal/Deskargak/tmp/kopia', filename))):
	os.unlink('/home/antonlarrazabal/Deskargak/tmp/kopia'+filename)

     else:
	print filename+' ez da 50 mega baino handiagoa'
