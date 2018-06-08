#!/usr/bin/env python

#
# Generated  by generateDS.py.
# Python 3.5.2 (default, Sep 14 2017, 22:51:06)  [GCC 5.4.0 20160609]
#
# Command line options:
#   ('-s', 'finvoice/sender/senderinfosubs.py')
#   ('-o', 'finvoice/sender/senderinfo.py')
#   ('--super', 'finvoice.sender.senderinfo')
#   ('--external-encoding', 'iso8859-15')
#   ('--no-dates', '')
#   ('--no-versions', '')
#   ('--validator-bodies', 'stubs/validator/sender/senderinfo/')
#   ('--user-methods', 'generators.gends_user_methods_senderinfo')
#
# Command line arguments:
#   xsd/FinvoiceSenderInfo.xsd
#
# Command line:
#   /home/aisopuro/.virtualenvs/py-finvoice/bin/generateDS.py -s "finvoice/sender/senderinfosubs.py" -o "finvoice/sender/senderinfo.py" --super="finvoice.sender.senderinfo" --external-encoding="iso8859-15" --no-dates --no-versions --validator-bodies="stubs/validator/sender/senderinfo/" --user-methods="generators.gends_user_methods_senderinfo" xsd/FinvoiceSenderInfo.xsd
#
# Current working directory (os.getcwd()):
#   py-finvoice
#

import sys
from lxml import etree as etree_

import finvoice.sender.senderinfo as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'iso8859-15'

#
# Data representation classes
#


class FinvoiceSenderInfoSub(supermod.FinvoiceSenderInfo):
    def __init__(self, Version=None, MessageDetails=None, SellerPartyDetails=None, SellerOrganisationUnitNumber=None, InvoiceSenderInformationDetails=None, SellerAccountDetails=None, SellerInvoiceDetails=None, ProposedDueDateAccepted=None, ProposedInvoicePeriodAccepted=None):
        super(FinvoiceSenderInfoSub, self).__init__(Version, MessageDetails, SellerPartyDetails, SellerOrganisationUnitNumber, InvoiceSenderInformationDetails, SellerAccountDetails, SellerInvoiceDetails, ProposedDueDateAccepted, ProposedInvoicePeriodAccepted, )
supermod.FinvoiceSenderInfo.subclass = FinvoiceSenderInfoSub
# end class FinvoiceSenderInfoSub


class InvoiceSenderInformationDetailsTypeSub(supermod.InvoiceSenderInformationDetailsType):
    def __init__(self, SellerWebaddressNameText=None, SellerWebaddressText=None, InvoiceSenderAddress=None, InvoiceSenderIntermediatorAddress=None, NewInvoiceSenderAddress=None, NewInvoiceSenderIntermediatorAddress=None):
        super(InvoiceSenderInformationDetailsTypeSub, self).__init__(SellerWebaddressNameText, SellerWebaddressText, InvoiceSenderAddress, InvoiceSenderIntermediatorAddress, NewInvoiceSenderAddress, NewInvoiceSenderIntermediatorAddress, )
supermod.InvoiceSenderInformationDetailsType.subclass = InvoiceSenderInformationDetailsTypeSub
# end class InvoiceSenderInformationDetailsTypeSub


class MessageDetailsTypeSub(supermod.MessageDetailsType):
    def __init__(self, MessageTypeCode=None, MessageTypeText=None, MessageActionCode=None, MessageActionCodeIdentifier=None, MessageDate=None, SenderInfoIdentifier=None):
        super(MessageDetailsTypeSub, self).__init__(MessageTypeCode, MessageTypeText, MessageActionCode, MessageActionCodeIdentifier, MessageDate, SenderInfoIdentifier, )
supermod.MessageDetailsType.subclass = MessageDetailsTypeSub
# end class MessageDetailsTypeSub


class SellerAccountDetailsTypeSub(supermod.SellerAccountDetailsType):
    def __init__(self, SellerAccountID=None, SellerBic=None, NewSellerAccountID=None, NewSellerBic=None):
        super(SellerAccountDetailsTypeSub, self).__init__(SellerAccountID, SellerBic, NewSellerAccountID, NewSellerBic, )
supermod.SellerAccountDetailsType.subclass = SellerAccountDetailsTypeSub
# end class SellerAccountDetailsTypeSub


class SellerAccountIDTypeSub(supermod.SellerAccountIDType):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None, extensiontype_=None):
        super(SellerAccountIDTypeSub, self).__init__(IdentificationSchemeName, valueOf_, extensiontype_, )
