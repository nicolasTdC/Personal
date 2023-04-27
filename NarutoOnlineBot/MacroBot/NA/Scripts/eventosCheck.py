import time
import os 
import pyautogui
import UserConfigs as UC
os. chdir(UC.filePath)
import GeneralActions as GA

#eventos False se ainda precisa fazer


def checkConvoy():
    GA.entrarEvento('ConvoyPlunderSelect1.png','ConvoyPlunderSelect2.png')
    time.sleep(3)
    check = GA.imgFind('RewardingAttempts3.png')
    check2 = GA.imgFind('convoyCheck2.png')
    if (check2 is None) and (check is None):
        pyautogui.press('esc')
        return False
    pyautogui.press('esc')
    return True

def checkTI():
    GA.entrarEvento('TeamInstanceSelect1.png','TeamInstanceSelect2.png')
    time.sleep(3)
    check = GA.imgFind('RewardingAttempts5.png')
    check2 = GA.imgFind('RewardingAttempts5_1.png')
    check3 = GA.imgFind('checkTI1.png')
    check4 = GA.imgFind('actCheckTI.png')
    
    if (check is None) and (check2 is None) and (check3 is not None) and (check4 is not None):
        pyautogui.press('esc')
        return False
    else:
        pyautogui.press('esc')
        return True

def checkRichField():
    GA.mouseClick(GA.mouseClick((1905,100)))
    time.sleep(2)
    GA.mouseClick(GA.imgFind('RichField.png'))
    ans = GA.imgFind('EnterRichField.png')
    while ans is None:
        ans = GA.imgFind('EnterRichField.png')
    GA.mouseClick(ans)
    time.sleep(2)
    check = GA.imgFind('RichFieldCheck.png')
    if check is None:
        pyautogui.press('esc')
        return False
    else:
        pyautogui.press('esc')
        return True

def checkExpTreasure():
    GA.mouseClick(GA.mouseClick((1905,100)))
    time.sleep(2)
    GA.mouseClick(GA.imgFind('RichField.png'))
    ans = GA.imgFind('EnterExpTreasure.png')
    while ans is None:
        ans = GA.imgFind('EnterExpTreasure.png')
    GA.mouseClick(ans)
    time.sleep(2)
    check = GA.imgFind('ExpTreasureCheck.png')
    check2 = GA.imgFind('ExpTreasureCheck2.png')
    if (check is None) and (check2 is None):
        pyautogui.press('esc')
        return False
    else:
        pyautogui.press('esc')
        return True

def checkDailyPractice(img1,img2):
    GA.mouseClick(GA.imgFind('DailyPractice.png'))
    time.sleep(2)
    ans1 = GA.imgFind(img1)
    ans2 = GA.imgFind(img2)
    
    if (ans1 is None) and (ans2 is None):
        pos =  (1078,705)
    
        pyautogui.moveTo(pos)
        time.sleep(1)
        #pyautogui.click()
        
        pyautogui.mouseDown()
        time.sleep(0.05)
    
        pyautogui.mouseUp()
        
    time.sleep(2)

    ans1 = GA.imgFind(img1)
    ans2 = GA.imgFind(img2)         
    
    if (ans1 is None) and (ans2 is None):
        pyautogui.press('esc')
        return False
    else:
        pyautogui.press('esc')
        return True

def checkMatsuri():
    GA.entrarEvento('MatsiruCheck1.png','MatsiruCheck2.png')
    time.sleep(3)
    check = GA.imgFind('checkMitsuri.png')
    if check is None:
        pyautogui.press('esc')
        return False
    else:
        pyautogui.press('esc')
        return True

def checkMatsuri2():
    GA.entrarEvento('Matsuri2Check1.png','Matsuri2Check2.png')
    time.sleep(3)
    check = GA.imgFind('checkMitsuri.png')
    if check is None:
        pyautogui.press('esc')
        return False
    else:
        pyautogui.press('esc')
        return True

#%%
