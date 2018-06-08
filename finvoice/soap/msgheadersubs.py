#!/usr/bin/env python

#
# Generated  by generateDS.py.
# Python 3.5.2 (default, Sep 14 2017, 22:51:06)  [GCC 5.4.0 20160609]
#
# Command line options:
#   ('-f', '')
#   ('-s', 'finvoice/soap/msgheadersubs.py')
#   ('-o', 'finvoice/soap/msgheader.py')
#   ('--super', 'finvoice.soap.msgheader')
#   ('--external-encoding', 'iso8859-15')
#   ('--no-dates', '')
#   ('--no-versions', '')
#
# Command line arguments:
#   xsd/msg-header-2_0.xsd
#
# Command line:
#   /home/aisopuro/.virtualenvs/py-finvoice/bin/generateDS.py -f -s "finvoice/soap/msgheadersubs.py" -o "finvoice/soap/msgheader.py" --super="finvoice.soap.msgheader" --external-encoding="iso8859-15" --no-dates --no-versions xsd/msg-header-2_0.xsd
#
# Current working directory (os.getcwd()):
#   py-finvoice
#

import sys
from lxml import etree as etree_

import finvoice.soap.msgheader as supermod

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


class SchemaSub(supermod.Schema):
    def __init__(self, location=None, version=None):
        super(SchemaSub, self).__init__(location, version, )
supermod.Schema.subclass = SchemaSub
# end class SchemaSub


class MessageHeaderSub(supermod.MessageHeader):
    def __init__(self, id=None, version=None, mustUnderstand=None, From=None, To=None, CPAId=None, ConversationId=None, Service=None, Action=None, MessageData=None, DuplicateElimination=None, Description=None, anytypeobjs_=None):
        super(MessageHeaderSub, self).__init__(id, version, mustUnderstand, From, To, CPAId, ConversationId, Service, Action, MessageData, DuplicateElimination, Description, anytypeobjs_, )
supermod.MessageHeader.subclass = MessageHeaderSub
# end class MessageHeaderSub


class ServiceSub(supermod.Service):
    def __init__(self, type_=None, valueOf_=None):
        super(ServiceSub, self).__init__(type_, valueOf_, )
supermod.Service.subclass = ServiceSub
# end class ServiceSub


class MessageDataSub(supermod.MessageData):
    def __init__(self, MessageId=None, Timestamp=None, RefToMessageId=None, TimeToLive=None):
        super(MessageDataSub, self).__init__(MessageId, Timestamp, RefToMessageId, TimeToLive, )
supermod.MessageData.subclass = MessageDataSub
# end class MessageDataSub


class DuplicateEliminationSub(supermod.DuplicateElimination):
    def __init__(self):
        super(DuplicateEliminationSub, self).__init__()
supermod.DuplicateElimination.subclass = DuplicateEliminationSub
# end class DuplicateEliminationSub


class SyncReplySub(supermod.SyncReply):
    def __init__(self, actor=None, id=None, version=None, mustUnderstand=None, anytypeobjs_=None):
        super(SyncReplySub, self).__init__(actor, id, version, mustUnderstand, anytypeobjs_, )
supermod.SyncReply.subclass = SyncReplySub
# end class SyncReplySub


class MessageOrderSub(supermod.MessageOrder):
    def __init__(self, id=None, version=None, mustUnderstand=None, SequenceNumber=None, anytypeobjs_=None):
        super(MessageOrderSub, self).__init__(id, version, mustUnderstand, SequenceNumber, anytypeobjs_, )
supermod.MessageOrder.subclass = MessageOrderSub
# end class MessageOrderSub


class AckRequestedSub(supermod.AckRequested):
    def __init__(self, actor=None, signed=None, id=None, version=None, mustUnderstand=None, anytypeobjs_=None):
        super(AckRequestedSub, self).__init__(actor, signed, id, version, mustUnderstand, anytypeobjs_, )
supermod.AckRequested.subclass = AckRequestedSub
# end class AckRequestedSub


class AcknowledgmentSub(supermod.Acknowledgment):
    def __init__(self, actor=None, id=None, version=None, mustUnderstand=None, Timestamp=None, RefToMessageId=None, From=None, Reference=None, anytypeobjs_=None):
        super(AcknowledgmentSub, self).__init__(actor, id, version, mustUnderstand, Timestamp, RefToMessageId, From, Reference, anytypeobjs_, )
