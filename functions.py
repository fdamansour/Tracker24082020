

def mouseClicked(event,iLoop):
    # nonlocal iLoop
    # global iLoop
    
    if (iLoop % 2)== 0:
        sw.Start()
    else:  
        sw.Stop()
    iLoop+=1
    
    return 1

