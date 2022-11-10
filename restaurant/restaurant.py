import check50
import check50.c
import re

@check50.check()
def exists():
    """restaurant.c exists"""
    check50.exists("restaurant.c")
    
@check50.check(exists)
def compiles():
    """restaurant.c compiles"""
    check50.c.compile("restaurant.c", lcs50=True)
