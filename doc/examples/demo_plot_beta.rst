Plot Beta
=========

The following example shows how to use JPyMAD to plot the beta functions for the LHC for injection and collision optics:

code-block:: python

    from matplotlib import pyplot
    from cern.jpymad.service import JPymadService

    def plot_beta(model, postfix=''):
        # Run twiss on the model, optionally give name of file
        # where tfs table is stored
        result, summary = model.twiss(seqname='lhcb1',
                                      columns=['name', 's', 'betx', 'bety'],
                                      file='lhcb1' + postfix + '.tfs')

        pyplot.figure()
        # do something with the result (note, madx is still waiting!):
        pyplot.xlabel('dist. from IP1')
        pyplot.ylabel(r'$\beta$')
        pyplot.plot(result.s, result.betx, label=r'$\beta_x$')
        pyplot.plot(result.s, result.bety, label=r'$\beta_y$')
        pyplot.savefig('beta' + postfix + '.eps')

    mdefname = 'lhc'
    opticname = 'injection'

    # Here it starts:

    # create the JPyMad Service
    pms = JPymadService()

    # print the name of all model definitions
    print(pms.mdefnames)

    # get one model-definition
    model = pms.create_model(mdefname)
    mdef = model.mdef

    # print a list of available sequences:
    print(mdef.seqnames)

    plot_beta(model, '_inj')

    # list the available optics and set a new one
    print(mdef.opticnames)
    model.set_optic(opticname)

    plot_beta(model, '_coll')

    # remove the model from the service:
    pms.delete_model(model)
