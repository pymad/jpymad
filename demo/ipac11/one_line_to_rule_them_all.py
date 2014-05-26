from matplotlib import pyplot as plt
from cern.jpymad import JPymadService as pm

# this one line does it "all":
# - starts madx
# - loads model lhc, default parameters
# - runs twiss on default sequence
# - returns the twiss table as a python lookup dictionary
# - since "reference count" for the model instance reaches zero,
#   madx process is terminated
tw, _ = pm().create_model('lhc').twiss()

# to prove it:
plt.plot(tw.s,tw.betx)
plt.show()
