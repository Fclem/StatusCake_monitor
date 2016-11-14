#!/usr/bin/python
from infra_monitor import *

__author__ = 'clement.fiere@helsinki.fi'
__date__ = '11/11/2016'


##################
# ACTUAL OBJECTS #
##################

class StatusCakeInterface(ServiceInterfaceAbstract):
	""" Interface between configured checks and StatusCake.com PUSH Tests """
	
	def __init__(self, inst_conf=MyConfig()):
		super(StatusCakeInterface, self).__init__(inst_conf)
	
	def _send(self, check_instance):
		""" send a poll to the StatusCake TestID """
		assert isinstance(check_instance, CheckObject)
		return self._sender(self._host_url, self._gen_url(check_instance), 'GET')
	
	# clem 10/11/2016
	def _gen_url(self, check_instance):
		return self._base_end_point_url % (check_instance.check_api_key, check_instance.id)

	def update_check(self, check_instance):
		""" Polls the check, to validate that it is online
		
		:type check_instance: CheckObject
		:rtype:
		"""
		# assert isinstance(check_instance, CheckObject)
		response = self._send(check_instance)
		return response.status == 200
	
	# clem 10/11/2016
	def set_check(self, check_instance, value=False):
		""" Set the check component value to On or Off
		
		:type check_instance: CheckObject
		:type value: bool
		"""
		return self.update_check(check_instance) if value else False
	
	def no_status_change(self, check_instance, old_status, new_status):
		return self.set_check(check_instance, new_status)
	

def main():
	# runs the watcher loop
	return Watcher.loop(StatusCakeInterface(get_config()))


if __name__ == '__main__':
	exit(0 if main() else 1)
else:
	conf = get_config()
