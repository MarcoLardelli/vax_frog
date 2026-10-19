import re,sys
s=open(sys.argv[1]).read()
# tokenize preserving comments/strings: work on top-level forms
def forms(s):
    i=0;depth=0;inbar=False;st=None;res=[];last=0
    while i<len(s):
        c=s[i]
        if inbar:
            if c=='|': inbar=False
        elif c==';':
            while i<len(s) and s[i]!='\n': i+=1
            continue
        elif c=='|': inbar=True
        elif c=='(':
            if depth==0: st=i
            depth+=1
        elif c==')':
            depth-=1
            if depth==0: res.append((st,i+1))
        i+=1
    return res
def strip_comments(f):
    out=[];inbar=False;i=0
    while i<len(f):
        c=f[i]
        if inbar:
            out.append(c)
            if c=='|': inbar=False
        elif c==';':
            while i<len(f) and f[i]!='\n': i+=1
            continue
        else:
            if c=='|': inbar=True
            out.append(c)
        i+=1
    return ''.join(out)
cnt=[0]
out=[];prev=0
for a,b in forms(s):
    f=s[a:b]
    if re.match(r'\(\s*[pP]\s',f):
        f=strip_comments(f)
        k=f.index('-->')
        lhs,rhs=f[:k],f[k:]
        if 'compute' in lhs:
            adds=[]
            def rep(m):
                cnt[0]+=1; v='<zz%d>'%cnt[0]
                adds.append('(zz-arith ^a %s ^op %s ^b %s ^r %s)'%(m.group(1),{'+':'plus','-':'minus'}[m.group(2)],m.group(3),v))
                return v
            # find negated CE containing compute: must be last CE
            negm=re.search(r'-\((?:[^()]|\([^()]*\))*compute(?:[^()]|\([^()]*\))*\)\s*$',lhs)
            if negm:
                pre,neg=lhs[:negm.start()],lhs[negm.start():]
                pre=re.sub(r'\(compute\s+(<[^>]+>)\s*([-+])\s*(\d+)\s*\)',rep,pre)
                neg=re.sub(r'\(compute\s+(<[^>]+>)\s*([-+])\s*(\d+)\s*\)',rep,neg)
                lhs=pre+' '+' '.join(adds)+' '+neg
            else:
                lhs=re.sub(r'\(compute\s+(<[^>]+>)\s*([-+])\s*(\d+)\s*\)',rep,lhs)
                lhs=lhs.rstrip()+' '+' '.join(adds)+'\n '
            assert 'compute' not in lhs, lhs
        f=lhs+rhs
    out.append(s[prev:a]); out.append(f); prev=b
out.append(s[prev:])
r=''.join(out)
# colon outside strings/comments -> _
o=[];inbar=False;incom=False
for c in r:
    if incom:
        if c=='\n': incom=False
    elif inbar:
        if c=='|': inbar=False
    elif c==';': incom=True
    elif c=='|': inbar=True
    elif c==':': c='_'
    o.append(c)
r=''.join(o)
arith='(literalize zz-arith a op b r)\n'
r=r.replace('(startup', arith+'(startup',1)
open(sys.argv[2],'w').write(r)
print('computes replaced',cnt[0])
