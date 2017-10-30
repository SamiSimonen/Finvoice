#!/usr/bin/env python

#
# Generated  by generateDS.py.
# Python 3.5.2 (default, Sep 14 2017, 22:51:06)  [GCC 5.4.0 20160609]
#
# Command line options:
#   ('-f', '')
#   ('-o', 'finvoice/ack/ackEb.py')
#   ('-s', 'finvoice/ack/ackEbsubs.py')
#   ('--super', 'finvoice.ack.ackEb')
#   ('--external-encoding', 'iso8859-15')
#   ('--no-dates', '')
#   ('--no-versions', '')
#
# Command line arguments:
#   xsd/FinvoiceackEb.xsd
#
# Command line:
#   /home/aisopuro/.virtualenvs/py-finvoice/bin/generateDS.py -f -o "finvoice/ack/ackEb.py" -s "finvoice/ack/ackEbsubs.py" --super="finvoice.ack.ackEb" --external-encoding="iso8859-15" --no-dates --no-versions xsd/FinvoiceackEb.xsd
#
# Current working directory (os.getcwd()):
#   py-finvoice
#

import sys
from lxml import etree as etree_

import finvoice.ack.ackEb as supermod

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
        rootTag = 'To'
        rootClass = supermod.To
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
        rootTag = 'To'
        rootClass = supermod.To
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
        rootTag = 'To'
        rootClass = supermod.To
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
        rootTag = 'To'
        rootClass = supermod.To
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from finvoice.ack.ackEb import *\n\n')
        sys.stdout.write('import finvoice.ack.ackEb as model_\n\n')
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
