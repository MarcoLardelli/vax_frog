import pexpect,sys,re
answers={'Luftdruck':'1012 1008 1003','Jahreszeit':'s','Windrichtung':'200 230 250','Windstaerke':'2 3 4',
'Luftfeuchtigkeit':'60 70 80','Nebel':'0 0 0','Lufttemperatur':'24 23 21','Wolkendichte':'2 3 5',
'Wolkentyp':'ci as ns','Regen':'0 0 5'}
script=sys.argv[1:]  # later answers
c=pexpect.spawn('sbcl --noinform --non-interactive --load load.lisp --eval \'(ops::run-vaxfrog "test.ops")\'',encoding='latin-1',timeout=30)
# usage: python3 drive.py j n b u e n q   (answers to the yes/no and menu prompts in order)
c.logfile_read=open('session.log','w')
pats=[r'-return-\s*:?\s*',r'(Luftdruck in Milibar|Jahreszeit\?|Windrichtung ein|Windstaerke ein|Luftfeuchtigkeit ein|Hat es Nebel|Lufttemperatur \?|Wolkendichte\?|Dominierender Wolkentyp|Hat es Regen\?)',r'\?\s*J,N|j,n\s*:|J/N|j,n :',r'Waehlen Sie[^:]*:|ein \(oder HELP\) :',r'Kondens|geben sie .a.,.b. oder',r'\(S\)tarken Tau',pexpect.EOF,pexpect.TIMEOUT]
key={'Luftdruck in Milibar':'Luftdruck','Jahreszeit?':'Jahreszeit','Windrichtung ein':'Windrichtung','Windstaerke ein':'Windstaerke','Luftfeuchtigkeit ein':'Luftfeuchtigkeit','Hat es Nebel':'Nebel','Lufttemperatur ?':'Lufttemperatur','Wolkendichte?':'Wolkendichte','Dominierender Wolkentyp':'Wolkentyp','Hat es Regen?':'Regen'}
si=0
for step in range(200):
    i=c.expect(pats)
    if i==0: c.sendline('')
    elif i==1: c.sendline(answers[key[c.match.group(1)]])
    elif i in (2,3,4,5):
        a=script[si] if si<len(script) else 'q'; si+=1; c.sendline(a)
    elif i==6: break
    else: print('TIMEOUT'); break
