import json,sys,collections
def load(p):
    L=open(p).read().split("\n"); d=json.loads(L[1]); return d
CONT=("IServerAction","IMobileScreen","IClientAction","IEntity","IMobileFlow","ITimer","IESpace","IReference","IRole","IStructure","ITheme","IMobileBlock","IAction","IConsumedRESTAPI","ISiteProperty","IResource","IStaticEntity","IImage")
def build(d):
    N=d["nodes"]; K=[n["_key"] for n in N]
    inn={}
    for s,t,a in zip(d["edgeSrc"],d["edgeDst"],d["edgeAttr"]): inn.setdefault(t,[]).append((s,a))
    return N,K,inn
def container(i,N,inn,own):
    seen={i}; q=[i]
    while q:
        j=q.pop(0); n=N[j]
        if j!=i and n["_type"] in CONT and n["_key"].startswith(own): return f'{n["_type"]}:{n.get("DisplayName") or n.get("Name")}'
        if j==i and n["_type"] in CONT: return f'{n["_type"]}:{n.get("DisplayName") or n.get("Name")}'
        for s,a in inn.get(j,[]):
            if a.get("_type") in ("ValidationMessages",): continue
            if s not in seen: seen.add(s); q.append(s)
    return "?"
own="7skC5R_8TVsV6FYAotkxDn*"
da,db=load(sys.argv[1]),load(sys.argv[2])
Na,Ka,ia=build(da); Nb,Kb,ib=build(db)
ma={n["_key"]:(n,i) for i,n in enumerate(Na)}; mb={n["_key"]:(n,i) for i,n in enumerate(Nb)}
res=collections.defaultdict(lambda: collections.Counter())
for k,(n,i) in mb.items():
    if k not in ma: res[container(i,Nb,ib,own) if k.startswith(own) else "LIBRARY/"+k.split("*")[0][:6]]["added"]+=1
    elif ma[k][0]!=n:
        fields=set(f for f in set(n)|set(ma[k][0]) if n.get(f)!=ma[k][0].get(f))
        coord = fields<= {"X","Y"}
        res[container(i,Nb,ib,own) if k.startswith(own) else "LIBRARY/"+k.split("*")[0][:6]]["changed(layout X/Y only)" if coord else "changed"]+=1
for k,(n,i) in ma.items():
    if k not in mb: res[container(i,Na,ia,own) if k.startswith(own) else "LIBRARY/"+k.split("*")[0][:6]]["removed"]+=1
for c,v in sorted(res.items()): print(f"{c:60s}",dict(v))
