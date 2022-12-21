
def init_rand_vars(var_list, **kwargs):
    rnd_seed = kwargs.get('seed', None)
    for v in var_list:
        v.assign_rand(seed=rnd_seed)

    return var_list