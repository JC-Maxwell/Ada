# -*- coding: utf-8 -*-

# ███████╗██╗██╗     ███████╗███████╗    ██╗  ██╗ █████╗ ███╗   ██╗██╗     ██████╗ ███████╗██████╗ 
# ██╔════╝██║██║     ██╔════╝██╔════╝    ██║  ██║██╔══██╗████╗  ██║██║     ██╔══██╗██╔════╝██╔══██╗
# █████╗  ██║██║     █████╗  ███████╗    ███████║███████║██╔██╗ ██║██║     ██║  ██║█████╗  ██████╔╝
# ██╔══╝  ██║██║     ██╔══╝  ╚════██║    ██╔══██║██╔══██║██║╚██╗██║██║     ██║  ██║██╔══╝  ██╔══██╗
# ██║     ██║███████╗███████╗███████║    ██║  ██║██║  ██║██║ ╚████║███████╗██████╔╝███████╗██║  ██║
# ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝

# DESCRIPTION:
# Contains some logic of our project:



# ======================================================== DEPENDENCIES

# Native:
import logging
import sys
import os.path

# SDK:
from pauli_sdk.Modules import constants as _Pauli_Constants
from pauli_sdk.Modules import helper as _Pauli_Helper
from pauli_sdk.Classes.response import Error
from pauli_sdk.Classes.response import Already_Handled_Exception

# Development:
from Modules.General import constants as _Constants
from Modules.General import helper as _Helper




# ======================================================== MODULE CODE

logger = logging.getLogger('root')

# Our public function explanation must be here:
def get_type_of_keys(params):
	try:

		logger.info(_Pauli_Constants.FUNCTION_EXECUTION_BEGINNING_MESSAGE)
			
		# ... C o d e     m o n k e y ...

		certificates = params['certificates']

		# Get type
		file_path = _Constants.BUCKET_PATH + certificates['cer_file']
		
		logger.info(certificates['cer_file'])
		if os.path.isfile(file_path):
			params_process = ['openssl','x509','-inform','DER','-in',file_path,'-subject','-noout']
			if '/OU=' in _Helper.execute_popen_process(params_process):
				result =  'CSD'
			else:
				result = 'FIEL'
			logger.info(result)
		else:
			logger.info('File does not exist')
			# Build error from exception:
			other_error = Error(_Pauli_Constants.HTTP_CODES['BAD_REQUEST'],'File does not exist')
			# Log exception/error:
			logger.critical(other_error.content)
			# Exception was already handled (i.e. error was built and logged int this except) so it is transformed into an already handled exception:
			already_handled_exception = Already_Handled_Exception(other_error)
			# Raise exception to outer except(s):
			raise already_handled_exception
		
		logger.info(_Pauli_Constants.FUNCTION_EXECUTION_ENDING_MESSAGE)

		return result

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

