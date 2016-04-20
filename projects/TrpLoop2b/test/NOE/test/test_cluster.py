import numpy as np
import mdtraj as md
import os, sys

t=md.load('traj0.xtc',top='conf.gro')

#a=np.load('Assignments.npy')
Ind = np.array([[5,7],[5,11],[5,27],[7,27],[8,7],[8,27],[13,7],[13,16],[14,7],[10,7],[11,7],[10,14],[11,14],[29,46],[29,27],[29,51],[31,35],[31,46],[32,27],[37,35],[37,40],[42,40],[42,44],[44,27],[53,55],[53,58],[53,59],[53,75],[56,75],[61,56],[61,64],[61,59],[62,56],[62,59],[51,55],[51,58],[77,79],[77,85],[77,51],[77,89],[79,85],[79,75],[85,75],[85,89],[91,93],[91,94],[91,96],[91,97],[91,89],[91,111],[93,89],[94,89],[113,115],[113,116],[113,118],[113,119],[113,111],[113,133],[115,111],[116,111],[118,111],[119,111],[135,137],[135,143],[135,144],[135,133],[135,152],[154,152],[154,159],[155,152],[155,159],[161,163],[161,164],[161,167],[161,178],[161,159],[161,183],[163,159],[164,167],[164,178],[164,159],[167,159],[169,167],[169,172],[172,174],[176,178],[185,178],[185,187],[185,188],[185,191],[185,183],[185,205],[187,183],[187,205],[188,183],[188,205],[191,183],[188,205],[191,183],[183,159],[207,210],[207,212],[207,213],[207,205],[207,222],[210,205],[218,217],[212,217],[212,218],[212,205],[224,226],[224,232],[224,233],[224,213],[224,212],[224,222],[224,241],[226,222],[226,241],[235,222],[235,241],[232,222],[232,241],[233,222],[228,222],[229,222],[230,222],[228,241],[229,241],[230,241],[243,245],[243,246],[243,248],[243,249],[243,241],[243,265],[245,241],[246,241],[252,245],[252,246],[252,254],[252,248],[252,249],[248,241],[249,241],[258,257],[267,269],[267,271],[267,272],[267,273],[267,275],[267,276],[267,277],[267,281],[269,281],[271,281],[272,281],[273,281],[275,269],[276,269],[277,269],[275,281],[276,281],[277,281],[283,286],[283,281],[283,305],[285,289],[285,281],[286,44],[286,289],[286,281],[291,289],[291,294],[300,298],[296,298],[294,27],[307,313],[307,322],[307,305],[309,313],[309,322],[309,305],[310,313],[310,322],[310,305],[313,305],[322,305],[315,313],[315,322],[320,313],[320,322]])
print len(Ind)
sys.exit()
for i in range(250):
        b=np.load('state%d.npy'%i)
        print i
        p=[]
        for z in b:
                d=md.compute_distances(t[z],Ind)
                p.append(d)
        u=[]
        v=[]
        w=[]
        for l in range(206):
                r=[]
                for j in range(len(p)):
                        r.append(p[j][0][l])
                        #       m=p[:,l].mean()
                        #       a.append(m)
                        #       e=((p[:,l]**-6.0).mean())**(-1./6.)
                        #       c.append(e)
                f=np.mean(r)
                u.append(f)
                e=[]
                for n in r:
                        s=n**-6.0
                        e.append(s)
                k=np.mean(e)**(-1./6.)
                w.append(k)

#        for y in w:
#                x=y**(-1./6.)
#                v.append(x)
        np.savetxt("state%d/average_whole_state%d.txt"%(i,i),u)
        np.savetxt("state%d/rminus6_whole_state%d.txt"%(i,i),w)
