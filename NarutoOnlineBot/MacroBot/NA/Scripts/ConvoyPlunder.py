import time
import os 
import pyautogui
import UserConfigs as UC
os. chdir(UC.filePath)
import GeneralActions as GA

def convoyLoop(rank,flagSS):
    ans = GA.imgFind(rank)
    rep = GA.imgFind('ConvoyRepetido.png')
    if (ans is None)  or ( rep is not None):
        GA.mouseClick(GA.imgFind('ConvoyRefresh.png')) 
        time.sleep(5)
        convoyLoop(rank,flagSS)
    else:
        pyautogui.moveTo(ans)
        time.sleep(2)
        pyautogui.moveRel(1250-668,0)
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()
       # GA.mouseClick(GA.imgFind('ConvoyClaim.png')) 
        time.sleep(2)
        for _ in range (0,3):
            GA.mouseClick(GA.imgFind('ConvoySupport.png')) 
            time.sleep(2)
        time.sleep(15)
        GA.mouseClick(GA.imgFind('ConvoySetOff.png')) 
        
        ans = GA.imgFind('ConvoyFinishConfirm.png')
        while ans is None:
            
            GA.Auto2x()  
            
            plunderWin = GA.imgFind('PlunderConfirmWin.png')
            plunderLoss = GA.imgFind('PlunderConfirmLoss.png')
            
            if plunderWin is not None:
                
                GA.mouseClick (plunderWin)
                
                time.sleep(5)
                
                GA.entrarEvento('ConvoyPlunderSelect1.png','ConvoyPlunderSelect2.png')
                GA.mouseClick(GA.imgFind('Participation.png'))    
                ans = GA.imgFind('ConvoySetOff2.png')
                while ans is None:
                    ans = GA.imgFind('ConvoySetOff2.png')
                GA.mouseClick(ans)
                
                
            
            if plunderLoss is not None:
                
                GA.mouseClick (plunderLoss) 
                time.sleep(5)
                
                GA.entrarEvento('ConvoyPlunderSelect1.png','ConvoyPlunderSelect2.png')
                GA.mouseClick(GA.imgFind('Participation.png'))    
                ans = GA.imgFind('ConvoySetOff2.png')
                while ans is None:
                    ans = GA.imgFind('ConvoySetOff2.png')
                GA.mouseClick(ans)                 
            
            ans = GA.imgFind('ConvoyFinishConfirm.png')
            
            
        GA.mouseClick(ans)
        

def Convoy(first):

    ready = GA.entrarEvento('ConvoyPlunderSelect1.png','ConvoyPlunderSelect2.png')
    
    time.sleep(2)
    if ready is not None:
        
        GA.mouseClick(GA.imgFind('Participation.png'))    
        time.sleep(10)
        
        lastCheck = GA.imgFind('lastConvoyCheck.png')
        if lastCheck is not None:
            pyautogui.press('esc')
            time.sleep(2)
            GA.mouseClick((1905,100))
            return True
        
        
        flagSS=True
        convoyLoop('ConvoySS.png',flagSS)
        
        time.sleep(5)
        
        GA.entrarEvento('ConvoyPlunderSelect1.png','ConvoyPlunderSelect2.png')
        GA.mouseClick(GA.imgFind('Participation.png'))    
        time.sleep(10)
        
        flagSS = False
        convoyLoop('ConvoyS.png',flagSS)
        
        time.sleep(5)
        
        GA.entrarEvento('ConvoyPlunderSelect1.png','ConvoyPlunderSelect2.png')
        GA.mouseClick(GA.imgFind('Participation.png'))    
        time.sleep(10)
        
        convoyLoop('ConvoyS.png',flagSS)
        
        time.sleep(5)
        GA.mouseClick(GA.mouseClick((1905,100)))    
    
    else:
        GA.mouseClick(GA.imgFind('CloseButton.png'))
    

