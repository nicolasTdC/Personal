import time
import os 
import datetime
import pyautogui
import UserConfigs as UC
os. chdir(UC.filePath)
import GeneralActions as GA
import DailyScript as DS
import ConvoyPlunder as CP
import Dicts as DICTS
import eventosCheck as eC
import TeamInstance as TI
import Mitsuri as Mitsuri

#%%
time.sleep(4)
#autoclick pra fase de elite
'''
while True:
    time.sleep(3)
    pyautogui.click(826,810)
    
'''   
#kurama
'''
while True:

    hora = GA.checkHour()
    minutos = datetime.datetime.now().minute




    if  ( (hora <23) and ( (hora >= 22) and (minutos >= 10) )) :

     GA.entrarEvento('NineTails1.png','NineTails2.png')
     
     GA.mouseClick(GA.imgFind('Participation.png'))   

     ans = GA.imgFind('KuramaHokageSupport.png')
     while ans is None:
         ans = GA.imgFind('KuramaHokageSupport.png')

     #troca comp
     for _ in range(3):
         GA.mouseClick((808,235))
         time.sleep(2)
        
     GA.mouseClick(GA.imgFind('NinjaMenu.png'))           
     
     time.sleep(2)
     
     GA.mouseClick((546,268))
     
     time.sleep(2)
     pyautogui.press('esc')
     ##
     
     time.sleep(2)
     pyautogui.moveTo(889,301)
     time.sleep(2)
     GA.mouseClick((889,301))
     

     ans = GA.imgFind('KuramaHokageSupport.png')
     while ans is not None:
         ans = GA.imgFind('KuramaHokageSupport.png')
     
     
     ans = GA.imgFind('KuramaHokageSupport.png')
     while ans is None:
         ans = GA.imgFind('KuramaHokageSupport.png')
        
        
     pyautogui.moveTo(889,301)
     time.sleep(2)
     GA.mouseClick((889,301))
     time.sleep(2)
     pyautogui.moveTo(889,301)
     time.sleep(2)
     GA.mouseClick((889,301))
     
     time.sleep(30)
     
     ans = GA.imgFind('KuramaHokageSupport.png')
     while ans is None:
         ans = GA.imgFind('KuramaHokageSupport.png')
      
     GA.mouseClick(GA.imgFind('NinjaMenu.png'))           
     
     time.sleep(2)
     
     GA.mouseClick((546,239))
     
     time.sleep(2)
     
     pyautogui.press('esc')
                      
     time.sleep(2)
        

     os.system('shutdown /s /t 1')


'''
#repetir TI
'''

while True:
    time.sleep(5)
    pyautogui.click(741,657)
    ans = GA.imgFind('TeamInstanceReturn.png')
    while ans is None:
        GA.Auto2x()
        ans = GA.imgFind('TeamInstanceReturn.png')
    GA.mouseClick(ans)
'''
#autoclick pra treino max

while True:
    time.sleep(3)
    pyautogui.click(917,671)
    
   