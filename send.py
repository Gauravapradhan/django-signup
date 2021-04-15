import request
headers={}
headers['authorization']='Bearer ey2hbdci0i3IVzI1NifsInrSccI6IkpkVC39.ey2402tlb290ex3Izey2hbdci0i3IVzI1NifsInrSccI6IkpkVC39.ey2402tlb290ex3Izey2hbdci0i3IVzI1NifsInrSccI6IkpkVC39.ey2402tlb290ex3Izey2hbdci0i3IVzI1NifsInrSccI6IkpkVC39.ey2402tlb290ex3Iz'
r=request.get('http://127.0.0.1:8000/paradigms',headers=headers)
print(r.text)