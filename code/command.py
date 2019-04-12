from time import sleep
commandfile = 'command.txt'
flag_state = 'None'
def write(event):
    global flag_state
    f = open(commandfile,"w+")
    f.write(event)
    f.close()
    if flag_state == '0':
        flag_state = '1'
    else:
        flag_state = '0'
    sleep(1)

while True:
    write(flag_state+','+'U')
    write(flag_state+','+'blink')
    write(flag_state+','+'L')