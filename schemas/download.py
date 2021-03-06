
from __future__ import print_function

# https://opcfoundation.org/UA/schemas/OPC%20UA%20Schema%20Files%20Readme.xls

resources = [
  'https://opcfoundation.org/UA/schemas/1.02/Opc.Ua.Types.xsd',
  'https://opcfoundation.org/UA/schemas/1.02/Opc.Ua.Services.wsdl',
  'https://opcfoundation.org/UA/schemas/1.02/Opc.Ua.Endpoints.wsdl',
  'https://opcfoundation.org/UA/schemas/DI/1.00/Opc.Ua.Di.Types.xsd',
  'https://opcfoundation.org/UA/schemas/ADI/1.00/Opc.Ua.Adi.Types.xsd',

  'https://opcfoundation.org/UA/schemas/1.02/SecuredApplication.xsd',

  'https://opcfoundation.org/UA/schemas/1.02/UANodeSet.xsd',
  'https://opcfoundation.org/UA/schemas/1.02/UAVariant.xsd', # gone
  'https://opcfoundation.org/UA/schemas/1.02/Opc.Ua.NodeSet2.xml',
  'https://opcfoundation.org/UA/schemas/1.02/Opc.Ua.NodeSet2.Part3.xml',
  'https://opcfoundation.org/UA/schemas/1.02/Opc.Ua.NodeSet2.Part4.xml',
  'https://opcfoundation.org/UA/schemas/1.02/Opc.Ua.NodeSet2.Part5.xml',
  'https://opcfoundation.org/UA/schemas/Opc.Ua.NodeSet2.Part8.xml',
  'https://opcfoundation.org/UA/schemas/1.02/Opc.Ua.NodeSet2.Part9.xml',
  'https://opcfoundation.org/UA/schemas/1.02/Opc.Ua.NodeSet2.Part10.xml',
  'https://opcfoundation.org/UA/schemas/1.02/Opc.Ua.NodeSet2.Part11.xml',
  'https://opcfoundation.org/UA/schemas/1.02/Opc.Ua.NodeSet2.Part13.xml',
  'https://opcfoundation.org/UA/schemas/DI/1.00/Opc.Ua.Di.NodeSet2.xml',
  'https://opcfoundation.org/UA/schemas/ADI/1.00/Opc.Ua.Adi.NodeSet2.xml',

  'https://opcfoundation.org/UA/schemas/1.02/OPCBinarySchema.xsd',
  'https://opcfoundation.org/UA/schemas/1.02/Opc.Ua.Types.bsd',
  'https://opcfoundation.org/UA/schemas/DI/1.00/Opc.Ua.Di.Types.bsd',
  'https://opcfoundation.org/UA/schemas/ADI/1.00/Opc.Ua.Adi.Types.bsd',

  'https://opcfoundation.org/UA/schemas/1.02/AttributeIds.csv',
  'https://opcfoundation.org/UA/schemas/1.02/StatusCode.csv',
  'https://opcfoundation.org/UA/schemas/1.02/NodeIds.csv',
]

import os

try:
  from urllib.request import urlopen
  from urllib.request import build_opener
  from urllib.parse import urlparse
except ImportError:
  from urllib import urlopen
  from urllib2 import build_opener
  from urlparse import urlparse

opener = build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

for url in resources:
  fname = os.path.basename(url)
  print('downloading',fname,'... ',end='')
  try:
    open(fname,'wb+').write(opener.open(url).read())
    print('OK')
  except Exception as e:
    print('FAILED ({0})'.format(e))

