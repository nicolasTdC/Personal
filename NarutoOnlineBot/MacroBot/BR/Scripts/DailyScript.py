import time
import pyautogui
import os
import UserConfigs as UC
os. chdir(UC.filePath)
import GeneralActions as GA
import Dicts as DICTS
import datetime

##Guild dono
def GuildDono(ryos):  #ex:'GuildDono('300000')
    GA.mouseClick(GA.imgFind('GroupButton.png'))
    time.sleep(2)
    GA.mouseClick(GA.imgFind('GuildDonoPage.png'))
    time.sleep(2)
    pos = (1216,517)
    GA.mouseClick(pos)    
    GA.write(ryos)
    GA.mouseClick(GA.imgFind('GuildDonate.png'))
    time.sleep(2)
    GA.mouseClick(GA.imgFind('CloseButton.png'))
    
##Rich Field

def RichField(lvlPos):
    GA.mouseClick(GA.mouseClick((1905,100)))
    time.sleep(2)
    GA.mouseClick(GA.imgFind('RichField.png'))
    ans = GA.imgFind('EnterRichField.png')
    
    while ans is None:
        ans = GA.imgFind('EnterRichField.png')
    GA.mouseClick(ans)
    time.sleep(2)
    GA.mouseClick(lvlPos)
    time.sleep(3)
    ans = GA.imgFind('ConfirmFimDeFase.png')
    while ans is None:
        GA.Auto2x()

        ans = GA.imgFind('ConfirmFimDeFase.png')
    GA.mouseClick(ans)

    time.sleep(20)

##Roleta

def Roleta(nbr):
    GA.mouseClick(GA.imgFind('GroupButton.png'))
    time.sleep(2)
    for _ in range(2):
        GA.mouseClick((1326,769))
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        
    
    GA.mouseClick((1277,746))
    time.sleep(10)
    for _ in range(nbr):
        GA.mouseClick((743,545))
        time.sleep(10)
    GA.mouseClick(GA.imgFind('CloseRoleta.png'))
    time.sleep(2)
    GA.mouseClick(GA.mouseClick((1905,100)))
    
##sapinho
def sapinho():
    GA.mouseClick(GA.imgFind('TreinoDiario.png'))
    time.sleep(2)
    
    ans = GA.imgFind('sapinho100.png')
    if ans is not None:
        pyautogui.press('esc')
        return False
    
    GA.mouseClick((673,762))
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(5)
    ans=GA.imgFind('levelupOkay.png')
    if ans is not None:
        GA.mouseClick(ans)
        ans = GA.imgFind('TreinoDiario.png')
        while ans is None:
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(1)
            ans = GA.imgFind('TreinoDiario.png')
                 
        GA.mouseClick(ans)
        
    GA.mouseClick((831,758))
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(5)
    ans=GA.imgFind('levelupOkay.png')
    if ans is not None:
        GA.mouseClick(ans)
        ans = GA.imgFind('TreinoDiario.png')
        while ans is None:
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(1)
            ans = GA.imgFind('TreinoDiario.png')
                 
        GA.mouseClick(ans)
    
    GA.mouseClick((996,749))
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(5)
    ans=GA.imgFind('levelupOkay.png')
    if ans is not None:
        GA.mouseClick(ans)
        ans = GA.imgFind('TreinoDiario.png')
        while ans is None:
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(1)
            ans = GA.imgFind('TreinoDiario.png')
                 
        GA.mouseClick(ans)
    
    GA.mouseClick((1158,765))
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(5)
    ans=GA.imgFind('levelupOkay.png')
    if ans is not None:
        GA.mouseClick(ans)
        ans = GA.imgFind('TreinoDiario.png')
        while ans is None:
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(1)
            ans = GA.imgFind('TreinoDiario.png')
                 
        GA.mouseClick(ans)
    
    GA.mouseClick((1335,752))
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(5)
    ans=GA.imgFind('levelupOkay.png')
    if ans is not None:
        GA.mouseClick(ans)
        ans = GA.imgFind('TreinoDiario.png')
        while ans is None:
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(1)
            ans = GA.imgFind('TreinoDiario.png')
        return True
        
    GA.mouseClick(GA.imgFind('CloseSapinho.png'))
    return True
