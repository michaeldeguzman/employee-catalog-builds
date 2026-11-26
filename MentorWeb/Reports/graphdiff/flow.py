import json,sys
def load(p):
    L=open(p).read().split("\n"); return json.loads(L[1])
d=load(sys.argv[1]); N=d["nodes"]; K=[n["_key"] for n in N]
out={}
for s,t,a in zip(d["edgeSrc"],d["edgeDst"],d["edgeAttr"]): out.setdefault(s,[]).append((t,a))
def find(name,typ):
    return [i for i,n in enumerate(N) if n.get("_type")==typ and n.get("DisplayName",n.get("Name"))==name]
def show(i,depth=0,seen=None,maxd=3):
    n=N[i]; label=n.get("DisplayName") or n.get("Label") or n.get("Name") or n.get("Value") or n.get("TextValue") or n.get("Operator") or ""
    print("  "*depth+f"[{n['_type']}] {str(label)[:90]}  <{n['_key'].split('*')[-1][:30]}>", {k:n[k] for k in ("X","Y") if k in n})
    if depth>=maxd: return
    for t,a in out.get(i,[]):
        print("  "*(depth+1)+"->",a.get("_type"),a.get("relationType",""),a.get("index",""))
        show(t,depth+2,seen,maxd)
sa=find(sys.argv[2],"IServerAction")
for i in sa:
    print("== action",sys.argv[2]); 
    # list children
    for t,a in out.get(i,[]):
        n=N[t]; print(" child",a.get("_type"),n["_type"],n.get("DisplayName") or n.get("Name") or "",n["_key"].split("*")[-1][:30],{k:n[k] for k in ("X","Y") if k in n})
