
#%% logging information in a file and/or console
def fn_logMyInfo(msg = "", useConsole = True, useFile = None):
    #%% test parameters
#    msg = 'I want to print this'
#    useConsole = True
#    useFile = os.path.join(outFld, "testlog.txt")
    
    if msg[0] == '\n':
        pass
    else:
        msg = '\n' + msg
    #%% function body
    if useConsole:
        print(msg)
        
    if useFile is not None:
        # actual write to the file
        with open(useFile, "a+") as f:
            f.write(msg)
    #%% return
    # no return here, this is just a logging function
