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

#pyautogui.PAUSE = 3

    #%%DISABLE INVITE
    
time.sleep(3)

GA.mouseClick(GA.imgFind('CreateTeam.png'))  
     
ans1 = GA.imgFind('TeamMenuCheck.png')
     
if ans1 is not None:
    GA.mouseClick(ans1)
    

ans2= GA.imgFind('TeamMenuCheck2.png')
     
if ans2 is not None:
    GA.mouseClick(ans2)     

pyautogui.press('esc')
#%%
dt = datetime.datetime.now()
WeekDay = dt.strftime('%A')

'''
if WeekDay != 'Monday':
    sapinho = True
'''
#else:
sapinho = False

Convoy = eC.checkConvoy()

time.sleep(2)

Dono = UC.Dono

RichField=eC.checkRichField()
faseRichField = DICTS.RichField[UC.faseRichField] 

time.sleep(2)

Roleta=UC.Roleta

CheckIn=eC.checkDailyPractice('checkSignIn1.png','checkSignIn2.png')

time.sleep(2)

Recruit = UC.Recruit

NinjaExam = eC.checkDailyPractice('checkNinjaExam1.png','checkNinjaExam2.png')

time.sleep(2)

LuckyRunes = UC.LuckyRunes

SurvivalTrial=eC.checkDailyPractice('checkSurvivalTrial1.png','checkSurvivalTrial2.png')
ptsSurvivalTrial = UC.pointsSurvivalTrial
  
time.sleep(2)

ExpTreasure=eC.checkExpTreasure()
faseExpTreasure = DICTS.ExpTreasure[UC.faseExpTreasure]

time.sleep(2)

NinjaTest= eC.checkDailyPractice('checkNinjaTest1.png','checkNinjaTest2.png')
#%%
time.sleep(2)

TeamInstance = eC.checkTI()
faseTI= DICTS.TeamInstances[UC.faseTI]
difTI = DICTS.TeamInstances[UC.difTI]

Matsuri1 = UC.Matsuri
Matsuri2 = UC.Matsuri2

time.sleep(2)

Arena=UC.Arena

onsenFlag = False

NineTails = UC.NineTails

cave =False

freeSummon = False
#%%
e = datetime.datetime.now()
hora = e.hour
minutes=e.minute


start = hora*60+minutes

pars = (Convoy,Dono,RichField,Roleta,CheckIn,Recruit,NinjaExam,LuckyRunes,SurvivalTrial,ExpTreasure,NinjaTest,Arena,start,TeamInstance,faseTI,difTI,faseExpTreasure,sapinho,faseRichField,WeekDay,Matsuri1,Matsuri2,onsenFlag ,NineTails,cave,freeSummon)


def main(pars):
    ###
    
    Convoy,Dono,RichField,Roleta,CheckIn,Recruit,NinjaExam,LuckyRunes,SurvivalTrial,ExpTreasure,NinjaTest,Arena,start,TeamInstance,faseTI,difTI,faseExpTreasure,sapinho,faseRichField,WeekDay,Matsuri1,Matsuri2,onsenFlag ,NineTails,cave,freeSummon = pars[0],pars[1],pars[2],pars[3],pars[4],pars[5],pars[6],pars[7],pars[8],pars[9],pars[10],pars[11],pars[12],pars[13],pars[14],pars[15],pars[16],pars[17],pars[18],pars[19],pars[20],pars[21],pars[22] ,pars[23],pars[24],pars[25]
    
    ###


    #%%#Free Treasures (Done for: Bond, Seal)
    if Recruit != 'True':
        time.sleep(4)
        DS.recruit(2)
        
        GA.replaceConfigs(Recruit, 'True')
        Recruit = 'True'
    
    #%%NinjaExam (ok)
    if NinjaExam == False:
        time.sleep(4)
        DS.NinjaExam()
        NinjaExam = True
    #%%lucky runes
    if LuckyRunes != 'True':
        time.sleep(3)
        DS.LuckyRunes()
        GA.replaceConfigs(LuckyRunes, 'True')
        LuckyRunes = 'True'
        
    #%%#Guild DONO (DONE)
    if Dono != 'True':
        time.sleep(2)
        DS.GuildDono(Dono)
        GA.replaceConfigs(Dono, 'True')
        Dono = True
    
    #%%#Rich Field (ok)
    if RichField == False:
        time.sleep(4)
        DS.RichField(faseRichField) #easy pos
        DS.RichField(faseRichField)      
        RichField=True 
    #%%Guild Roleta (ok)
    if Roleta != 'True':
        time.sleep(4)
        
        DS.Roleta(6)
        
        GA.replaceConfigs(Roleta, 'True')
        Roleta = 'True'
     
    #%%Survival (em progresso / teste)
    
    if SurvivalTrial==False:
        time.sleep(4)
        DS.SurvivalTrial(ptsSurvivalTrial)
    
    #%%NinjaTest (ok)
    time.sleep(2)
    if NinjaTest==False:
        #DS.NinjaTest()
        NinjaTest=True
    #%%ilusao(teste)

   # DS.ilusao()
    #%%
    time.sleep(1)
    
    if cave is not True:
    
       cave=  DS.cave()
    #%%
    if freeSummon is not True:
    
        freeSummon = DS.freeSummon()
    #%%Timed Events
    hora = GA.checkHour()
    minutos = datetime.datetime.now().minute
    dt = datetime.datetime.now()
    WeekDay = dt.strftime('%A')
