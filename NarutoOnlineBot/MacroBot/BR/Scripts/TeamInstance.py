import time
import os
import pyautogui
import UserConfigs as UC
os. chdir(UC.filePath)
import GeneralActions as GA


def TeamInstance(posSeta,vezesSeta): #primeiras 4 por enquanto

    
    
    ##EM TIME MAS EH INCONSISTENTE
    
    ''' 
    
     GA.mouseClick(GA.imgFind('CreateTeam.png'))  
    
     time.sleep(3)
     GA.mouseClick(GA.imgFind('TeamInstanceCreate.png'))
     time.sleep(2)
     GA.mouseClick(GA.imgFind('CreateTeamMenuCreateTeam.png'))
     time.sleep(2)
     GA.mouseClick((978,571))
     time.sleep(2)
     pyautogui.hotkey('ctrl', 'a')
     
     time.sleep(2)
     pyautogui.press('backspace')        
     time.sleep(2)
     
     GA.write('AJUDA FG / HELP TI')
     time.sleep(2)
    
     GA.mouseClick(GA.imgFind('CreateTeamMenuCreate.png'))
     time.sleep(2)
     GA.mouseClick(GA.imgFind('CreateTeam.png')) 
     time.sleep(2)
     GA.mouseClick(GA.imgFind('TeamInvite.png')) 
     
     time.sleep(2)
     
     GA.mouseClick((944,524))
     time.sleep(2)
     pyautogui.hotkey('ctrl', 'a')
     
     time.sleep(2)
     pyautogui.press('backspace')        
     time.sleep(2)
     
     GA.write('AJUDA FG / HELP TI ; CLICK >>')
     time.sleep(2)
     
     GA.mouseClick(GA.imgFind('SendTeamInvite.png'))#pra guilda
     time.sleep(2)
       
     GA.mouseClick(GA.imgFind('CreateTeam.png'))  
     time.sleep(2)
    
     ans=GA.imgFind('TeamEmptySlot.png')
     for _ in range(10):
         ans=GA.imgFind('TeamEmptySlot.png')
         time.sleep(10)
         if ans is None:
             Time=True
             break
     if Time==True:
        
        pyautogui.press('esc') 
        
        ready = GA.entrarEvento('TeamInstanceSelect1.png','TeamInstanceSelect2.png')
        
        time.sleep(4)
        
        GA.mouseClick(GA.imgFind('Participation.png'))   
        
        time.sleep(4)
    
        GA.mouseClick(lvl)
        
        time.sleep(6)
        
        GA.Auto2x()
        #%%
    '''
    
    #solo
    
    GA.entrarEvento('TeamInstanceSelect1.png','TeamInstanceSelect2.png')
    
    time.sleep(2)
    
    GA.mouseClick(GA.imgFind('Participation.png'))   
    
    time.sleep(4)
    
    ans = GA.imgFind('TIfailsafe.png')
    if ans is not None:
        pyautogui.press('esc')
        return True
    
    for _ in range(5):
        
        ans = GA.imgFind('TeamInstanceAll.png')

        while ans is None:
            
            ans = GA.imgFind('TeamInstanceAll.png')
        
        GA.mouseClick(ans)
        
        time.sleep(1)
        
        pyautogui.moveTo(posSeta)
        
        for _ in range(vezesSeta):
            time.sleep(1)
            pyautogui.mouseDown()
            time.sleep(0.05)
            pyautogui.mouseUp()
        
        pyautogui.moveRel(0,454-539)
        
        time.sleep(1)
        pyautogui.mouseDown()
        time.sleep(0.05)
        pyautogui.mouseUp()
        
        ans = GA.imgFind('TeamInstanceConfirmEntry.png')
        
        while ans is None:
            ans = GA.imgFind('TeamInstanceConfirmEntry.png')
        
        GA.mouseClick(ans)
        
        ans = GA.imgFind('TeamInstanceReturn.png')
        while ans is None:
            GA.Auto2x()
            ans = GA.imgFind('TeamInstanceReturn.png')
        GA.mouseClick(ans)
    
    pyautogui.press('esc')
