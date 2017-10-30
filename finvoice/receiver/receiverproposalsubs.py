#!/usr/bin/env python

#
# Generated  by generateDS.py.
# Python 3.5.2 (default, Sep 14 2017, 22:51:06)  [GCC 5.4.0 20160609]
#
# Command line options:
#   ('-s', 'finvoice/receiver/receiverproposalsubs.py')
#   ('-o', 'finvoice/receiver/receiverproposal.py')
#   ('--super', 'finvoice.receiver.receiverproposal')
#   ('--external-encoding', 'iso8859-15')
#   ('--no-dates', '')
#   ('--no-versions', '')
#
# Command line arguments:
#   xsd/ReceiverProposal.xsd
#
# Command line:
#   /home/aisopuro/.virtualenvs/py-finvoice/bin/generateDS.py -s "finvoice/receiver/receiverproposalsubs.py" -o "finvoice/receiver/receiverproposal.py" --super="finvoice.receiver.receiverproposal" --external-encoding="iso8859-15" --no-dates --no-versions xsd/ReceiverProposal.xsd
#
# Current working directory (os.getcwd()):
#   py-finvoice
#

import sys
from lxml import etree as etree_

import finvoice.receiver.receiverproposal as supermod

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


class ReceiverProposalSub(supermod.ReceiverProposal):
    def __init__(self, Version=None, MessageDetails=None, SellerPartyDetails=None, SellerOrganisationUnitNumber=None, InvoiceSenderInformationDetails=None, SellerInvoiceDetails=None, BuyerPartyDetails=None, InvoiceRecipientDetails=None, ConversionDetails=None, RPFreeText=None):
        super(ReceiverProposalSub, self).__init__(Version, MessageDetails, SellerPartyDetails, SellerOrganisationUnitNumber, InvoiceSenderInformationDetails, SellerInvoiceDetails, BuyerPartyDetails, InvoiceRecipientDetails, ConversionDetails, RPFreeText, )
supermod.ReceiverProposal.subclass = ReceiverProposalSub
# end class ReceiverProposalSub


class BuyerPartyDetailsTypeSub(supermod.BuyerPartyDetailsType):
    def __init__(self, BuyerPartyIdentifier=None, BuyerOrganisationName=None, BuyerPostalAddressDetails=None):
        super(BuyerPartyDetailsTypeSub, self).__init__(BuyerPartyIdentifier, BuyerOrganisationName, BuyerPostalAddressDetails, )
supermod.BuyerPartyDetailsType.subclass = BuyerPartyDetailsTypeSub
# end class BuyerPartyDetailsTypeSub


class BuyerPostalAddressDetailsTypeSub(supermod.BuyerPostalAddressDetailsType):
    def __init__(self, BuyerStreetName=None, BuyerTownName=None, BuyerPostCodeIdentifier=None, CountryCode=None, CountryName=None, BuyerPostOfficeBoxIdentifier=None):
        super(BuyerPostalAddressDetailsTypeSub, self).__init__(BuyerStreetName, BuyerTownName, BuyerPostCodeIdentifier, CountryCode, CountryName, BuyerPostOfficeBoxIdentifier, )
supermod.BuyerPostalAddressDetailsType.subclass = BuyerPostalAddressDetailsTypeSub
# end class BuyerPostalAddressDetailsTypeSub


class ConversionDetailsTypeSub(supermod.ConversionDetailsType):
    def __init__(self, ConversionID=None, DDArchiveCode=None, BuyerDDIdentifier=None, DDReferenceNumber=None, BuyerDDAccountId=None):
        super(ConversionDetailsTypeSub, self).__init__(ConversionID, DDArchiveCode, BuyerDDIdentifier, DDReferenceNumber, BuyerDDAccountId, )
supermod.ConversionDetailsType.subclass = ConversionDetailsTypeSub
# end class ConversionDetailsTypeSub


class InvoiceRecipientDetailsTypeSub(supermod.InvoiceRecipientDetailsType):
    def __init__(self, InvoiceRecipientAddress=None, InvoiceRecipientIntermediatorAddress=None, SellerInvoiceIdentifier=None):
        super(InvoiceRecipientDetailsTypeSub, self).__init__(InvoiceRecipientAddress, InvoiceRecipientIntermediatorAddress, SellerInvoiceIdentifier, )