#%%    
    if ( (hora <16) and (hora >= 13) ) or ((hora <23) and (hora >= 20) ):
    
        if Convoy == False: #Convoy (TESTE)
            
            first=True
        
            CP.Convoy(first)
            
            Convoy == True
            #%%
    
    if ( (hora <16) and (hora >= 12) ) or ((hora <24) and (hora >= 20) ):
        if TeamInstance == False: #TI (TESTE)
        
            TI.TeamInstance(faseTI,difTI)
            
            TeamInstance = True
    
    #%%bds
    if (WeekDay == 'Tuesday') or (WeekDay == 'Thursday') or (WeekDay == 'Sunday'):
        DS.bds(hora,minutos)
    #%%gato
    if (WeekDay == 'Thursday')    :
        DS.gato(hora,minutos)
        
    #%%matsuri arena (teste)
    
    if WeekDay == 'Sunday':
        if  ( (hora <20) and (hora >= 17) ):
            if Matsuri1 != 'True':
                Matsuri1 = eC.checkMatsuri()

                if Matsuri1 is False:                   
                    Mitsuri.Mitsuri('MatsiruCheck1.png','MatsiruCheck2.png',1)
                    GA.replaceConfigs(Matsuri, 'True')
                    Matsuri1 = 'True'
        
    #%%matsuri normal (teste)
    
    if (WeekDay == 'Monday') or (WeekDay == 'Friday') :
        if  ( (hora <24) and (hora >= 21) ):
            
            if Matsuri2 != 'True':
                Matsuri2 = eC.checkMatsuri2()

                if Matsuri2 is False:                   
                    Mitsuri.Mitsuri('Matsuri2Check1.png','Matsuri2Check2.png',2)
                    GA.replaceConfigs(Matsuri2, 'True')
                    Matsuri2 = 'True'
    
    #%%
    time.sleep(1)
    if WeekDay == ('Sunday') or WeekDay == ('Monday') or WeekDay == ('Tuesday') or WeekDay == ('Friday'):
        
        #NineTails (teste)
        if  ( (hora <23) and ( (hora >= 22) and (minutos >= 10) )) :
            if NineTails != 'True': 
            
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
                 
                 time.sleep(5)
                 
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
                 
                 pyautogui.moveTo(546,239)
                 GA.mouseClick((546,239))
                 
                 time.sleep(2)
                 
                 pyautogui.press('esc')
                                  
                 time.sleep(2)
                    
                 if WeekDay != 'Monday':
                    os.system('shutdown /s /t 1')
    
                 else:
                     GA.mouseClick(GA.mouseClick((1905,100)))
                     GA.replaceConfigs(NineTails, 'True')
                     NineTails = 'True'
            
    ##%GGN
     
    if WeekDay == ('Wednesday') or WeekDay == ('Saturday'):
        
        if ( (hora >= 21) and (minutos >= 31) ) :
        
            DS.ggn()
            GA.mouseClick(GA.mouseClick((1905,100)))
            while ( (hora < 22) or (minutos <16) ):
                hora = GA.checkHour()
                minutos = datetime.datetime.now().minute
            DS.ggn()
            
            time.sleep(10)
            os.system('shutdown /s /t 1')
    
            
    #%%Arena
    if Arena == True:
        time.sleep(2)
    
        DS.EnterArena()
        time.sleep(2)
        DS.ArenaLoop(1)#numero de runs
    #%%CheckIn (DONE)
    onlineTime = datetime.datetime.now()
    onlineTimeCheck= onlineTime.hour*60+onlineTime.minute
    
    
    if (CheckIn==False) and ( (onlineTimeCheck - start) >=60 ):
        time.sleep(4)
        
        DS.checkIn()
        CheckIn=True
    
    #%%OnlinePack (DONE)
        time.sleep(4)
        
        DS.OnlinePack()
    #%%ExpTreasure  (teste)
    '''
    if ExpTreasure == False:
        time.sleep(2)
        DS.ExpTreasure(faseExpTreasure)
        ExpTreasure=True
    '''
    #%%Sapinho (teste para dobro)
    if sapinho == True:
        
        sapinho = DS.sapinho()
        
    if (WeekDay == 'Tuesday') and ((hora >= 2) and minutos >= 5) and (hora <7):
        sapinho = DS.sapinho()
        time.sleep(2)
        os.system('shutdown /s /t 1')
        
    time.sleep(3)
    
    #%%onsen
    time.sleep(1)
    if onsenFlag == False:
        onsenFlag = DS.onsen()
    
    return (Convoy,Dono,RichField,Roleta,CheckIn,Recruit,NinjaExam,LuckyRunes,SurvivalTrial,ExpTreasure,NinjaTest,Arena,start,TeamInstance,faseTI,difTI,faseExpTreasure,sapinho,faseRichField,WeekDay,Matsuri1,Matsuri2,onsenFlag ,NineTails,cave,freeSummon)
    
#%%
while __name__== '__main__':
    
    
    pars = main(pars)
    #Convoy,Dono,RichField,Roleta,CheckIn,NinjaExam,LuckyRunes,SurvivalTrial,ExpTreasure,NinjaTest,Arena,TeamInstance,faseExpTreasure ,sapinho,WeekDay,Matsuri1,Matsuri2,onsenFlag,NineTails,cave,freeSummon=res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9],res[10],res[11],res[12],res[13],res[14],res[15],res[16],res[17],res[18],res[19],res[12],res[13],res[14],res[15],res[16]
    
    
#%%
