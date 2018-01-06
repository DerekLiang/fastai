from .imports import *
from .torch_imports import *

def accuracy(preds, targs, axis=1):
    preds = np.argmax(preds, axis=axis)
    return (preds==targs).mean()

def accuracy_thresh(thresh):
    return lambda preds,targs: accuracy_multi(preds, targs, thresh)

def accuracy_multi(preds, targs, thresh):
    return ((preds>thresh)==targs).mean()

