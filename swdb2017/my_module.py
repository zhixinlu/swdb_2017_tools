import numpy as np
#test
def downsample(data, n, axis=0):
    """Reduce the number of samples in an array by averaging together
    n samples at a time.

    Parameters
    ----------
    data : array
        The input array to be downsampled.
    n : int
        Downsampling factor; this is the number of raw samples that will be averaged
        together for each new sample.
    axis : int
        The array axis that should be downsampled (default=0).


    Returns
    -------
    array
        An array in which each item is the average of *n* items
        from the input *data* array.
    """
    if n <= 1:
        return data
    new_len = data.shape[axis] // n
    s = list(data.shape)
    s[axis] = new_len
    s.insert(axis+1, n)
    sl = [slice(None)] * data.ndim
    sl[axis] = slice(0, new_len*n)
    d1 = data[tuple(sl)]
    d1.shape = tuple(s)
    d2 = d1.mean(axis+1)
    return d2
