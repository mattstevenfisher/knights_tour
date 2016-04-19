import time

_start_time = {}
_elapsed_time = {}
	
def tic(ind='_default'):
	_start_time[ind] = time.time()
	
	
def toc(ind = '_default'):
	if ind in _start_time:
		_elapsed_time[ind] = time.time() - _start_time[ind]
		print 'Elapsed time: {0:.7f} seconds'.format(_elapsed_time[ind])
		return _elapsed_time[ind]
	else:
		print 'Timer not started. Use tic() to start.'