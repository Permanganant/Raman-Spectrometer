#Raman1 Spectrometer




#Librarys 
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import cm
#import peakutils




def find_nearest_index(arr, value):
    """For a given value, the function finds the nearest value 
    in the array and returns its index."""
    arr = np.array(arr)
    index = (np.abs(arr - value)).argmin()
    return index



#Bubblesort arrray to sort peak values
def bubbleSort(arr): 
    n = len(arr) 
  
    
    for i in range(n): 
  
        
        for j in range(0, n-i-1): 
  
           
            if arr[j] < arr[j+1] : 

                arr[j], arr[j+1] = arr[j+1], arr[j] 






def peakfinder(img):
    
    px_Counter = []

    a = 1
    n = 0

   
    #defining and appending arrays
    px_Counter = []
    for i in range(int(0),int(256)):
        px_Counter.append([])
        for j in range(0,1819):
             px_Counter[i].append(i*j)

    px_Counter2 = []
    
    for e in range (0,1820):
        px_Counter2.append(e)
    


    

    ai = []     
    
    
    for e in range (0,1819):
        ai.append(e)

    af = []     
   
    
    for e in range (0,1819):
        af.append(e)

    



    for i in range (0,256,200):#Region of images(roi) and the number of line to count pixels 
        for j in range (0,1819):#ROI
   
              
            px1,px2,px3 = img[i,j]#Getting rgb values from the defined image
       
            if (px1 > 16) or (px2 > 16) or (px3 > 16):
            
                px_Counter[i][j] = (px1 + px2 + px3)#Counting pixel and assigning to the 2 dimensional(rows and columns) array
           

            else:
                px_Counter[i][j] = (px1 + px2 + px3)#If there is no pixels into the chosen position the count in that position will be zero

    for j in range (0,1819):    
        for i in range (0,256,200):
            px_Counter2[j] = px_Counter[i][j] #Signment for each column intensity into the one dimensional array to plot and correlation



   
   




    y = range(0,1819)
    
    
    import numpy as np
    #import scipy.signal #you can also use scipy.signal function to find peaks

    
    a = 0
    i = 0

  

       
    
    
    #My own unique peak finder function begin here!
    #Function detects the increasings and decreasings of the function and when the path changes its direction it saves the peak position value
    while(a < 1818):
        #print('kontrol',a)
        
        if((int(px_Counter2[a+1]) - int(px_Counter2[a])) > 0):
            #print(a)
            #print(int(px_Counter2[a+1]) - int(px_Counter2[a]))
            if a > 1818:
                    break
            
            while(((int(px_Counter2[a+1]) - int(px_Counter2[a])) > 0)):
                #print('kontrol a',a)
                #print(int(px_Counter2[a+1]) - int(px_Counter2[a]))
                if a > 1818:
                    break
                a = a + 1
                #print('1',a) 
                if a > 1818:#Breaks if are just for the make sure that 'a' value is still into the while loop
                        break

            ai[i] = a#assigning the position to the  one dimensional array
            print(a)#printing peaks' positions(unsorted)
            i = i + 1

        

        elif((int(px_Counter2[a+1]) - int(px_Counter2[a])) <= 0 ):
             
             if a > 1818:
                    break
             while(((int(px_Counter2[a+1]) - int(px_Counter2[a])) <= 0)):
                #print(int(px_Counter2[a+1]) - int(px_Counter2[a]))
                if a > 1818:
                    break
                a = a + 1
                #print('2',a)
                if a > 1818:
                       break
        
        if a > 1818:
                    break
           
    #Defining peak array
    peak = []
    for e in range (0,i):
        peak.append(e)
    
    #assignments of peak values
    for e in range (0,i-1):            
        peak[e] = px_Counter2[ai[e]]            

   
    bubbleSort(peak)#Sorting the values
   
    
    for t in range (0,10):
        print(px_Counter2.index(peak[t]))#This is printing the sorted peaks

  
        




    #print('Detect peaks with minimum height and distance filters.')
    #indexes, _ = scipy.signal.find_peaks(px_Counter2, height=0,threshold = 0, distance=1)
    #print('Peaks are: %s' % (indexes))
    #a = len(indexes)
  
    #indexes,_ = scipy.signal.peak_prominences(y,px_Counter2)
    #print('Peaks are: %s' % (indexes))
    #a = len(indexes)   

    #peak = []     
    
    
    #for e in range (0,a-1):
        #peak.append(e)


    #for i in range  (0,a-1):
       # b = indexes[i]        
        #peak[i] = px_Counter2[b]


    #peak1 = peak
    #bubbleSort(peak)
    #for i in range (0,a - 1):
        #print('peak height',peak[i])
        #print('x ekseni',px_Counter2.index(peak[i]))


    #if you want to use scipy.signal function is begin here.Make sure the other function is in the comment
    
    """
    import numpy as np

    import scipy.signal
    print('Detect peaks with order (distance) filter.')
    indexes = scipy.signal.argrelextrema(np.array(px_Counter2),comparator=np.greater,order=1)
    print('Peaks are: %s' % (indexes[0]))

    

    

    for j in range (0,1819):    
        for i in range (0,257,200):
            px_Counter2[j] = px_Counter[i][j] 


    for i in range (1,1818):
        if(px_Counter2[i+1] <= px_Counter2[i] and px_Counter2[i] >= px_Counter2[i-1]):
            peak[a] = px_Counter2[i]
            print(a)
            print(peak[a])
            a = a + 1 
    
    """




        
        
    