#%%CheckIn
def checkIn():
    GA.mouseClick(GA.imgFind('DailyPractice.png'))
    time.sleep(2)
    ans1= GA.imgFind('DailyCheck1.png')
    ans2 = GA.imgFind('DailyCheck2.png')
    if ans1 is not None:
        
        GA.mouseClick(ans1)
    else: 
        GA.mouseClick(ans2)
    time.sleep(2)
    GA.mouseClick(GA.imgFind('Participation.png'))    
    time.sleep(2)
    ans = GA.imgFind('CheckinToday.png')
    while ans is None:
        ans = GA.imgFind('CheckinToday.png')
    GA.mouseClick(ans)
#%%OnlinePack
def OnlinePack():
    GA.mouseClick(GA.imgFind('OnlinePack.png'))
    for _ in range (3):
        time.sleep(2)
        GA.mouseClick(GA.imgFind('OnlinePackClaim.png'))
    time.sleep(2)

    GA.mouseClick(GA.imgFind('CloseHall.png'))
#%%Arena
def EnterArena():
    GA.mouseClick(GA.imgFind('Arena.png'))     
    time.sleep(2)
    pyautogui.moveTo((489,556))
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    GA.mouseClick(GA.imgFind('ArenaTaskConfirm.png'))  
    time.sleep(2)
    pyautogui.moveTo((501,696))
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    GA.mouseClick(GA.imgFind('ArenaTaskConfirm.png'))  
    time.sleep(2)
    
def ArenaLoop(nbr):
    for _ in range(nbr):
        
        
        ans = GA.mouseClick(GA.imgFind('ranqueadaArena.png')) 
        
        GA.mouseClick(ans)
        
        ans = GA.imgFind('confirmarVitoria.png')
        ans2 = GA.imgFind('confirmarDerrota.png')
        
        while (ans  is None) and (ans2 is None):
            GA.Auto2x()
            ans = GA.imgFind('confirmarVitoria.png')
            ans2 = GA.imgFind('confirmarDerrota.png')
                  
        GA.mouseClick(ans)
        GA.mouseClick(ans2)

        time.sleep(3)
       # ans1 = GA.imgFind('ConfirmArena.png')
        ans2 = GA.imgFind('confirmarArenaRankDown.png')
        ans3 = GA.imgFind('confirmarArenaRankUp.png')
        '''
        if ans1 is not None:
            GA.mouseClick(ans1)
        '''
        if ans2 is not None:
            GA.mouseClick(ans2)
        if ans3 is not None:
            GA.mouseClick(ans3)
                
        '''
        time.sleep(2)
        pyautogui.moveTo((489,556))
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
        GA.mouseClick(GA.imgFind('ArenaTaskConfirm.png'))  
        time.sleep(2)
        pyautogui.moveTo((501,696))
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        GA.mouseClick(GA.imgFind('ArenaTaskConfirm.png'))  
        time.sleep(2)
        '''
    GA.mouseClick(GA.imgFind('CloseArena.png')) 
    pyautogui.press('esc')
