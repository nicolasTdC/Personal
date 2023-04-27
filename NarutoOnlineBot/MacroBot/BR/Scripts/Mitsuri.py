import time
import os
import pyautogui
import UserConfigs as UC
os. chdir(UC.filePath)
import GeneralActions as GA


def Mitsuri(img1,img2,nbr):
    time.sleep(2)
    GA.entrarEvento(img1,img2)
    
    GA.mouseClick(GA.imgFind('Participation.png'))    
    
    time.sleep(2)
    
    signUp = GA.imgFind('MitsuriSignUp.png')
    GA.mouseClick(signUp)

    if signUp is None:
        signUp = GA.imgFind('MitsuriRegister.png')
        GA.mouseClick(signUp)
        
    time.sleep(2)
      
    GA.mouseClick(628, 507)

    time.sleep(1)
    
    GA.mouseClick(765, 507)

    time.sleep(1)
    
    GA.mouseClick(943, 507)

    time.sleep(1)
    
    GA.mouseClick(1112, 507)

    time.sleep(1)
    
    GA.mouseClick(1267, 507)

    time.sleep(1)
    
    GA.mouseClick(628, 578)

    time.sleep(1)
    
    GA.mouseClick(765, 578)

    time.sleep(1)
    
    GA.mouseClick(943, 578)

    time.sleep(1)
    
    GA.mouseClick(1112, 578)

    time.sleep(1)
    
    GA.mouseClick(1267, 578)

    time.sleep(1)
    
    GA.mouseClick(628, 653)

    time.sleep(1)
    
    GA.mouseClick(765, 653)

    time.sleep(1)
    
    GA.mouseClick(943, 653)

    time.sleep(1)
    
    GA.mouseClick(1112, 653)

    time.sleep(1)
    
    GA.mouseClick(1267, 653)

    time.sleep(1)
    
    GA.mouseClick((978,813))
    
    time.sleep(3)
    
    for _ in range(3):
        flag = MitsuriFight(nbr)
        if flag == True:
            return True
        
    ans = GA.imgFind('MatsuriConfirm.png')
    
    while ans is None:
        ans = GA.imgFind('MatsuriConfirm.png')
    
    GA.mouseClick(ans)
    
    ans = GA.imgFind('MatsuriConfirm2.png')
    
    while ans is None:
        ans = GA.imgFind('MatsuriConfirm2.png')
    
    GA.mouseClick(ans)
    
    
def MitsuriFight(nbr):
    
    time.sleep(5)
    if nbr ==1:
        pyautogui.mouseDown(368,372)
        time.sleep(1)    
        pyautogui.moveTo(715,511)
        time.sleep(1)  
        pyautogui.mouseUp()
    
        time.sleep(1)
        
        pyautogui.mouseDown(368,448)
        time.sleep(1)
        pyautogui.moveTo(715,568)
        time.sleep(1)  
        pyautogui.mouseUp()
    
        time.sleep(1)
        
        pyautogui.mouseDown(368,526)
        time.sleep(1)
        pyautogui.moveTo(715,653)
        time.sleep(1)  
        pyautogui.mouseUp()
    
        time.sleep(1)
        
        pyautogui.mouseDown(368,620)
        time.sleep(1)
        pyautogui.moveTo(837,568)
        time.sleep(1)  
        pyautogui.mouseUp()
    
        time.sleep(1)
        
        GA.mouseClick(GA.imgFind('MitsuriBattle.png'))
        
        time.sleep(60)
        
        cancel = GA.imgFind('MatsuriCancel.png')
        if cancel is not None:
            return True
        
    
    if nbr ==2:
        pyautogui.mouseDown(368,372)
        time.sleep(1)    
        pyautogui.moveTo(699,532)
        time.sleep(1)  
        pyautogui.mouseUp()
    
        time.sleep(1)
        
        pyautogui.mouseDown(368,448)
        time.sleep(1)
        pyautogui.moveTo(699,598)
        time.sleep(1)  
        pyautogui.mouseUp()
    
        time.sleep(1)
        
        pyautogui.mouseDown(368,526)
        time.sleep(1)
        pyautogui.moveTo(699,673)
        time.sleep(1)  
        pyautogui.mouseUp()
    
        time.sleep(1)
        
        pyautogui.mouseDown(368,620)
        time.sleep(1)
        pyautogui.moveTo(824,600)
        time.sleep(1)  
        pyautogui.mouseUp()
    
        time.sleep(1)
        
        GA.mouseClick((819,862))
        
        time.sleep(60)
        
        cancel = GA.imgFind('MatsuriCancel.png')
        if cancel is not None:
            return True
    
    ans1 = GA.imgFind('ConfirmDefeat.png')
    ans2= GA.imgFind('PlunderConfirmWin.png')
    
    while (ans1 is None) and (ans2 is None):
        ans1 = GA.imgFind('ConfirmDefeat.png')
        ans2= GA.imgFind('PlunderConfirmWin.png')
        GA.Auto2x()
    
    if ans1 is not None:
        
        GA.mouseClick(ans1)
        
    if ans2 is not None:
        
        GA.mouseClick(ans2)



    #%%