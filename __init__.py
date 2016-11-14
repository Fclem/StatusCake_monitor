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
	
	# clem 14/11/2011
	@staticmethod
	def _make_dict(data, prop_sep='&', kv_sep='='):
		a_dict = dict()
		for each in data.split(prop_sep):
			key, value = each.split(kv_sep, 1)
			a_dict.update({key: value})
		return a_dict
	
	def _send(self, check_instance):
		""" send a poll to the StatusCake TestID """
		assert isinstance(check_instance, CheckObject)
		data = self._make_dict(self._conf.api_data % (check_instance.check_api_key, check_instance.id))
		return self._sender(self._host_url, self._gen_url(), HTTPMethods.GET, data)
	
	# clem 10/11/2016
	def _gen_url(self):
		return self._base_end_point_url

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
