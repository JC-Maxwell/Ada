# -*- coding: utf-8 -*-

# ██╗   ██╗████████╗██╗██╗     ██╗████████╗██╗███████╗███████╗
# ██║   ██║╚══██╔══╝██║██║     ██║╚══██╔══╝██║██╔════╝██╔════╝
# ██║   ██║   ██║   ██║██║     ██║   ██║   ██║█████╗  ███████╗
# ██║   ██║   ██║   ██║██║     ██║   ██║   ██║██╔══╝  ╚════██║
# ╚██████╔╝   ██║   ██║███████╗██║   ██║   ██║███████╗███████║
#  ╚═════╝    ╚═╝   ╚═╝╚══════╝╚═╝   ╚═╝   ╚═╝╚══════╝╚══════╝

                       
# DESCRIPTION:
# Contains the local constants that are used in a Pauli's project.




# ======================================================== DEPENDENCIES

# Native:
import logging
import sys

# External:
from suds.client import Client

# SDK:
from pauli_sdk.Modules import constants as _Pauli_Constants
from pauli_sdk.Modules import helper as _Pauli_Helper
from pauli_sdk.Classes.response import Error
from pauli_sdk.Classes.response import Already_Handled_Exception

# Development:
from Modules.General import constants as _Constants

# ======================================================== MODULE CODE

logger = logging.getLogger('root')

# Our public function explanation must be here:
def get_xml(params):

	try:

		logger.info(_Pauli_Constants.FUNCTION_EXECUTION_BEGINNING_MESSAGE)
			
		# ... C o d e     m o n k e y ...

		identifier = params['identifier']
		uuid = params['uuid']

		username = _Constants.FINKOK_CREDENTIALS['username']
		password = _Constants.FINKOK_CREDENTIALS['password']

		url = "http://facturacion.finkok.com/servicios/soap/utilities.wsdl"
		client = Client(url,cache=None)

		result = client.service.get_xml(username,password,uuid,identifier)
		
		try:
			xml = client.last_received().getChild("senv:Envelope").getChild("senv:Body").getChild("tns:get_xmlResponse").getChild("tns:get_xmlResult").getChild("s0:xml").getText()
			logger.info(_Pauli_Constants.FUNCTION_EXECUTION_ENDING_MESSAGE)
			return xml
		except:
			error = Error(404,'Not found')
			already_handled_exception = Already_Handled_Exception(error)
			raise already_handled_exception	
			
	# Exception was already handled (i.e. error was built and logged in a deeper except) so it just raised to outer excepts(s):
	except Already_Handled_Exception as already_handled_exception:

		# Raise exception to outer except(s)
		raise already_handled_exception

	# Handle other exception (i.e. internal server error)
	except:

		# Get exception:
		other_exception = str(sys.exc_info()[1])
		# Build error from exception:
        other_error = Error(_Pauli_Constants.HTTP_CODES['INTERNAL'],_Pauli_Constants.ERROR_MESSAGES['INTERNAL'])
		# Log exception/error:
        logger.critical(other_error.content + other_exception)
        # Exception was already handled (i.e. error was built and logged int this except) so it is transformed into an already handled exception:
        already_handled_exception = Already_Handled_Exception(other_error)
        # Raise exception to outer except(s):
        raise already_handled_exception