#%%FreeTreasures
def recruit(nbr):#nbr of chests
    GA.mouseClick(GA.imgFind('recruit.png'))    
    time.sleep(4)
    #bond treasure
    
    ans=GA.imgFind('BondTreasureFree.png')
    if ans is not None:
        pyautogui.moveTo(ans)
        time.sleep(2)
        pyautogui.moveRel(-1180+1138, -646+704)
        time.sleep(2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.press('esc')  
    time.sleep(2)
    
    #SealTreasure
    ans=GA.imgFind('SealTreasureFree.png')
    if ans is not None:
        pyautogui.moveTo(ans)
        time.sleep(2)
        pyautogui.moveRel(-1180+1138, -646+704)
        time.sleep(2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.press('esc')  
    
    #TendoTreasure
    ans=GA.imgFind('tendoFree.png')
    if ans is not None:
        pyautogui.moveTo(ans)
        time.sleep(2)
        pyautogui.moveRel(-1180+1138, -646+704)
        time.sleep(2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.press('esc')      
    
    
    #end
    time.sleep(3)
    pyautogui.press('esc')  
#%%NinjaExam
def NinjaExam():
    GA.mouseClick(GA.imgFind('NinjaExam.png'))
    time.sleep(5)
    
    GA.mouseClick(GA.imgFind('NinjaExamReset.png'))
    time.sleep(3)
    
    GA.mouseClick(GA.imgFind('NinjaExamResetConfirm.png'))
    time.sleep(3)

    GA.mouseClick(GA.imgFind('NinjaExamSweep.png'))
    time.sleep(3)

    GA.mouseClick(GA.imgFind('NinjaExamQuickSweep.png'))
    
    ans = GA.imgFind('NinjaExamCompleteSweep.png')
    while ans is None:
        ans = GA.imgFind('NinjaExamCompleteSweep.png')
    
    GA.mouseClick(ans)
    time.sleep(3)
    pyautogui.press('esc')
    
#%%Lucky Runes
def LuckyRunes():
    GA.mouseClick(GA.imgFind('LuckyRunes.png'))
    time.sleep(5)
    
    for _ in range (4):
        GA.mouseClick(GA.imgFind('LuckyRunesLucky.png'))
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(2)
    pyautogui.press('esc')

#%%ExpTreasure
def ExpTreasure(fase):
    
    for _ in range(4):   
    
        GA.mouseClick(GA.mouseClick((1905,100)))
        time.sleep(5)
        GA.mouseClick(GA.imgFind('RichField.png'))
        time.sleep(5)
        GA.mouseClick(GA.imgFind('EnterExpTreasure.png'))
        time.sleep(3)
        
        GA.mouseClick(fase)
        
        time.sleep(1)
        startExpTreasure = GA.imgFind('ExpTreasureShukakuStart.png')
        GA.mouseClick(startExpTreasure)
        
        time.sleep(5)
        
        startExpTreasure = GA.imgFind('ExpTreasureShukakuStart.png')
        if startExpTreasure is not None:
            pyautogui.press('esc')
            return True
        
        
        ans = GA.imgFind('confirmarVitoria.png')
        while ans is None:
            ans = GA.imgFind('confirmarVitoria.png')
            GA.Auto2x()
        GA.mouseClick(ans)
        time.sleep(2)
        GA.mouseClick(ans)
        
        time.sleep(4)
        
        ans=GA.imgFind('levelupOkay.png')
        if ans is not None:
            GA.mouseClick(ans)
            time.sleep(1)
            ans = GA.imgFind('TreinoDiario.png')
            while ans is None:
                time.sleep(1)
                pyautogui.press('esc')
                time.sleep(1)
                ans = GA.imgFind('TreinoDiario.png')
                
    pyautogui.press('esc')

    
#%%NinjaTest

def NinjaTest():
    GA.mouseClick(GA.mouseClick((1905,100)))
    time.sleep(5)
    
    GA.mouseClick(GA.imgFind('DailyPractice.png'))
    time.sleep(2)
    ans1 = GA.imgFind('NinjaTestSelect1.png')
    ans2 = GA.imgFind('NinjaTestSelect2.png')

    if ans1 is not None:
        pos = ans1  
        GA.mouseClick(pos)
        
    else: 
        pos = ans2
            
        GA.mouseClick(pos)
    
    time.sleep(2)
    GA.mouseClick(GA.imgFind('Participation.png'))    
    ans = GA.imgFind('NinjaTesteStartTest.png')
    while ans is None:
        ans = GA.imgFind('NinjaTesteStartTest.png')
    GA.mouseClick(ans)
    
    for _ in range(10):
        time.sleep(7)
        GA.mouseClick((938,603))
        time.sleep(2)
        GA.mouseClick(GA.imgFind('NinjaTestSubmit.png'))
        
    time.sleep(5)

    GA.mouseClick(GA.imgFind('NinjaTestClaim.png'))
    time.sleep(1)
    pyautogui.press('esc')
    #%%
def SurvivalTrial(points):
    survCount=0
    
    GA.mouseClick(GA.imgFind('SurvivalTrial.png'))

    time.sleep(5)
   
    ans = GA.imgFind('SurvivalTrialReset.png')
    
    GA.mouseClick(ans)

    GA.mouseClick((1020,963))
    
    time.sleep(3)
    
    for SurvivalB in range (3):
        
        if survCount>=points:
            break
        
        GA.mouseClick((1114,557))
        ans = GA.imgFind('SurvivalTrialBattle.png')
        while ans is None:
            ans = GA.imgFind('SurvivalTrialBattle.png')
           
        time.sleep(1)
        
        for i in range(1,5):
            
            img = 'SurvivalTrialDead' + str(i) + '.png'
            checkDead = GA.imgFind(img)
    
            if checkDead is not None:
                SurvivalTrialDead()
                break
        
        time.sleep(2)
                    
        GA.mouseClick(ans)
        ans = GA.imgFind('SurvivalTrialBattleEnd.png')
        while ans is None:
            ans = GA.imgFind('SurvivalTrialBattleEnd.png')
            GA.Auto2x()
        GA.mouseClick(ans)
        time.sleep(3)
        survCount+=20
    
    for SurivvalC in range (5):
        
        if survCount>=points:
            break
        
        GA.mouseClick((1074,688))
        ans = GA.imgFind('SurvivalTrialBattle.png')
        while ans is None:
            ans = GA.imgFind('SurvivalTrialBattle.png')
        
        time.sleep(1)
        
        for i in range(1,5):
            
            img = 'SurvivalTrialDead' + str(i) + '.png'
            checkDead = GA.imgFind(img)
    
            if checkDead is not None:
                SurvivalTrialDead()
                break
        
        time.sleep(2)
        
        GA.mouseClick(ans)
        ans = GA.imgFind('SurvivalTrialBattleEnd.png')
        while ans is None:
            ans = GA.imgFind('SurvivalTrialBattleEnd.png')
            GA.Auto2x()
        GA.mouseClick(ans)
        time.sleep(3)
        survCount+=10

    for SurivvalA in range (2):
        
        if survCount>=points:
            break
        
        GA.mouseClick((815,525))
        ans = GA.imgFind('SurvivalTrialBattle.png')
        while ans is None:
            ans = GA.imgFind('SurvivalTrialBattle.png')
        
        time.sleep(1)
        
        for i in range(1,5):
            
            img = 'SurvivalTrialDead' + str(i) + '.png'
            checkDead = GA.imgFind(img)
    
            if checkDead is not None:
                SurvivalTrialDead()
                break
        
        time.sleep(2)
        
        GA.mouseClick(ans)
        ans = GA.imgFind('SurvivalTrialBattleEnd.png')
        while ans is None:
            ans = GA.imgFind('SurvivalTrialBattleEnd.png')
            GA.Auto2x()
        GA.mouseClick(ans)
        time.sleep(3)
        survCount+=30
    
    
    time.sleep(3)
    GA.mouseClick((1430,909))#reward claim
   
    time.sleep(3)
    GA.mouseClick((873,595))
    
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('esc')    
def SurvivalTrialDead():
        for key in DICTS.posLuta:
            
            pyautogui.moveTo(DICTS.posLuta[key])
            time.sleep(1)
            pyautogui.mouseDown()
            time.sleep(1)
            pyautogui.moveTo(977,189)
            time.sleep(1)
            pyautogui.mouseUp()
            time.sleep(1)
        
        pyautogui.moveTo(977,189)
        time.sleep(1)
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(DICTS.posLuta['12']) 
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(1)
        
        pyautogui.moveTo(977,189)
        time.sleep(1)
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(DICTS.posLuta['22']) 
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(1)
        
        pyautogui.moveTo(977,189)
        time.sleep(1)
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(DICTS.posLuta['32']) 
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(1)
        
        pyautogui.moveTo(977,189)
        time.sleep(1)
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(DICTS.posLuta['21']) 
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(1)

def onsen():
    GA.mouseClick(GA.imgFind('DailyPractice.png'))
    time.sleep(2)
    ans1 = GA.imgFind('Onsen1.png')
    ans2 = GA.imgFind('Onsen2.png')  
    
    if (ans1 is None) and ( ans2 is None):
        pyautogui.press('esc')
        return True
    
    if ans1 is not None:
        pos = ans1  
        GA.mouseClick(pos)
        
    else: 
        pos = ans2
            
        GA.mouseClick(pos)
    
    GA.mouseClick(GA.imgFind('Participation.png'))    
    time.sleep(5)
    GA.mouseClick((1072,223))
    time.sleep(6)
    ans = GA.imgFind('onsenBath.png')
    ans2 = GA.imgFind('onsenBathEnd.png')
    
    if ans is not None:
        GA.mouseClick(ans)
        time.sleep(60*5)
    
    if ans2 is not None:
        return True
    
    pyautogui.press('esc')
    time.sleep(2)
    GA.mouseClick(GA.mouseClick((1905,100)))
    
#%%

def ilusao():
    
    GA.mouseClick(GA.imgFind('ilusao.png'))
    time.sleep(2)
    ans = GA.imgFind('checkIlusao.png')
    if ans is None:

    
        GA.mouseClick((627,231))
        time.sleep(1)
        for _ in range(2):
            GA.mouseClick((1423,892))
            time.sleep(1)

            ans = GA.imgFind('ilusaoConfirm.png')

            if ans is not None:
                GA.mouseClick(ans)
                        
            pyautogui.press('esc')
            time.sleep(1)

        GA.mouseClick((717,231))
        time.sleep(1)
        for _ in range(2):
            GA.mouseClick((1423,892))
            time.sleep(1)
            ans = GA.imgFind('ilusaoConfirm.png')

            if ans is not None:
                GA.mouseClick(ans)
            
            pyautogui.press('esc')
            time.sleep(1)

        GA.mouseClick((817,231))
        time.sleep(1)
        for _ in range(2):
            GA.mouseClick((1423,892))
            time.sleep(1)
            ans = GA.imgFind('ilusaoConfirm.png')

            if ans is not None:
                GA.mouseClick(ans)
            pyautogui.press('esc')
            time.sleep(1)
    pyautogui.press('esc')
    
def cave():
     GA.mouseClick(GA.imgFind('Cave.png'))
     time.sleep(2)
     ans  = GA.imgFind('CaveFree.png')
     if ans is not None:
         GA.mouseClick(ans)
     pyautogui.press('esc')
     return True

def gato(hora,minutos):
    if (hora == 22) and (minutos >10) and (minutos <15):
    
        GA.entrarEvento('gato.png','gato2.png')
        GA.mouseClick(GA.imgFind('Participation.png'))   
        ans = GA.imgFind('gatoSplash.png')
        while ans is None:
            ans = GA.imgFind('gatoSplash.png')
        GA.mouseClick((903,583))
        ans = GA.imgFind('gatoSupport.png')
        while ans is None:
            ans = GA.imgFind('gatoSupport.png')
        GA.mouseClick(ans)
        ans = GA.imgFind('gatoSupportConfirm.png')
        while ans is None:
            ans = GA.imgFind('gatoSupportConfirm.png')
        GA.mouseClick(ans)
        ans = GA.imgFind('gatoSignup.png')
        while ans is None:
            ans = GA.imgFind('gatoSignup.png')
        GA.mouseClick(ans)
        time.sleep(1)
        GA.mouseClick(ans)
        time.sleep(5)
        pyautogui.moveTo(1819,102)
        GA.mouseClick((1819,102))
        time.sleep(5)
        GA.mouseClick((1373,561))
        
        time.sleep(60*10)
        
        os.system('shutdown /s /t 1')

def bds(hora,minutos):
    if (hora == 21) and (minutos >30) and (minutos <40):
        GA.entrarEvento('sage1.png','sage2.png')
        GA.mouseClick(GA.imgFind('Participation.png')) 
        time.sleep(3)
        pyautogui.moveTo(959,788)
        GA.mouseClick((959,788))
        time.sleep(3)
        GA.mouseClick((1242,784))
        
        while (minutos <41):
            minutos = datetime.datetime.now().minute
        
        flop = GA.imgFind('DailyPractice.png')
        if flop is not None:
            return True
        
        while (hora != 22) and (minutos <7):
        
            ans1 = GA.imgFind('bdsLoose.png')
            ans2 = GA.imgFind('SurvivalTrialBattleEnd.png')
            while (ans1 is None) and (ans2 is None):
                ans1 = GA.imgFind('bdsLoose.png')
                ans2 = GA.imgFind('SurvivalTrialBattleEnd.png')
                GA.Auto2x()
            GA.mouseClick(ans1)
            GA.mouseClick(ans2)
    
            hora = GA.checkHour()
            minutos = datetime.datetime.now().minute

        for _ in range(10):
        
            pyautogui.press('esc')
            time.sleep(2)
def freeSummon():
    GA.mouseClick(GA.imgFind('PowerUp.png'))
    time.sleep(1)
    GA.mouseClick(GA.imgFind('Summons.png'))
    
    time.sleep(1)
    GA.mouseClick(GA.imgFind('SummonsSummon.png'))
       
    time.sleep(3)
    
    ans = GA.imgFind('summonFree.png')
    
    if ans is None:
        pyautogui.press('esc')
        return True
     
    
    pyautogui.moveTo(ans)
    time.sleep(2)
    pyautogui.moveRel(-838+771, -711+784)
    time.sleep(2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('esc')

    time.sleep(1)
    pyautogui.press('esc')
    
    return True
    

def ggn():
    GA.entrarEvento('ggn.png','ggn2.png')
    GA.mouseClick(GA.imgFind('Participation.png')) 
    ans = GA.imgFind('ggnAnbu.png')
    while ans is None:
        ans = GA.imgFind('ggnAnbu.png')
    pyautogui.moveTo(957,579)
    time.sleep(1)
    GA.mouseClick((957,579))
    time.sleep(3)
    pyautogui.moveTo(852,370)
    time.sleep(1)
    GA.mouseClick((852,370))
    ans = GA.imgFind('ggnClosed.png')
    while ans is None:
        GA.Auto2x()
        ans = GA.imgFind('ggnClosed.png')
    pyautogui.moveTo(1635,132)
    time.sleep(1)
    GA.mouseClick((1635,132))
    
    