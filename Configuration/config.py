# -*- coding: utf-8 -*-

#  ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗ ██╗   ██╗██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
# ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝ ██║   ██║██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
# ██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗██║   ██║██████╔╝███████║   ██║   ██║██║   ██║██╔██╗ ██║
# ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║██║   ██║██╔══██╗██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
# ╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
#  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                                                                                         
                                                                      
# DESCRIPTION:
# Contains Pauli's project main data and api functions:




# ======================================================== DEPENDENCIES

# Development:
from pauli_sdk.Modules import constants as _PAULI_Constants
from Modules.SAT import electronic_accounting as _Electronic_Accounting
from Modules.SAT import files_handler as _Files_Handler
from Modules.Finkok import utilities as _Finkok_Utilities






# ======================================================== MODULE CODE

# Params validation properties:
list_item_specification = _PAULI_Constants.LIST_ITEM_SPECIFICATION
dict_item_specification = _PAULI_Constants.DICT_ITEM_SPECIFICATION
required_params = _PAULI_Constants.REQUIRED_PARAMS
value_type = _PAULI_Constants.VALUE_TYPE
param_type = _PAULI_Constants.PARAM_TYPE
obligatory = _PAULI_Constants.OBLIBATORY_PARAM
optional = _PAULI_Constants.OPTIONAL_PARAM
instance = _PAULI_Constants.INSTANCE
private_API_key = _PAULI_Constants.PRIVATE_API_KEY
public_function = _PAULI_Constants.PUBLIC_FUNCTION
private_function = _PAULI_Constants.PRIVATE_FUNCTION	




    #            ██╗      ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██████╗  █████╗ ████████╗ █████╗ 
    #            ╚██╗     ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
    # █████╗█████╗╚██╗    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║  ██║███████║   ██║   ███████║
    # ╚════╝╚════╝██╔╝    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ██║  ██║██╔══██║   ██║   ██╔══██║
    #            ██╔╝     ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║       ██████╔╝██║  ██║   ██║   ██║  ██║
    #            ╚═╝      ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝                                       





# Pauli's project general configuration:
general = {
	# Project name:
	'project_name' : 'Ada',# Our project name
	# Logging data:
	'logging_root' : '/var/log/supervisord/Ada/',# Where to log (absolute path)
	'logging_file_default_name' : 'ADA.log',# Logging file name (justa a file name with .log extension)
	'logging_time_zone' : 'America/Mexico_City',# Log time according with this timezone
	'logging_format' : '%(asctime)s - [%(levelname)s] - %(module)s - %(funcName)s:%(lineno)d - %(message)s',
	'logging_level' : 'debug',
	# Listening data:
	'pauli_project_private_port' : 5002,# Our project is gonna be listening on this port (a number)
	'main_path' : '/ada',# Our project is gonna be listening on this path (/something)
	# Debugging:
	'debugging_available' : True,# If set, every change on the project is gonna be updated (a boolean)
	# DB connection (MongoDB)
	'db' : {
		'host' : 'mongoDBDomain',# Domain of our DB
		'port' : 27017,# DB port (a number)
		'name' : 'dataBaseName'# Mongo data base name
	},# End of db
	'utf' : 'utf8', 
	# Private API key:
	private_API_key : '*_Some_Private_API_Key_'# Use in case of a private API function to authenticate
}# End of general












    #            ██╗       █████╗ ██████╗ ██╗    ███████╗██╗   ██╗███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
    #            ╚██╗     ██╔══██╗██╔══██╗██║    ██╔════╝██║   ██║████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
    # █████╗█████╗╚██╗    ███████║██████╔╝██║    █████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
    # ╚════╝╚════╝██╔╝    ██╔══██║██╔═══╝ ██║    ██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
    #            ██╔╝     ██║  ██║██║     ██║    ██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
    #            ╚═╝      ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                                                                                         
# Types: list, dict, int, float, unicode (str), bool

