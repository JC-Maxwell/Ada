# -*- coding: utf-8 -*-

# ███████╗ █████╗ ████████╗    ███████╗██╗██╗     ███████╗
# ██╔════╝██╔══██╗╚══██╔══╝    ██╔════╝██║██║     ██╔════╝
# ███████╗███████║   ██║       █████╗  ██║██║     █████╗  
# ╚════██║██╔══██║   ██║       ██╔══╝  ██║██║     ██╔══╝  
# ███████║██║  ██║   ██║       ██║     ██║███████╗███████╗
# ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝╚══════╝╚══════╝
                                                                   
# DESCRIPTION
# Contains classes that manage a Pauli's project responses.





# ======================================================== DEPENDENCIES

# Native:
import logging

# External:
from flask import json
from flask import make_response
from flask import abort

# SDK:
from pauli_sdk.Modules import constants as _Pauli_Constants

# Development:
from Modules.General import constants as _Constants
from Modules.General import helper as _Helper
from Modules.SAT import sat_data as _SAT_data


# ======================================================== MODULE CODE

logger = logging.getLogger('root')


# SAT_DOCUMENT CLASS
class Sat_document(object):
	def __init__(self, obj):
		del obj['certificates']
		self = _Helper.assign_attributes(self,obj)
	def to_dict(self):
		return _Helper.instance_to_dict(self)
	def translate(self):
		return _Helper.translate(self.to_dict(),_SAT_data.DOCUMENT_TRANSLATE[type(self).__name__])

# CHART_OF_ACCOUNTS CLASS
class Chart_of_Accounts(Sat_document):
	def __init__(self, obj):
		obj['version'] = "1.1"
		Sat_document.__init__(self,obj)
	def get_xml(self,certificates):
		document_type = type(self).__name__
		xml_without_stamp = _Helper.generate_simple_xml(self.translate(),document_type)
		xml_with_stamp = _Helper.stamp_xml(self.identifier,document_type,xml_without_stamp,certificates)
		return xml_with_stamp

# CFDI CLASS
class CFDI(Sat_document):
	def __init__(self, obj):
		obj['version'] = "3.2"
		Sat_document.__init__(self,obj)
	def get_xml(self,certificates):
		document_type = type(self).__name__
		xml_without_stamp = _Helper.generate_simple_xml(self.translate(),document_type)
		xml_with_stamp = _Helper.stamp_xml(self.seller.identifier,document_type,xml_without_stamp,certificates)
		return xml_with_stamp

# CHART_OF_ACCOUNTS CLASS
class Trial_Balance(Sat_document):
	def __init__(self, obj):
		obj['version'] = "1.1"
		Sat_document.__init__(self,obj)
	def get_xml(self,certificates):
		document_type = type(self).__name__
		xml_without_stamp = _Helper.generate_simple_xml(self.translate(),document_type)
		xml_with_stamp = _Helper.stamp_xml(self.identifier,document_type,xml_without_stamp,certificates)
		return xml_with_stamp