supermod.Acknowledgment.subclass = AcknowledgmentSub
# end class AcknowledgmentSub


class ErrorListSub(supermod.ErrorList):
    def __init__(self, highestSeverity=None, id=None, version=None, mustUnderstand=None, Error=None, anytypeobjs_=None):
        super(ErrorListSub, self).__init__(highestSeverity, id, version, mustUnderstand, Error, anytypeobjs_, )
supermod.ErrorList.subclass = ErrorListSub
# end class ErrorListSub


class ErrorSub(supermod.Error):
    def __init__(self, id=None, codeContext='urn:oasis:names:tc:ebxml-msg:service:errors', errorCode=None, severity=None, location=None, Description=None, anytypeobjs_=None):
        super(ErrorSub, self).__init__(id, codeContext, errorCode, severity, location, Description, anytypeobjs_, )
supermod.Error.subclass = ErrorSub
# end class ErrorSub


class StatusResponseSub(supermod.StatusResponse):
    def __init__(self, messageStatus=None, id=None, version=None, RefToMessageId=None, Timestamp=None, anytypeobjs_=None):
        super(StatusResponseSub, self).__init__(messageStatus, id, version, RefToMessageId, Timestamp, anytypeobjs_, )
supermod.StatusResponse.subclass = StatusResponseSub
# end class StatusResponseSub


class StatusRequestSub(supermod.StatusRequest):
    def __init__(self, id=None, version=None, RefToMessageId=None, anytypeobjs_=None):
        super(StatusRequestSub, self).__init__(id, version, RefToMessageId, anytypeobjs_, )
supermod.StatusRequest.subclass = StatusRequestSub
# end class StatusRequestSub


class sequenceNumber_typeSub(supermod.sequenceNumber_type):
    def __init__(self, status='Continue', valueOf_=None):
        super(sequenceNumber_typeSub, self).__init__(status, valueOf_, )
supermod.sequenceNumber_type.subclass = sequenceNumber_typeSub
# end class sequenceNumber_typeSub


class PartyIdSub(supermod.PartyId):
    def __init__(self, type_=None, valueOf_=None):
        super(PartyIdSub, self).__init__(type_, valueOf_, )
supermod.PartyId.subclass = PartyIdSub
# end class PartyIdSub


class ToSub(supermod.To):
    def __init__(self, PartyId=None, Role=None):
        super(ToSub, self).__init__(PartyId, Role, )
supermod.To.subclass = ToSub
# end class ToSub


class FromSub(supermod.From):
    def __init__(self, PartyId=None, Role=None):
        super(FromSub, self).__init__(PartyId, Role, )
supermod.From.subclass = FromSub
# end class FromSub


class DescriptionSub(supermod.Description):
    def __init__(self, lang=None, valueOf_=None):
        super(DescriptionSub, self).__init__(lang, valueOf_, )
supermod.Description.subclass = DescriptionSub
# end class DescriptionSub


class SignatureTypeSub(supermod.SignatureType):
    def __init__(self, Id=None, SignedInfo=None, SignatureValue=None, KeyInfo=None, Object=None):
        super(SignatureTypeSub, self).__init__(Id, SignedInfo, SignatureValue, KeyInfo, Object, )
supermod.SignatureType.subclass = SignatureTypeSub
# end class SignatureTypeSub


class SignatureValueTypeSub(supermod.SignatureValueType):
    def __init__(self, Id=None, valueOf_=None):
        super(SignatureValueTypeSub, self).__init__(Id, valueOf_, )
supermod.SignatureValueType.subclass = SignatureValueTypeSub
# end class SignatureValueTypeSub


class SignedInfoTypeSub(supermod.SignedInfoType):
    def __init__(self, Id=None, CanonicalizationMethod=None, SignatureMethod=None, Reference=None):
        super(SignedInfoTypeSub, self).__init__(Id, CanonicalizationMethod, SignatureMethod, Reference, )
supermod.SignedInfoType.subclass = SignedInfoTypeSub
# end class SignedInfoTypeSub


