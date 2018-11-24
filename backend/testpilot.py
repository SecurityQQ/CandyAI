#robot control library

import threading
import DobotDllType as dType


#constants
baskets =[55, 275, 495, 715]
lastIndex=1000

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

#Load Dll
api = dType.load()


def connect():
    #Connect Dobot
    state = dType.ConnectDobot(api, "", 115200)[0]
    print("Connect status:",CON_STR[state])
    print(state == dType.DobotConnect.DobotConnect_NoError)

    #Clean Command Queued
    dType.SetQueuedCmdClear(api)

    #Async Motion Params Setting
    dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 1)
    dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
    dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

    # Enable Linear Rail
    dType.SetDeviceWithL(api, True)

    #Async Home
    dType.SetHOMECmd(api, temp = 0, isQueued = 1)
    #start point
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 232.1355, -2.7885, 99.0417, 48.8663, 0.0, isQueued=1)


def gotobasket(basket_id):

    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 232.1355, -2.7885, 99.0417, 48.8663, baskets[basket_id], isQueued=1)
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 232.1355, -2.7885, 99.0417, 48.8663, baskets[basket_id], isQueued=1)
    #dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 232.1355, -2.7885, 99.0417, 48.8663, 800.0, isQueued=1)
    execute();

def getcandies():
    #старт забора
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 294.0566, -13.8674, -20.0509, 46.8545, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 294.0566, -13.8674, -20.0509, 46.8545, isQueued=1)
    #забор   
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 298.5595, -12.0067, -60.2918, -15.7484, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 298.5595, -12.0067, -60.2918, -15.7484, isQueued=1)
    #поднял конфеты  
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 266.7224 , -10.4796, 24.4154, -15.6955, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 266.7224 , -10.4796, 24.4154, -15.6955, isQueued=1)
    #конец забора вверх  
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 236.6166 , -3.4984, 49.1397, -43.6925, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 236.6166 , -3.4984, 49.1397, -43.6925, isQueued=1)
    #конец забор 
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 35.4201, -230.5215, 42.3953, -124.1102, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 35.4201, -230.5215, 42.3953, -124.1102, isQueued=1)
    print("all command added to queue")
    execute();


def fakecandies():
     #старт забора
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 294.0566, -13.8674, -20.0509, 46.8545, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 294.0566, -13.8674, -20.0509, 46.8545, isQueued=1)
    #забор   
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 298.5595, -12.0067, -60.2918, -15.7484, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 298.5595, -12.0067, -60.2918, -15.7484, isQueued=1)
    #поднял конфеты  
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 266.7224 , -10.4796, 24.4154, -15.6955, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 266.7224 , -10.4796, 24.4154, -15.6955, isQueued=1)
    #конец забора вверх  
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 236.6166 , -3.4984, 49.1397, -43.6925, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 236.6166 , -3.4984, 49.1397, -43.6925, isQueued=1)
    #конец забор 
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 35.4201, -230.5215, 42.3953, -124.1102, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 35.4201, -230.5215, 42.3953, -124.1102, isQueued=1)

    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 35.4201, -230.5215, 42.3953, -124.1102, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 35.4201, -230.5215, 42.3953, -124.1102, isQueued=1)

    #выкинуть1
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 236.6166, -3.4984, 49.1397, -43.6925, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 236.6166, -3.4984, 49.1397, -43.6925, isQueued=1)
    #выкинуть2
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 236.6166, -3.4984, 49.1397, 30.0, isQueued=1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, 236.6166, -3.4984, 49.1397, 30.0, isQueued=1)

    print("all command added to queue")
    execute();

def abortcandies():
    #конец линии 
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 10, -230.5215, 42.3953, -124.1102, 820, isQueued=1)
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 10, -230.5215, 42.3953, -124.1102, 820, isQueued=1)
    #точка высыпания 
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 10, -193.8299, 92.5204, -85.5014 ,  820, isQueued=1)
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 10, -193.8299, 92.5204, -85.5014 ,  820, isQueued=1)

    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 10, -232.4232, 91.1334, -84.8132 , 840, isQueued=1)
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 10, -232.4232, 91.1334, -84.8132 , 840, isQueued=1)

    #точка высыпания 
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 10, -232.4232, 91.1334, -35.7132 ,  840, isQueued=1)
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 10, -232.4232, 91.1334, -35.7132 ,  840, isQueued=1)

    #конец   
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 10, -232.4232,   91.1334, -120.9131,  0, isQueued=1)
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, 10, -232.4232,   91.1334, -120.9131,  0, isQueued=1)

    execute();

def goodbye():
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, -30.0, -100.0,  50.0,    -100.0,  400, isQueued=1)
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, -30.0, -100.0,  50.0,    -100.0,  400, isQueued=1)

    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, -130.0,  -250.0,  140.0,   -240.0,  400, isQueued=1)
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, -130.0, -250.0,  140.0,   -190.0,  400, isQueued=1)

    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, -130.0,  -250.0,  140.0,   -240.0,  400, isQueued=1)
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, -130.0, -250.0,  140.0,   -190.0,  400, isQueued=1)
    
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, -130.0,  -250.0,  140.0,   -240.0,  400, isQueued=1)
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVJXYZMode, -130.0, -250.0,  140.0,   -190.0,  400, isQueued=1)
    execute();

def execute():
    #Start to Execute Command Queued
    dType.SetQueuedCmdStartExec(api)
    #Wait for Executing Last Command 
    #while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
    #    dType.dSleep(30)
    #dType.SetQueuedCmdStopExec(api)
    print("ended queue")

def disconnect():
    #Disconnect Dobot
    dType.DisconnectDobot(api)
    print("Connect status:",CON_STR[state])
