
baskets =[55, 275, 495, 715]

import threading
import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

#Load Dll
api = dType.load()

#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])

if (state == dType.DobotConnect.DobotConnect_NoError):

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
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 232.1355, -2.7885, 99.0417, 48.8663, 0.0, isQueued=1)

    #495
    basket=baskets[2]


    basketIndex=dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 232.1355, -2.7885, 99.0417, 48.8663, basket, isQueued=1)[0]
    print(basketIndex)


    #старт забора
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 294.0566, -13.8674, -20.0509, 46.8545, basket, isQueued=1)
    #забор   
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 298.5595, -12.0067, -60.2918, -15.7484, basket, isQueued=1)
    #поднял конфеты  
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 266.7224 , -10.4796, 24.4154, -15.6955, basket, isQueued=1)
    #конец забора вверх  
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 236.6166 , -3.4984, 49.1397, -43.6925 ,  basket, isQueued=1)
    #конец забор 
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 35.4201, -230.5215, 42.3953, -124.1102 ,  basket, isQueued=1)




    #конец линии 
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 10, -230.5215, 42.3953, -124.1102, 820, isQueued=1)
    #точка высыпания 
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 10, -193.8299, 92.5204, -85.5014 ,  820, isQueued=1)
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 10, -232.4232, 91.1334, -84.8132 , 840, isQueued=1)
    #точка высыпания 
    dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 10, -232.4232, 91.1334, -35.7132  ,  840, isQueued=1)


    #конец   
    lastIndex= dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 10, -232.4232,   91.1334, -120.9131  ,  0, isQueued=1)[0]


    #Start to Execute Command Queued
    dType.SetQueuedCmdStartExec(api)

    #Wait for Executing Last Command 
    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(300)

    #Stop to execute command queued
    dType.SetQueuedCmdStopExec(api)