supermod.SellerAccountIDType.subclass = SellerAccountIDTypeSub
# end class SellerAccountIDTypeSub


class SellerBicTypeSub(supermod.SellerBicType):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None, extensiontype_=None):
        super(SellerBicTypeSub, self).__init__(IdentificationSchemeName, valueOf_, extensiontype_, )
supermod.SellerBicType.subclass = SellerBicTypeSub
# end class SellerBicTypeSub


class SellerInvoiceDetailsTypeSub(supermod.SellerInvoiceDetailsType):
    def __init__(self, SellerDirectDebitIdentifier=None, PaymentInstructionIdentifier=None, SellerInstructionFreeText=None, SellerInvoiceTypeDetails=None, SellerServiceCode=None):
        super(SellerInvoiceDetailsTypeSub, self).__init__(SellerDirectDebitIdentifier, PaymentInstructionIdentifier, SellerInstructionFreeText, SellerInvoiceTypeDetails, SellerServiceCode, )
supermod.SellerInvoiceDetailsType.subclass = SellerInvoiceDetailsTypeSub
# end class SellerInvoiceDetailsTypeSub


class SellerPartyDetailsTypeSub(supermod.SellerPartyDetailsType):
    def __init__(self, SellerPartyIdentifier=None, SellerOrganisationNames=None, SellerOrganisationBankName=None, SellerPostalAddressDetails=None, IndustryCode=None):
        super(SellerPartyDetailsTypeSub, self).__init__(SellerPartyIdentifier, SellerOrganisationNames, SellerOrganisationBankName, SellerPostalAddressDetails, IndustryCode, )
supermod.SellerPartyDetailsType.subclass = SellerPartyDetailsTypeSub
# end class SellerPartyDetailsTypeSub


class SellerOrganisationNamesTypeSub(supermod.SellerOrganisationNamesType):
    def __init__(self, LanguageCode=None, SellerOrganisationName=None):
        super(SellerOrganisationNamesTypeSub, self).__init__(LanguageCode, SellerOrganisationName, )
supermod.SellerOrganisationNamesType.subclass = SellerOrganisationNamesTypeSub
# end class SellerOrganisationNamesTypeSub


class SellerPostalAddressDetailsTypeSub(supermod.SellerPostalAddressDetailsType):
    def __init__(self, SellerStreetName=None, SellerTownName=None, SellerPostCodeIdentifier=None, CountryCode=None, CountryName=None, SellerPostOfficeBoxIdentifier=None):
        super(SellerPostalAddressDetailsTypeSub, self).__init__(SellerStreetName, SellerTownName, SellerPostCodeIdentifier, CountryCode, CountryName, SellerPostOfficeBoxIdentifier, )
supermod.SellerPostalAddressDetailsType.subclass = SellerPostalAddressDetailsTypeSub
# end class SellerPostalAddressDetailsTypeSub


class dateSub(supermod.date):
    def __init__(self, Format=None, valueOf_=None):
        super(dateSub, self).__init__(Format, valueOf_, )
supermod.date.subclass = dateSub
# end class dateSub


class TextLanguageOptionalSub(supermod.TextLanguageOptional):
    def __init__(self, LanguageCode=None, valueOf_=None, extensiontype_=None):
        super(TextLanguageOptionalSub, self).__init__(LanguageCode, valueOf_, extensiontype_, )
supermod.TextLanguageOptional.subclass = TextLanguageOptionalSub
# end class TextLanguageOptionalSub


class TextLanguageRequiredSub(supermod.TextLanguageRequired):
    def __init__(self, LanguageCode=None, valueOf_=None, extensiontype_=None):
        super(TextLanguageRequiredSub, self).__init__(LanguageCode, valueOf_, extensiontype_, )
supermod.TextLanguageRequired.subclass = TextLanguageRequiredSub
# end class TextLanguageRequiredSub


class SellerAccountIDType1Sub(supermod.SellerAccountIDType1):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None):
        super(SellerAccountIDType1Sub, self).__init__(IdentificationSchemeName, valueOf_, )
supermod.SellerAccountIDType1.subclass = SellerAccountIDType1Sub
# end class SellerAccountIDType1Sub


class SellerBicType2Sub(supermod.SellerBicType2):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None):
        super(SellerBicType2Sub, self).__init__(IdentificationSchemeName, valueOf_, )
supermod.SellerBicType2.subclass = SellerBicType2Sub
# end class SellerBicType2Sub


