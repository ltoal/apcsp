import check50
import check50.c

@check50.check()
def exists():
    """typecastingCL.c exists"""
    check50.exists("typecastingCL.c")
    
@check50.check(exists)
def compiles():
    """typecastingCL.c compiles"""
    check50.c.compile("typecastingCL.c", lcs50=True)
    
@check50.check(compiles)
def handles_no_arg():
    """typecastingCL.c handles no arguments"""
    check50.run("./typecastingCL").exit(1)
    
@check50.check(compiles)
def handles_one_arg():
    """typecastingCL.c handles one argument"""
    check50.run("./typecastingCL A").exit(1)
    
@check50.check(compiles)
def handles_too_many_arg():
    """typecastingCL.c handles one argument"""
    check50.run("./typecastingCL hello 2 hello").exit(1)
    
@check50.check(compiles)
def handles_lowercase_inputs():
    """typecastingCL.c handles an all-lowercase input"""
    check50.run("./typecastingCL computer 1").stdout("dpnqvufs").exit(0)
    
@check50.check(compiles)
def handles_uppercase_inputs():
    """typecastingCL.c handles an all-uppercase input"""
    check50.run("./typecastingCL COMPUTER 5").stdout("HTRUZYJW").exit(0)

@check50.check(compiles)
def handles_mixed_inputs():
    """typecastingCL.c handles a mix of uppercase/lowercase/symbols"""
    check50.run("./typecastingCL Hey!! 3").stdout("Kh|$$").exit(0)
