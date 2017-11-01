from datetime import datetime
import time 
import subprocess
import os	
import os.path
import cv2 #must be installed on the flight computer in order to work

class data_logger(object):
#generic interface to log data 

#data_logger is set up to be a ring buffer if the user indicates the data
#should not be permanent. All the data currently goes to a file called "data" 
#on the desktop. Each data_logger object then has a folder named after its tag 
#within the data folder.Every instance of a logged data array goes to its own timestamped 
#text file, may be implemented so all data arrays will be concatenated into one large data file that 
#can be searched into in post-processing from the terminal by using "grep" 
#with the tag names.

#Args:
#tag: string label that the user wants to be able to find the data organized under
#isPermanent: boolean that indicates whether or not files are permanent
#interval: integer that file age should not exceed (in seconds), used before size was implemented but still can be used
#size: integer that file size should not exceed (in bytes)

	#directory = '~/Desktop/Data/'
	#os.system('mkdir -p ' + os.path.expanduser(directory)) 
		

	def __init__(self, tag, isPermanent, interval, size): 
		
		self.tag = tag
		self.isPermanent = isPermanent
		self.interval = interval
		self.directory = '~/Desktop/Data/' + tag +'/'
		self.size = size
		os.system('mkdir -p ' + os.path.expanduser(self.directory)) 

	def save_data_array(self, data):
	
		

		timestr = time.strftime("%d_%b_%Y_%H:%M:%S", time.localtime())		
		filename = self.tag + "Data" + '-' + timestr
		fullpath = os.path.expanduser(self.directory + filename + '.txt')
		file = open(fullpath, 'a')
		save = "TAG: " + self.tag + "\n"
		save += "{}".format(data)
		print(save + ' ' + timestr)
		save += '\n'
		file.write(save)
		file.close()

		self.remove_old() #moved to end of this function

	def remove_old(self): 
		#size = 5200
		initialSize = subprocess.check_output(['du', '-bs', os.path.expanduser(self.directory)])
		index = initialSize.find(os.path.expanduser(self.directory))
		initialSize = initialSize[:index] 
		initialSize = initialSize.strip(" ")
		print ('initial size is', (int(initialSize)))
		
		tooBig = False
		if int(initialSize) > self.size: 
			tooBig = True

		while tooBig or not self.isPermanent: 
			os.system("ls -t " + os.path.expanduser(self.directory) + " > filelist.txt") #should list the files from newest to oldest
			#os.system("rm filelist.txt")
			input = open("filelist.txt", 'r')
			lines = input.readlines()
			input.close()
			track = 0
			for line in lines:
				track += 1
				print('round: %d', track)
				x = str(line)
				print("line is: "+x)
				tagCheck=x[0:len(x)-30] #not used anywhere else
				fileDateStr = x[len(x)-25:len(x)-5]
				print("fileDateStr is: "+fileDateStr)
				fileDate = datetime.strptime(fileDateStr, "%d_%b_%Y_%H:%M:%S")
				
				currentime = time.strftime("%d_%b_%Y_%H:%M:%S", time.localtime())
				currentime = datetime.strptime(currentime, "%d_%b_%Y_%H:%M:%S")
				fileAge = currentime - fileDate
				print(currentime)
				print(fileDate)
				REMOVE = fileAge.seconds > self.interval

				if ((REMOVE and not self.isPermanent) or (track == len(lines) and tooBig)) : 
					subprocess.check_call(["rm", os.path.expanduser(self.directory) + x[:len(x)-1]])
					newSize = subprocess.check_output(['du', '-bs', os.path.expanduser(self.directory)])
					index = newSize.find(os.path.expanduser(self.directory))
					newSize = newSize[:index] 
					newSize = newSize.strip(" ")
					print('this is the new size', int(newSize))
					if int(newSize) < self.size: 
						tooBig = False
		                                
		                
					

	def save_image(self, img): #currently implemented such that img is the file destination of an already saved image e.g. /home/user/Desktop/picture.jpg
		timestr = time.strftime("%d_%b_%Y_%H:%M:%S", time.localtime())	#The image is saved in a folder according to the tag, with a number (1,2,3...) then the timestring from when it was saved
		filename = self.tag + "Image" + '-' + timestr
		
		extension='.jpg'
		fullpath = os.path.expanduser(self.directory + '1' + filename + extension )
		num=2
		while (os.path.isfile(fullpath)):
			fullpath = os.path.expanduser(self.directory + str(num) + filename + extension )
			num+=1
			
	
		imgOb=cv2.imread(img)
		cv2.imwrite(fullpath, imgOb)
		
		os.system('rm '+img)

		self.remove_old()



	def save_message(self, msg):
		
		timestr = time.strftime("%d_%b_%Y_%H:%M:%S", time.localtime())		
		filename = self.tag + "Data" + '-' + timestr
		fullpath = os.path.expanduser(self.directory + filename + '.txt')
		file = open(fullpath, 'w+')
		file.write("TAG: " + self.tag + "\n" + msg)
		file.close() 

		self.remove_old()

def make_data_logger(tag, isPermanent, interval, size): 
	x = data_logger(tag, isPermanent, interval, size)
	return x




