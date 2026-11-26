import json,sys,collections
def load(p):
    L=open(p).read().split("\n"); h=json.loads(L[0]); d=json.loads(L[1]); return h,d
def idx(d):
    nodes=d["nodes"]
    keys=[n.get("_key") for n in nodes]
    nmap={}
    for n in nodes: nmap[n.get("_key")]=json.dumps(n,sort_keys=True)
    edges=collections.Counter()
    for s,t,a in zip(d["edgeSrc"],d["edgeDst"],d["edgeAttr"]):
        edges[(keys[s],keys[t],json.dumps(a,sort_keys=True))]+=1
    return nodes,keys,nmap,edges
ha,da=load(sys.argv[1]); hb,db=load(sys.argv[2])
print("A",ha["revision"],len(da["nodes"]),len(da["edgeSrc"]),"B",hb["revision"],len(db["nodes"]),len(db["edgeSrc"]))
na,ka,ma,ea=idx(da); nb,kb,mb,eb=idx(db)
print("dup keys A",len(ka)-len(set(ka)),"B",len(kb)-len(set(kb)))
added=[k for k in mb if k not in ma]; removed=[k for k in ma if k not in mb]
changed=[k for k in mb if k in ma and ma[k]!=mb[k]]
print("nodes added",len(added),"removed",len(removed),"changed",len(changed))
def owner(k): return (k or "").split("*")[-1].split(".")[0]
typ={n.get("_key"):n.get("_type") for n in nb}; typa={n.get("_key"):n.get("_type") for n in na}
print("top-level keys equal:",{k:da[k]==db[k] for k in ("v","key","roots")})
for lbl,ks,t in (("ADDED",added,typ),("REMOVED",removed,typa),("CHANGED",changed,typ)):
    c=collections.Counter(t.get(k) for k in ks); print(lbl,dict(c))
    c2=collections.Counter(owner(k) for k in ks); print(" owners",dict(c2.most_common(15)))
re_=eb-ea; ra=ea-eb
print("edges added",sum(re_.values()),"removed",sum(ra.values()))
print(" edge owners added",dict(collections.Counter(owner(k[0]) for k in re_.elements()).most_common(15)))
print(" edge owners removed",dict(collections.Counter(owner(k[0]) for k in ra.elements()).most_common(15)))
if len(sys.argv)>3:
    for k in (added+removed+changed)[:int(sys.argv[3])]:
        print(k, (mb.get(k) or ma.get(k))[:300])