class CanonicalizationMethodTypeSub(supermod.CanonicalizationMethodType):
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(CanonicalizationMethodTypeSub, self).__init__(Algorithm, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.CanonicalizationMethodType.subclass = CanonicalizationMethodTypeSub
# end class CanonicalizationMethodTypeSub


class SignatureMethodTypeSub(supermod.SignatureMethodType):
    def __init__(self, Algorithm=None, HMACOutputLength=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(SignatureMethodTypeSub, self).__init__(Algorithm, HMACOutputLength, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.SignatureMethodType.subclass = SignatureMethodTypeSub
# end class SignatureMethodTypeSub


class ReferenceTypeSub(supermod.ReferenceType):
    def __init__(self, Id=None, URI=None, Type=None, Transforms=None, DigestMethod=None, DigestValue=None):
        super(ReferenceTypeSub, self).__init__(Id, URI, Type, Transforms, DigestMethod, DigestValue, )
supermod.ReferenceType.subclass = ReferenceTypeSub
# end class ReferenceTypeSub


class TransformsTypeSub(supermod.TransformsType):
    def __init__(self, Transform=None):
        super(TransformsTypeSub, self).__init__(Transform, )
supermod.TransformsType.subclass = TransformsTypeSub
# end class TransformsTypeSub


class TransformTypeSub(supermod.TransformType):
    def __init__(self, Algorithm=None, anytypeobjs_=None, XPath=None, valueOf_=None, mixedclass_=None, content_=None):
        super(TransformTypeSub, self).__init__(Algorithm, anytypeobjs_, XPath, valueOf_, mixedclass_, content_, )
supermod.TransformType.subclass = TransformTypeSub
# end class TransformTypeSub


class DigestMethodTypeSub(supermod.DigestMethodType):
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(DigestMethodTypeSub, self).__init__(Algorithm, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.DigestMethodType.subclass = DigestMethodTypeSub
# end class DigestMethodTypeSub


class KeyInfoTypeSub(supermod.KeyInfoType):
    def __init__(self, Id=None, KeyName=None, KeyValue=None, RetrievalMethod=None, X509Data=None, PGPData=None, SPKIData=None, MgmtData=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(KeyInfoTypeSub, self).__init__(Id, KeyName, KeyValue, RetrievalMethod, X509Data, PGPData, SPKIData, MgmtData, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.KeyInfoType.subclass = KeyInfoTypeSub
# end class KeyInfoTypeSub


class KeyValueTypeSub(supermod.KeyValueType):
    def __init__(self, DSAKeyValue=None, RSAKeyValue=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(KeyValueTypeSub, self).__init__(DSAKeyValue, RSAKeyValue, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.KeyValueType.subclass = KeyValueTypeSub
# end class KeyValueTypeSub


class RetrievalMethodTypeSub(supermod.RetrievalMethodType):
    def __init__(self, URI=None, Type=None, Transforms=None):
        super(RetrievalMethodTypeSub, self).__init__(URI, Type, Transforms, )
supermod.RetrievalMethodType.subclass = RetrievalMethodTypeSub
# end class RetrievalMethodTypeSub


class X509DataTypeSub(supermod.X509DataType):
    def __init__(self, X509IssuerSerial=None, X509SKI=None, X509SubjectName=None, X509Certificate=None, X509CRL=None, anytypeobjs_=None):
        super(X509DataTypeSub, self).__init__(X509IssuerSerial, X509SKI, X509SubjectName, X509Certificate, X509CRL, anytypeobjs_, )
supermod.X509DataType.subclass = X509DataTypeSub
# end class X509DataTypeSub


class X509IssuerSerialTypeSub(supermod.X509IssuerSerialType):
    def __init__(self, X509IssuerName=None, X509SerialNumber=None):
        super(X509IssuerSerialTypeSub, self).__init__(X509IssuerName, X509SerialNumber, )
supermod.X509IssuerSerialType.subclass = X509IssuerSerialTypeSub
# end class X509IssuerSerialTypeSub


class PGPDataTypeSub(supermod.PGPDataType):
    def __init__(self, PGPKeyID=None, PGPKeyPacket=None, anytypeobjs_=None):
        super(PGPDataTypeSub, self).__init__(PGPKeyID, PGPKeyPacket, anytypeobjs_, )
supermod.PGPDataType.subclass = PGPDataTypeSub
# end class PGPDataTypeSub


class SPKIDataTypeSub(supermod.SPKIDataType):
    def __init__(self, SPKISexp=None, anytypeobjs_=None):
        super(SPKIDataTypeSub, self).__init__(SPKISexp, anytypeobjs_, )
supermod.SPKIDataType.subclass = SPKIDataTypeSub
# end class SPKIDataTypeSub


class ObjectTypeSub(supermod.ObjectType):
    def __init__(self, Id=None, MimeType=None, Encoding=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(ObjectTypeSub, self).__init__(Id, MimeType, Encoding, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.ObjectType.subclass = ObjectTypeSub
# end class ObjectTypeSub


class ManifestTypeSub(supermod.ManifestType):
    def __init__(self, Id=None, Reference=None):
        super(ManifestTypeSub, self).__init__(Id, Reference, )
supermod.ManifestType.subclass = ManifestTypeSub
# end class ManifestTypeSub


class SignaturePropertiesTypeSub(supermod.SignaturePropertiesType):
    def __init__(self, Id=None, SignatureProperty=None):
        super(SignaturePropertiesTypeSub, self).__init__(Id, SignatureProperty, )
supermod.SignaturePropertiesType.subclass = SignaturePropertiesTypeSub
# end class SignaturePropertiesTypeSub


class SignaturePropertyTypeSub(supermod.SignaturePropertyType):
    def __init__(self, Target=None, Id=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(SignaturePropertyTypeSub, self).__init__(Target, Id, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.SignaturePropertyType.subclass = SignaturePropertyTypeSub
# end class SignaturePropertyTypeSub


class DSAKeyValueTypeSub(supermod.DSAKeyValueType):
    def __init__(self, P=None, Q=None, G=None, Y=None, J=None, Seed=None, PgenCounter=None):
        super(DSAKeyValueTypeSub, self).__init__(P, Q, G, Y, J, Seed, PgenCounter, )
supermod.DSAKeyValueType.subclass = DSAKeyValueTypeSub
# end class DSAKeyValueTypeSub


class RSAKeyValueTypeSub(supermod.RSAKeyValueType):
    def __init__(self, Modulus=None, Exponent=None):
        super(RSAKeyValueTypeSub, self).__init__(Modulus, Exponent, )
supermod.RSAKeyValueType.subclass = RSAKeyValueTypeSub
# end class RSAKeyValueTypeSub


class rootSub(supermod.root):
    def __init__(self):
        super(rootSub, self).__init__()
supermod.root.subclass = rootSub
# end class rootSub


class EnvelopeSub(supermod.Envelope):
    def __init__(self, Header=None, Body=None, anytypeobjs_=None):
        super(EnvelopeSub, self).__init__(Header, Body, anytypeobjs_, )
supermod.Envelope.subclass = EnvelopeSub
# end class EnvelopeSub


class HeaderSub(supermod.Header):
    def __init__(self, anytypeobjs_=None):
        super(HeaderSub, self).__init__(anytypeobjs_, )
supermod.Header.subclass = HeaderSub
# end class HeaderSub


class BodySub(supermod.Body):
    def __init__(self, anytypeobjs_=None):
        super(BodySub, self).__init__(anytypeobjs_, )
supermod.Body.subclass = BodySub
# end class BodySub


class FaultSub(supermod.Fault):
    def __init__(self, faultcode=None, faultstring=None, faultactor=None, detail=None):
        super(FaultSub, self).__init__(faultcode, faultstring, faultactor, detail, )
supermod.Fault.subclass = FaultSub
# end class FaultSub


class detailSub(supermod.detail):
    def __init__(self, anytypeobjs_=None):
        super(detailSub, self).__init__(anytypeobjs_, )
supermod.detail.subclass = detailSub
# end class detailSub


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
        rootTag = 'Schema'
        rootClass = supermod.Schema
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:tns="http://www.oasis-open.org/committees/ebxml-msg/schema/msg-header-2_0.xsd"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Schema'
        rootClass = supermod.Schema
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
        rootTag = 'Schema'
        rootClass = supermod.Schema
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:tns="http://www.oasis-open.org/committees/ebxml-msg/schema/msg-header-2_0.xsd"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Schema'
        rootClass = supermod.Schema
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from finvoice.soap.msgheader import *\n\n')
        sys.stdout.write('import finvoice.soap.msgheader as model_\n\n')
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
