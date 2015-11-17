import os

def intentparse(command):
    text = command.split(' ')[0]
    i = open("logs/intentlogs.txt", 'w')
    t = command
    i.write("t is " + str(t) + '\n')
    q = open('core/intent/questionwords.txt').read()
    if text in q or text in q.lower():
        i.write("is question")
        return "search"
    f = open("core/intent/verblist.txt").read().split('\n')
    for item in f:
        if text.lower()==item.lower():
            i.write("verb")
            return item
    return False

def check2(command, exclude):
    command.replace(exclude, '')
    print exclude
    print "check2"
    text = command.split(' ')[0]
    i = open("logs/intentlogs.txt", 'w')
    t = command
    i.write("t is " + str(t) + '\n')
    i.write("exclude is %s"%exclude+"\n")
    q = open('core/intent/questionwords.txt').read()
    if text.lower() in q or text in q.lower():
        i.write("is question")
        return "search"
    f = open("core/intent/verblist.txt").read().split('\n')
    for item in f:
        if item.lower()==text.lower():
            i.write("verb")
            return item
    return False
