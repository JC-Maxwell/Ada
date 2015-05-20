# -*- coding: utf-8 -*-

# ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ 
# ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
# ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
# ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
# ██║  ██║███████╗███████╗██║     ███████╗██║  ██║
# ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                   
# DESCRIPTION
# Contains classes that manage a Pauli's project responses.





# ======================================================== DEPENDENCIES

# Native:
import os
import logging
import sys
import base64
from subprocess import PIPE, Popen
import hashlib

# External:
from M2Crypto import RSA
from lxml import etree as ET
from lxml.builder import ElementMaker # lxml only !

# SDK:
from pauli_sdk.Modules import constants as _Pauli_Constants
from pauli_sdk.Modules import helper as _Pauli_Helper
from pauli_sdk.Classes.response import Error
from pauli_sdk.Classes.response import Already_Handled_Exception

# Development:
from Modules.General import constants as _Constants
from Modules.SAT import sat_data as _SAT_data


# ======================================================== MODULE CODE

logger = logging.getLogger('root')

# Our public function explanation must be here:

def assign_attributes(obj,attributes):
	try:
		for item in attributes:
			if type(attributes[item]) == dict:
				setattr(obj,item,get_class(item)())
				assign_attributes(getattr(obj,item),attributes[item])
			elif type(attributes[item]) == list:
				setattr(obj,item,[])
				for i in attributes[item]:
					getattr(obj,item).append(assign_attributes(get_class(item)(),i))
			else:
				setattr(obj,item,attributes[item])
		return obj
	
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

def get_class(item):
	try:
		if item in _SAT_data.CLASSES:
			return _SAT_data.CLASSES[item]
		else:
			return _SAT_data.DEFAULT_CLASS

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

def instance_to_dict(obj):
	try:
		if isinstance(obj,_SAT_data.SAT_TYPE):
			dictionary = instance_to_dict(obj.__dict__)
		if type(obj) == dict:
			dictionary = {}
			for item in obj:
				dictionary.update({item:instance_to_dict(obj[item])})
		elif type(obj) == list:
			dictionary = []
			for i in obj:
				dictionary.append(instance_to_dict(i))
		elif type(obj) == unicode or type(obj) == int or type(obj) == str:
			dictionary = obj
		else:
			dictionary = instance_to_dict(obj.__dict__)
		return dictionary
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

def translate(dictionary,tr):
	try:
		new = {}
		for item in dictionary:
			if type(dictionary[item]) == dict:
				new[tr[item]] = translate(dictionary[item],tr)
			elif type(dictionary[item]) == list:
				new[tr[item]] = []
				for i in dictionary[item]:
					new[tr[item]].append(translate(i,tr))
			else:
				new[tr[item]] = dictionary[item]
		return new
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

def get_tag(obj,E):
	try:
		data = []
		dictionary = {}
		for item in obj:
			if type(obj[item]) == dict:
				data.append(E(item,*get_tag(obj[item],E))) 
			elif  type(obj[item]) == list:
				for i in obj[item]:
					data.append(E(item,*get_tag(i,E)))
			else: 
				dictionary[item] = obj[item]
			data.append(dictionary)
		return data
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

def get_tree(dictionary,E,NSMAP,XSD):
	try:
		schemaLocation_tag = {'{'+NSMAP['xsi']+'}schemaLocation' : XSD}
		tags = get_tag(dictionary,E)
		tree = [schemaLocation_tag] + tags
		return tree

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

# Only one namespace
def generate_simple_xml(dictionary,document_type):
	try:
		ROOT = _SAT_data.ROOT[document_type]
		NSMAP = _SAT_data.NSMAP[document_type]
		NAMESPACE = _SAT_data.NAMESPACE[document_type]
		XSD = _SAT_data.XSD[document_type]
		
		E = ElementMaker(namespace=NSMAP[NAMESPACE],
						nsmap=NSMAP)

		xml = E(ROOT,*get_tree(dictionary,E,NSMAP,XSD))
		return xml

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

def get_serial_number(cer_file):
	try:
		process = Popen(['openssl','x509','-inform','DER','-in',cer_file,'-serial','-noout'], stdout=PIPE, stderr=PIPE)
		error = process.stderr.read()
		process.stderr.close()
		serial_number_hex = process.stdout.read()
		process.stdout.close()

		if not error: 
			serial_number_hex = serial_number_hex[7:].strip()
			serial_number = ''
			for i in xrange(0,len(serial_number_hex),2):
				block = serial_number_hex[i:i+2]
				entero = int(block,16)
				serial_number = serial_number + chr(entero)
			return serial_number	
		else: 
		    return "Se produjo el siguiente error:\n%s" % error
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

def get_credentials(identifier,certificates):
	try:
		credentials_folder = _Constants.IDENTIFIER_PATH + identifier + '/' + _Constants.CREDENTIALS_FOLDER + '/'
		logger.info(certificates)
		credentials = {
			'pem_file' : credentials_folder + identifier + '_EAC.pem',
			'cer_file' : credentials_folder + certificates['cer_file'],
			'key_file' : credentials_folder + certificates['key_file'],
			'password' : certificates['password']
		}
		return credentials
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

def stamp_xml(identifier,document_type,xml_without_stamp,certificates):
	try:
		credentials = get_credentials(identifier,certificates)
		# if not os.path.isfile(credentials['pem_file']):
		# 	out = generate_pem_file(identifier,credentials)
		# 	logger.info(out)
		out = generate_pem_file(identifier,credentials)
		logger.info(out)
		
		serial_number = get_serial_number(credentials['cer_file'])
		keys = RSA.load_key(credentials['pem_file'])
		cert_file = open(credentials['cer_file'], 'r')
		cert = base64.b64encode(cert_file.read())
		xml = xml_without_stamp
		xsl_root = ET.parse(_SAT_data.XSLT[document_type])
		xsl = ET.XSLT(xsl_root)
		cadena_original = xsl(xml)
		digest = hashlib.new('sha1', str(cadena_original)).digest()
		sello = base64.b64encode(keys.sign(digest, "sha1"))

		xml.attrib['Sello'] = sello
		xml.attrib['Certificado'] = cert
		xml.attrib['noCertificado'] = serial_number

		xml_with_stamp = ET.tostring(xml,pretty_print=True,xml_declaration=True, encoding='UTF-8')
		logger.info(xml_with_stamp)

		return xml_with_stamp
	
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

def generate_pem_file(identifier,credentials):
	try:
		key_file = credentials['key_file']
		password = credentials['password']
		file_path = credentials['pem_file']
		params_process = ['openssl','pkcs8','-inform','DET','-in',key_file, '-passin', 'pass:'+password,'-out',file_path]
		return execute_popen_process(params_process)
	
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

def execute_popen_process(params):
	try:
		process = Popen(params,stdout=PIPE, stderr=PIPE)
		error = process.stderr.read()
		process.stderr.close()
		success = process.stdout.read()
		process.stdout.close()
		if not error:
			return success
		else:
			return error
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