supermod.InvoiceRecipientDetailsType.subclass = InvoiceRecipientDetailsTypeSub
# end class InvoiceRecipientDetailsTypeSub


class InvoiceSenderInformationDetailsTypeSub(supermod.InvoiceSenderInformationDetailsType):
    def __init__(self, SellerWebaddressNameText=None, SellerWebaddressText=None, InvoiceSenderAddress=None, InvoiceSenderIntermediatorAddress=None):
        super(InvoiceSenderInformationDetailsTypeSub, self).__init__(SellerWebaddressNameText, SellerWebaddressText, InvoiceSenderAddress, InvoiceSenderIntermediatorAddress, )
supermod.InvoiceSenderInformationDetailsType.subclass = InvoiceSenderInformationDetailsTypeSub
# end class InvoiceSenderInformationDetailsTypeSub


class MessageDetailsTypeSub(supermod.MessageDetailsType):
    def __init__(self, MessageTypeCode=None, MessageTypeText=None, MessageActionCode=None, MessageActionCodeIdentifier=None, MessageDate=None, SenderInfoIdentifier=None):
        super(MessageDetailsTypeSub, self).__init__(MessageTypeCode, MessageTypeText, MessageActionCode, MessageActionCodeIdentifier, MessageDate, SenderInfoIdentifier, )
supermod.MessageDetailsType.subclass = MessageDetailsTypeSub
# end class MessageDetailsTypeSub


class SellerInvoiceDetailsTypeSub(supermod.SellerInvoiceDetailsType):
    def __init__(self, SellerDirectDebitIdentifier=None, PaymentInstructionIdentifier=None, SellerInstructionFreeText=None, SellerInvoiceTypeDetails=None):
        super(SellerInvoiceDetailsTypeSub, self).__init__(SellerDirectDebitIdentifier, PaymentInstructionIdentifier, SellerInstructionFreeText, SellerInvoiceTypeDetails, )
supermod.SellerInvoiceDetailsType.subclass = SellerInvoiceDetailsTypeSub
# end class SellerInvoiceDetailsTypeSub


class SellerPartyDetailsTypeSub(supermod.SellerPartyDetailsType):
    def __init__(self, SellerPartyIdentifier=None, SellerOrganisationNames=None, SellerPostalAddressDetails=None):
        super(SellerPartyDetailsTypeSub, self).__init__(SellerPartyIdentifier, SellerOrganisationNames, SellerPostalAddressDetails, )
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


class SellerInvoiceIdentifierTypeSub(supermod.SellerInvoiceIdentifierType):
    def __init__(self, SellerInvoiceIdentifierType_member=None, valueOf_=None):
        super(SellerInvoiceIdentifierTypeSub, self).__init__(SellerInvoiceIdentifierType_member, valueOf_, )
supermod.SellerInvoiceIdentifierType.subclass = SellerInvoiceIdentifierTypeSub
# end class SellerInvoiceIdentifierTypeSub


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


class SellerInvoiceIdentifierTextType1Sub(supermod.SellerInvoiceIdentifierTextType1):
    def __init__(self, LanguageCode=None, SellerInvoiceIdentifierType=None, SellerInvoiceIdentifierMinLength=1, SellerInvoiceIdentifierMaxLength=35, SellerInvoiceIdentifierSpaces=False, SellerInvoiceIdentifierHyphens=False, valueOf_=None):
        super(SellerInvoiceIdentifierTextType1Sub, self).__init__(LanguageCode, SellerInvoiceIdentifierType, SellerInvoiceIdentifierMinLength, SellerInvoiceIdentifierMaxLength, SellerInvoiceIdentifierSpaces, SellerInvoiceIdentifierHyphens, valueOf_, )
supermod.SellerInvoiceIdentifierTextType1.subclass = SellerInvoiceIdentifierTextType1Sub
# end class SellerInvoiceIdentifierTextType1Sub


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
        rootTag = 'ReceiverProposal'
        rootClass = supermod.ReceiverProposal
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
        rootTag = 'ReceiverProposal'
        rootClass = supermod.ReceiverProposal
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
        rootTag = 'ReceiverProposal'
        rootClass = supermod.ReceiverProposal
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
        rootTag = 'ReceiverProposal'
        rootClass = supermod.ReceiverProposal
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from finvoice.receiver.receiverproposal import *\n\n')
        sys.stdout.write('import finvoice.receiver.receiverproposal as model_\n\n')
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
