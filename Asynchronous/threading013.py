"""
Timer
A threading.Timer is a way to schedule a function to be called 
after a certain amount of time has passed. You create a Timer 
by passing in a number of seconds to wait and a function to 
call:

t = threading.Timer(30.0, my_function)

You start the Timer by calling .start(). The function will be 
called on a new thread at some point after the specified time, 
but be aware that there is no promise that it will be called 
exactly at the time you want.

If you want to stop a Timer that you’ve already started, you 
can cancel it by calling .cancel(). Calling .cancel() after 
the Timer has triggered does nothing and does not produce an 
exception.

A Timer can be used to prompt a user for action after a 
specific amount of time. If the user does the action before 
the Timer expires, .cancel() can be called.
"""