class NewSellerAccountIDTypeSub(supermod.NewSellerAccountIDType):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None):
        super(NewSellerAccountIDTypeSub, self).__init__(IdentificationSchemeName, valueOf_, )
supermod.NewSellerAccountIDType.subclass = NewSellerAccountIDTypeSub
# end class NewSellerAccountIDTypeSub


class NewSellerBicTypeSub(supermod.NewSellerBicType):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None):
        super(NewSellerBicTypeSub, self).__init__(IdentificationSchemeName, valueOf_, )
supermod.NewSellerBicType.subclass = NewSellerBicTypeSub
# end class NewSellerBicTypeSub


class SellerInstructionFreeTextTypeSub(supermod.SellerInstructionFreeTextType):
    def __init__(self, LanguageCode=None, valueOf_=None):
        super(SellerInstructionFreeTextTypeSub, self).__init__(LanguageCode, valueOf_, )
supermod.SellerInstructionFreeTextType.subclass = SellerInstructionFreeTextTypeSub
# end class SellerInstructionFreeTextTypeSub


class SellerInvoiceTypeDetailsTypeSub(supermod.SellerInvoiceTypeDetailsType):
    def __init__(self, SellerInvoiceTypeText=None, SellerInvoiceIdentifierText=None):
        super(SellerInvoiceTypeDetailsTypeSub, self).__init__(SellerInvoiceTypeText, SellerInvoiceIdentifierText, )
supermod.SellerInvoiceTypeDetailsType.subclass = SellerInvoiceTypeDetailsTypeSub
# end class SellerInvoiceTypeDetailsTypeSub


class SellerInvoiceTypeTextTypeSub(supermod.SellerInvoiceTypeTextType):
    def __init__(self, LanguageCode=None, valueOf_=None):
        super(SellerInvoiceTypeTextTypeSub, self).__init__(LanguageCode, valueOf_, )
supermod.SellerInvoiceTypeTextType.subclass = SellerInvoiceTypeTextTypeSub
# end class SellerInvoiceTypeTextTypeSub


class SellerInvoiceIdentifierTextTypeSub(supermod.SellerInvoiceIdentifierTextType):
    def __init__(self, LanguageCode=None, SellerInvoiceIdentifierType=None, SellerInvoiceIdentifierMinLength=1, SellerInvoiceIdentifierMaxLength=35, SellerInvoiceIdentifierSpaces=False, SellerInvoiceIdentifierHyphens=False, valueOf_=None, extensiontype_=None):
        super(SellerInvoiceIdentifierTextTypeSub, self).__init__(LanguageCode, SellerInvoiceIdentifierType, SellerInvoiceIdentifierMinLength, SellerInvoiceIdentifierMaxLength, SellerInvoiceIdentifierSpaces, SellerInvoiceIdentifierHyphens, valueOf_, extensiontype_, )
supermod.SellerInvoiceIdentifierTextType.subclass = SellerInvoiceIdentifierTextTypeSub
# end class SellerInvoiceIdentifierTextTypeSub


class SellerInvoiceIdentifierTextType3Sub(supermod.SellerInvoiceIdentifierTextType3):
    def __init__(self, LanguageCode=None, SellerInvoiceIdentifierType=None, SellerInvoiceIdentifierMinLength=1, SellerInvoiceIdentifierMaxLength=35, SellerInvoiceIdentifierSpaces=False, SellerInvoiceIdentifierHyphens=False, valueOf_=None):
        super(SellerInvoiceIdentifierTextType3Sub, self).__init__(LanguageCode, SellerInvoiceIdentifierType, SellerInvoiceIdentifierMinLength, SellerInvoiceIdentifierMaxLength, SellerInvoiceIdentifierSpaces, SellerInvoiceIdentifierHyphens, valueOf_, )
supermod.SellerInvoiceIdentifierTextType3.subclass = SellerInvoiceIdentifierTextType3Sub
# end class SellerInvoiceIdentifierTextType3Sub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'FinvoiceSenderInfo'
        rootClass = supermod.FinvoiceSenderInfo
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'FinvoiceSenderInfo'
        rootClass = supermod.FinvoiceSenderInfo
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'FinvoiceSenderInfo'
        rootClass = supermod.FinvoiceSenderInfo
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'FinvoiceSenderInfo'
        rootClass = supermod.FinvoiceSenderInfo
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from finvoice.sender.senderinfo import *\n\n')
        sys.stdout.write('import finvoice.sender.senderinfo as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