# Set of API functions information:
functions = {

	# ██████╗ ██╗   ██╗██████╗ ██╗     ██╗ ██████╗
	# ██╔══██╗██║   ██║██╔══██╗██║     ██║██╔════╝
	# ██████╔╝██║   ██║██████╔╝██║     ██║██║     
	# ██╔═══╝ ██║   ██║██╔══██╗██║     ██║██║     
	# ██║     ╚██████╔╝██████╔╝███████╗██║╚██████╗
	# ╚═╝      ╚═════╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝
                                            
	# PUBLIC FUNCTION EXAMPLE:
	'generate_chart_of_accounts' : {
		# Function information:
		public_function : True,
		required_params : {# Required params is a "dict_item_specification"
			'certificates' : {
				value_type : dict,
				param_type : obligatory,
				dict_item_specification : {
					'cer_file' : {
						value_type : unicode,
						param_type : obligatory
					},
					'key_file' : {
						value_type : unicode,
						param_type : obligatory
					},
					'password' : {
						value_type : unicode,
						param_type : obligatory
					}
				}
			},
			'identifier' : {
				value_type : unicode,
				param_type : obligatory,
			},# End of identifier
			'month' : {
				value_type : unicode,
				param_type : obligatory
			},# End of month
			'year' : {
				value_type : unicode,
				param_type : obligatory
			},# End of year
			'accounts' : {
				value_type : list,
				param_type : obligatory,
				list_item_specification : {
					value_type : dict,
					param_type : obligatory,
					dict_item_specification : {
						'grouping_code' : {
							value_type : unicode,
							param_type : obligatory
						},
						'internal_code' : {
							value_type : unicode,
							param_type : obligatory
						},
						'description' : {
							value_type : unicode,
							param_type : obligatory
						},
						'parent' : {
							value_type : unicode,
							param_type : optional
						},
						'level' : {
							value_type : unicode,
							param_type : obligatory
						},
						'nature' : {
							value_type : unicode,
							param_type : obligatory
						}
					}#End of 
				}#End of ListItemSpecification
			} # End of accounts
		},# End of required params
		instance : _Electronic_Accounting.chart_of_accounts
	},# End of generate_chart_of_accounts

	'generate_trial_balance' : {
		# Function information:
		public_function : True,
		required_params : {# Required params is a "dict_item_specification"
			'certificates' : {
				value_type : dict,
				param_type : obligatory,
				dict_item_specification : {
					'cer_file' : {
						value_type : unicode,
						param_type : obligatory
					},
					'key_file' : {
						value_type : unicode,
						param_type : obligatory
					},
					'password' : {
						value_type : unicode,
						param_type : obligatory
					}
				}
			},
			'identifier' : {
				value_type : unicode,
				param_type : obligatory,
			},# End of identifier
			'month' : {
				value_type : unicode,
				param_type : obligatory
			},# End of month
			'year' : {
				value_type : unicode,
				param_type : obligatory
			},# End of year
			'type_of_shipment' : {
				value_type : unicode,
				param_type : obligatory
			},# End of type_of_shipment
			'date_of_last_modified' : {
				value_type : unicode,
				param_type : optional
			},# End of year
			'accounts' : {
				value_type : list,
				param_type : obligatory,
				list_item_specification : {
					value_type : dict,
					param_type : obligatory,
					dict_item_specification : {
						'internal_code' : {
							value_type : unicode,
							param_type : obligatory
						},
						'opening_balance' : {
							value_type : unicode,
							param_type : obligatory
						},
						'debit' : {
							value_type : unicode,
							param_type : obligatory
						},
						'credit' : {
							value_type : unicode,
							param_type : obligatory
						},
						'final_balance' : {
							value_type : unicode,
							param_type : obligatory
						},
					}#End of 
				}#End of ListItemSpecification
			} # End of accounts
		},# End of required params
		instance : _Electronic_Accounting.trial_balance
	},# End of our_public_function

	'get_type_of_keys' : {
		# Function information:
		public_function : True,
		required_params : {# Required params is a "dict_item_specification"
			'certificates' : {
				value_type : dict,
				param_type : obligatory,
				dict_item_specification : {
					'cer_file' : {
						value_type : unicode,
						param_type : obligatory
					},
					'key_file' : {
						value_type : unicode,
						param_type : optional
					},
					'password' : {
						value_type : unicode,
						param_type : optional
					}
				}
			}
		},# End of required params
		instance : _Files_Handler.get_type_of_keys
	},# End of our_public_function

	'get_xml_from_finkok' : {
		# Function information:
		public_function : True,
		required_params : {# Required params is a "dict_item_specification"
			'identifier' : {
				value_type : unicode,
				param_type : obligatory
			},
			'uuid' : {
				value_type : unicode,
				param_type : optional
			}
		},# End of required params
		instance : _Finkok_Utilities.get_xml
	},# End of our_public_function


	# ██████╗ ██████╗ ██╗██╗   ██╗ █████╗ ████████╗███████╗
	# ██╔══██╗██╔══██╗██║██║   ██║██╔══██╗╚══██╔══╝██╔════╝
	# ██████╔╝██████╔╝██║██║   ██║███████║   ██║   █████╗  
	# ██╔═══╝ ██╔══██╗██║╚██╗ ██╔╝██╔══██║   ██║   ██╔══╝  
	# ██║     ██║  ██║██║ ╚████╔╝ ██║  ██║   ██║   ███████╗
	# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚══════╝                                      


}# End of functions







