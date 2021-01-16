import numpy as np
import pandas as pd
import biceps
####### Data and Output Directories #######
energies = np.loadtxt('cineromycin_B/cineromycinB_QMenergies.dat')*627.509  # convert from hartrees to kcal/mol
energies = energies/0.5959   # convert to reduced free energies F = f/kT
energies -= energies.min()  # set ground state to zero, just in case
states = len(energies)
print(f"Possible input data extensions: {biceps.toolbox.list_possible_extensions()}")
input_data = biceps.toolbox.sort_data('cineromycin_B/J_NOE')
print(f"Input data: {biceps.toolbox.list_extensions(input_data)}")
####### Parameters #######
nsteps=1000000
print(f"nSteps of sampling: {nsteps}")
n_lambdas = 3
outdir = '%s_steps_%s_lam'%(nsteps, n_lambdas)
biceps.toolbox.mkdir(outdir)
lambda_values = np.linspace(0.0, 1.0, n_lambdas)
parameters = [dict(ref="uniform", sigma=(0.05, 20.0, 1.02)),
        dict(ref="exp", sigma=(0.05, 5.0, 1.02), gamma=(0.2, 5.0, 1.02)),]
print(pd.DataFrame(parameters))
###### Multiprocessing Lambda values #######
@biceps.multiprocess(iterable=lambda_values)
def mp_lambdas(lam):
#for lam in [0.0]:
    ensemble = biceps.Ensemble(lam, energies)
    ensemble.initialize_restraints(input_data, parameters)
    sampler = biceps.PosteriorSampler(ensemble)
    sampler.sample(nsteps=nsteps, burn=0, print_freq=1000, verbose=0)
    sampler.traj.process_results(outdir+'/traj_lambda%2.2f.npz'%(lam))

'''
####### Convergence Check #######
maxtau=1000
C = biceps.Convergence(filename=outdir+"/traj_lambda0.00.npz",
        outdir=outdir)
C.get_autocorrelation_curves(method="auto", maxtau=maxtau)
C.plot_auto_curve(figname="auto_curve.pdf", xlim=(0, maxtau))
C.process(nblock=5, nfold=10, nround=100, savefile=True,
        block=True, normalize=True)
'''

####### Posterior Analysis #######
A = biceps.Analysis(nstates=states, outdir=outdir)
A.plot()





