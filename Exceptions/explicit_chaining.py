#If the raise exception is not caught, python prints both exceptions as part of std error message.
try:
	1/0
except Exception as E:
	raise TypeError('This message too gets printed') from E
	
