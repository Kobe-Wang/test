#Create 100w files in /samba/sdbf
#Testing time

import os, time, hashlib, md5, random

#Use urandom to randomly generate file
def uRandom(filename, bs, count):
    os.system("dd if=/dev/urandom of="+filename+" bs="+bs+" count="+count+"")

#For vertifying files from restoring
def md5File(filename):
    os.system("md5sum "+filename+"")

def md5sum(file_name):  
    if os.path.isfile(file_name):  
        f = open(file_name,'rb')  
        #import hashlib  
        md5 = hashlib.md5(f.read()).hexdigest()  
        f.close()  
        return md5  
    else:  
        return 0 

def randomFile(filename, bs, count):
    filePath = "/dev/urandom"
    fr = open(filePath, "r")
    fw = open(filename, "w")
    for i in range(1,count+1):  #count
       bytes = fr.read(bs)
       fw.write(bytes)
       #print bytes
    fr.close()
    fw.close()

if __name__=='__main__': 
    
    rangeBegin = 100 #begin range of random
    rangeEnd = 500  #end range of random
    
    fileUpDIR = "/samba/sdf/"
    diskCap = str(rangeBegin) + "k"+ "-" + str(rangeEnd) + "k"
    fw_md5 = open(fileUpDIR + "md5/" + diskCap + "_md5.txt", "w")  #write md5 of file for vertifying
    start_time = time.time()
	  
    dir1_path = fileUpDIR + diskCap
    os.makedirs(dir1_path) # First folder
    countSID = 1000001
    for dir2 in range(1, 101):
       dir2_path = dir1_path + "/" + str(dir2)
       os.makedirs(dir2_path) #Second folder
       for dir3 in range(1,101):
          dir3_path = dir2_path + "/" + str(dir3)
          os.makedirs(dir3_path)  #Third folder
          for i in range(1, 51):  #Write 50 files in third folder
	     file_path_name = dir3_path + "/"  + str(i) +".bin"
	     randomFile(file_path_name, 1024, random.randrange(rangeBegin,rangeEnd))
       	     #uid, filepath name, md5 file
	     fw_md5.write( str(countSID) +"\t" + file_path_name + "\t" + md5sum(file_path_name))
             fw_md5.write("\n")
             countSID = countSID + 1
    fw_md5.close()
    
    executeTime = time.time() - start_time
    print executeTime, "seconds"
    print (executeTime/60), "mins"
    print (executeTime/3600), "hours"   

