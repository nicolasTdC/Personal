import datetime
import pyautogui
import time
import os 
import UserConfigs as UC
os. chdir(UC.filePath)

def checkHour():
    e = datetime.datetime.now()
    hora=e.hour
    return hora

def mouseClick(pos):
    pyautogui.click(pos, duration = 0.1)
    
def imgFind(img):
    ans = pyautogui.locateCenterOnScreen(img) #return(x,y) or None
    return ans

def abaEventos():
    mouseClick((100,220))
    pyautogui.mouseDown()
    time.sleep(2)
    
    pyautogui.mouseUp()

def write(word):
    pyautogui.write(word)  

def entrarEvento(img1,img2): #('','')
    abaEventos()
    
    time.sleep(2)
    

    ans1 = imgFind(img1)
    ans2 = imgFind(img2)
    
    if (ans1 is None) and (ans2 is None):
        pos =  (1078,705)
    
        pyautogui.moveTo(pos)
        time.sleep(1)
        #pyautogui.click()
        
        pyautogui.mouseDown()
        time.sleep(0.05)
    
        pyautogui.mouseUp()
        
    time.sleep(2)

    ans1 = imgFind(img1)
    ans2 = imgFind(img2)         
    
    if ans1 is not None:
        pos = ans1  
        mouseClick(pos)
        
    else: 
        pos = ans2
            
        mouseClick(pos)


    
    time.sleep(1)    
    '''
    
    if first == True:
        
        ready = imgFind(actPoint)
    
    else:
    
    ready = imgFind(actPoint)
    '''
    ready = True
    return ready

def Auto2x():
    ans = imgFind('FindAuto.png')
    if ans is not None:
        mouseClick(ans)
    ans =  imgFind('FindX1Speed.png')
    if ans is not None:
        mouseClick(ans)
#%%
def replaceConfigs(search,replace):
    with open('UserConfigs.py', 'r') as file :
      filedata = file.read()
    
    # Replace the target string
    filedata = filedata.replace(search, replace)
    
    # Write the file out again
    with open('UserConfigs.py', 'w') as file:
      file.write(filedata)