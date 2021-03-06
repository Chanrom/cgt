import sys
from cgt.core import UNARY_INFO, BINARY_INFO
import cgt, os, os.path as osp
fh = sys.stdout

os.chdir(osp.dirname(osp.dirname(osp.realpath(cgt.__file__))))

with open("cgt/api_autogen.py","w") as fh:
    fh.write("# This file was autogenerated by gen_py.py. Do not edit.")
    fh.write("\nfrom . import core\n")

    for (shortname,info) in sorted(UNARY_INFO.iteritems(), key = lambda x:x[0]):    
        fh.write(
"""
def {npname}(x):
    "Applies function {npname} elementwise to argument x"
    return core.Result(core.ElwiseUnary("{shortname}"), [x])
    """.format(shortname=shortname,npname=info.short.lower()))

    for (infixname,info) in sorted(BINARY_INFO.iteritems(), key = lambda x:x[1].short):    
        fh.write(
"""
def {npname}(x, y):
    "Applies function {npname} elementwise to arguments x,y"
    return core.elwise_binary("{infixname}", x,y)
    """.format(infixname = infixname, npname=info.short))
    
