# -*- coding: utf-8 -*-

# ███████╗ █████╗ ████████╗    ██████╗  █████╗ ████████╗ █████╗ 
# ██╔════╝██╔══██╗╚══██╔══╝    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
# ███████╗███████║   ██║       ██║  ██║███████║   ██║   ███████║
# ╚════██║██╔══██║   ██║       ██║  ██║██╔══██║   ██║   ██╔══██║
# ███████║██║  ██║   ██║       ██████╔╝██║  ██║   ██║   ██║  ██║
# ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
                                                                               
# DESCRIPTION:
# Contains the local constants that are used in a Pauli's project.




# ======================================================== DEPENDENCIES

# Native:

# External:

# SDK:

# Development:
from Modules.General import constants as _Constants

# ======================================================== MODULE CODE

 #  _____   ____   _____ _    _ __  __ ______ _   _ _______ _____ 
 # |  __ \ / __ \ / ____| |  | |  \/  |  ____| \ | |__   __/ ____|
 # | |  | | |  | | |    | |  | | \  / | |__  |  \| |  | | | (___  
 # | |  | | |  | | |    | |  | | |\/| |  __| | . ` |  | |  \___ \ 
 # | |__| | |__| | |____| |__| | |  | | |____| |\  |  | |  ____) |
 # |_____/ \____/ \_____|\____/|_|  |_|______|_| \_|  |_| |_____/ 

CHART_OF_ACCOUNTS = 'Chart_of_Accounts' 
TRIAL_BALANCE = 'Trial_Balance' 


 #  _____       _______         _________     _______  ______ 
 # |  __ \   /\|__   __|/\     |__   __\ \   / /  __ \|  ____|
 # | |  | | /  \  | |  /  \       | |   \ \_/ /| |__) | |__   
 # | |  | |/ /\ \ | | / /\ \      | |    \   / |  ___/|  __|  
 # | |__| / ____ \| |/ ____ \     | |     | |  | |    | |____ 
 # |_____/_/    \_\_/_/    \_\    |_|     |_|  |_|    |______|
class Sat_type(object):
	pass

class Account(Sat_type):
	pass

class Default_class(Sat_type):
	pass

 #   _____ ____  _   _  _____ _______       _   _ _______ _____ 
 #  / ____/ __ \| \ | |/ ____|__   __|/\   | \ | |__   __/ ____|
 # | |   | |  | |  \| | (___    | |  /  \  |  \| |  | | | (___  
 # | |   | |  | | . ` |\___ \   | | / /\ \ | . ` |  | |  \___ \ 
 # | |___| |__| | |\  |____) |  | |/ ____ \| |\  |  | |  ____) |
 #  \_____\____/|_| \_|_____/   |_/_/    \_\_| \_|  |_| |_____/ 

SAT_TYPE = Sat_type

CLASSES = {
	'accounts' : Account,
	'account' : Account
}

DEFAULT_CLASS = Default_class

 #  _______ _____            _   _  _____ _            _______ ______ 
 # |__   __|  __ \     /\   | \ | |/ ____| |        /\|__   __|  ____|
 #    | |  | |__) |   /  \  |  \| | (___ | |       /  \  | |  | |__   
 #    | |  |  _  /   / /\ \ | . ` |\___ \| |      / /\ \ | |  |  __|  
 #    | |  | | \ \  / ____ \| |\  |____) | |____ / ____ \| |  | |____ 
 #    |_|  |_|  \_\/_/    \_\_| \_|_____/|______/_/    \_\_|  |______|

DOCUMENT_TRANSLATE = {
	CHART_OF_ACCOUNTS : {
		'version':'Version',
		'identifier':'RFC', 
		'month':'Mes', 
		'year':'Anio',
		"accounts" : 'Ctas',
		"grouping_code" : "CodAgrup",
		"internal_code" : "NumCta",
		"description" : "Desc",
		"parent" : "SubCtaDe",
		"level" : "Nivel",
		"nature" : "Natur"
	},
	TRIAL_BALANCE : {
		'version':'Version',
		'identifier':'RFC', 
		'month':'Mes', 
		'year':'Anio',
		'type_of_shipment' : 'TipoEnvio',
		'date_of_last_modified' : 'FechaModBal',
		"accounts" : 'Ctas',
		"internal_code" : "NumCta",
		"opening_balance" : "SaldoIni",
		"debit" : "Debe",
		"credit" : "Haber",
		"final_balance" : "SaldoFin"
	}
}

 #  __  __ ______ _______       _____       _______       
 # |  \/  |  ____|__   __|/\   |  __ \   /\|__   __|/\    
 # | \  / | |__     | |  /  \  | |  | | /  \  | |  /  \   
 # | |\/| |  __|    | | / /\ \ | |  | |/ /\ \ | | / /\ \  
 # | |  | | |____   | |/ ____ \| |__| / ____ \| |/ ____ \ 
 # |_|  |_|______|  |_/_/    \_\_____/_/    \_\_/_/    \_\                                                   

ROOT = {
	CHART_OF_ACCOUNTS : 'Catalogo',
	TRIAL_BALANCE : 'Balanza'	
}

NAMESPACE = {
	CHART_OF_ACCOUNTS : 'catalogocuentas',
	TRIAL_BALANCE : 'BCE'
}

NSMAP = {
	CHART_OF_ACCOUNTS : {
		'catalogocuentas' : 'www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas',
		 'xsi' : 'http://www.w3.org/2001/XMLSchema-instance'
	},
	TRIAL_BALANCE : {
		'BCE' : 'www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion',
		'xsi' : 'http://www.w3.org/2001/XMLSchema-instance'
	}
}

XSD = {
	CHART_OF_ACCOUNTS :'www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas http://www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas/CatalogoCuentas_1_1.xsd',
	TRIAL_BALANCE :'www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion http://www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion/BalanzaComprobacion_1_1.xsd'
}

XSLT = {
	CHART_OF_ACCOUNTS : _Constants.SOURCE_PATH + 'CatalogoCuentas_1_1.xslt',
	TRIAL_BALANCE : _Constants.SOURCE_PATH + 'BalanzaComprobacion_1_1.xslt'	
}