#Ploting Function(Nanometer -Intensity and Position Intensity)
def plot(img):
    #
    px_Counter = []

    i = range (0,256)
    j = range(0,1819)


    px_Counter = []
    for i in range(256):
        px_Counter.append([])
        for j in range(1819):
             px_Counter[i].append(i*j)

    px_Counter2 = []     
    for e in range (0,1819):
        px_Counter2.append(e)





    for i in range (0,256,200):
        for j in range (0,1819):
   
              
            px1,px2,px3 = img[i,j]
       
            if (px1 > 16) or (px2 > 16) or (px3 > 16):
            
                px_Counter[i][j] = (px1 + px2 + px3)
           

            else:
                px_Counter[i][j] = (px1 + px2 + px3)

    for j in range (0,1819):    
        for i in range (0,256,200):
            px_Counter2[j] = px_Counter[i][j] 
    

    y = range(0,1819)
    pxc = px_Counter2    

    
    
    

    fig, (ax1) = plt.subplots(1, sharex=True, sharey=True)        
    ax1.fill_between(y, px_Counter2, facecolor='b', alpha=0.5)
    

    
    
    #cv2.line(img , (0,0) , (150,150) , (123,344,23) ,10) #opencv(BGR) (location , beggining of the line , end of the line ,color, thickness of the line)


    #To proportionate Nanometer value from position
    delta = float(370/1819)
    w= 380
    

    nanometer = []
    for e in range (0,1819):
        nanometer.append(e)



    nanometer[0] = 380
    for e in range (1,1819):
        w = w + delta
        nanometer[e] = w

   

    plt.ylabel('PX DENSITY')
    plt.xlabel('position')
    
    plt.plot(y,px_Counter2,linewidth = 0.1)#Plot the array
    #plt.scatter(y, px_Counter2, c=y, cmap= 'prism',marker = 3,linewidth = 0.5)
    plt.show()#Showing the plotted array



    #Filling inside of the graph with chosen colour
    fig, (ax2) = plt.subplots(1, sharex=True, sharey=True)      
    ax2.fill_between(nanometer, px_Counter2, facecolor='r', alpha=0.5)
    


    plt.ylabel('PX DENSITY')
    plt.xlabel('nanometer')
    plt.plot(nanometer,px_Counter2,linewidth = 0.1)
    plt.show()
    
    

   
#Main Function

r = 2
   
img = cv2.imread('C:\\Users\sbese\Pictures\cr\sp%s.jpg' % r,-1)#Defining the image with opencv library
plot(img)#Ploting
peakfinder(img)#Finding peaks




