import os
os.makedirs('/home/antonlarrazabal/Deskargak/backup')
for filename in os.listdir('/home/antonlarrazabal/Deskargak'):
	os.system('tar cvf fitxategi_izena.tar')
