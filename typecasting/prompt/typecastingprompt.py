import check50
import check50.c

@check50.check()
def exists():
    """typecastingPrompt.c exists"""
    check50.exists("typecastingPrompt.c")
    
@check50.check(exists)
def compiles():
    """typecastingPrompt.c compiles"""
    check50.c.compile("typecastingPrompt.c", lcs50=True)
    
@check50.check(compiles)
def handles_lowercase_inputs():
    """typecastingCL.c handles an all-lowercase input"""
    check50.run("./typecastingPrompt").stdin("computer").stdin("1").stdout("dpnqvufs").exit(0)
    
@check50.check(compiles)
def handles_uppercase_inputs():
    """typecastingCL.c handles an all-uppercase input"""
    check50.run("./typecastingPrompt").stdin("COMPUTER").stdin("5").stdout("HTRUZYJW").exit(0)

@check50.check(compiles)
def handles_mixed_inputs():
    """typecastingCL.c handles a mix of uppercase/lowercase/symbols"""
    check50.run("./typecastingPrompt").stdin("Hey!!").stdin("3").stdout("Kh|$$").exit(0)
