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
