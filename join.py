#import pdb
import os,sys

codefile, textfile, outfile = sys.argv[1:4]

ignoreChar = {
    u' ': u'　',
    u'"': u'”',
    u'\'': u'’',
    u'(': u'（',
    u'!': u'！',
    u'?': u'？',
    u"...": u'…',
    u'-': u'‐',
    u',': u'，',
    u'.': u'．',
    u'~': u'～',
    u')': u'）',
#    u']': u'］',
#    u'[': u'［',
    u'*': u'＊',
    u"\u2014": u'‐'}

def listunifile(filename):
	f = open(filename,'rb').read()
	if f[:2]=='\xff\xfe': f = f.decode('utf16')
	elif f[:2]=='\xfe\xff': f = f[2:].decode('utf_16_be')
	elif f[:3]=='\xef\xbb\xbf': f = f[3:].decode('utf8')
	else: f = f.decode('shiftjis')
	return f.replace(u'\r\n',u'\n').replace(u'\r','').split(u'\n')

Text=[]
Text.append(u'\n')
print 'importing %s ...'%os.path.split(textfile)[1]
for line in listunifile(textfile):
        for k, v in ignoreChar.iteritems():
                line = line.replace(k, v)
        Text.append(line)

data = []
textStartToken = '<TeXt>'
textEndToken   = '</tExT>'
for line in open(codefile,'rb').read().decode('shiftjis').split(u'\n'):
	if textStartToken in line:
		p = line.index(textStartToken)
		q = line.index(textEndToken,p)
		count = line[p+len(textStartToken):q]
		line = line[:p]+Text[int(count)]+line[q+len(textEndToken):]
	data.append(line)
	
open(outfile,'wb').write(u'\n'.join(data).encode('shiftjis'))
