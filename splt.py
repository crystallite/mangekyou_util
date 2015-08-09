import os,sys

mbcode = 'shiftjis'
#mbcode = 'gbk'

def listunifile(filename):
	f = open(filename,'rb').read()
	if f[:2]=='\xff\xfe': f = f.decode('utf16')
	elif f[:2]=='\xfe\xff': f = f[2:].decode('utf_16_be')
	elif f[:3]=='\xef\xbb\xbf': f = f[3:].decode('utf8')
	else: f = f.decode(mbcode)
	return f.replace('\r\n','\n').split(u'\n')

def findText(line):
	found = False
	for n in range(len(line)):
		c = line[n]
		if ord(c)>0x80:
			startpos = n
			found = True
			break
	if not found:
		return False
	for n in range(len(line),0, -1):
		c = line[n-1]
		if ord(c)>0x80:
			endpos = n
			break
	return startpos, endpos

charIgnore = {
    u'　': u'　',
    u'「': u'「',
    u'『': u'『',
    u'（': u'（',
    u'！': u'！',
    u'？': u'？',
    u'…': u'…',
    u'—': u'—',
    u'─': u'—',
    u'，': u'，',
    u'。': u'。',
    u'～': u'～',
    u'〜': u'～',
    u'」': u'」',
    u'』': u'』',
    u'）': u'）',
    u'•' : u'·',
    u'・' : u'·',
    u'♪': u'♪',
}

def getDisp(line):
	displine = []
	for c in line:
		if c not in charIgnore: break
		displine.append(charIgnore[c])
	return ''.join(displine)

ignoreLine = [u'//', u'％',u'^cdel',u'^cbase',u'^iload',u'^cface',u'^sload',\
		u'^ffade',u'^cd',u'^cadd',u'^ce',u'^cinit',u'\\li',u'^eeffect',u'\\l,"',u'\\sub,@@!Avg_CharaGetNo,']
def checkIgnoreLine(line):
	chkline = line.strip()
	for chk in ignoreLine:
		if chkline.startswith(chk): return True
	return False

nameLine = [u'【']
def checkName(line):
	chkline = line.strip()
	for chk in nameLine:
		if chkline.startswith(chk):
			return [0,len(line)]
	return False

textLine = ['^savedate','^saveroute','^savescene',u'^select']
def checkTextLine(line):
	chkline = line.strip()
	for chk in textLine:
		if chkline.startswith(chk):
			return findText(line)
	textpos = findText(line)
	if textpos:
		if textpos[0]:
			print 'found unexpected text:'
			print line.encode('gb18030')
		else:
			return textpos
	return False

def SpltS(filename):
	TEXT=[]
	SPLT=[]
	counter = 1
	for line in listunifile(filename):
		if checkIgnoreLine(line):
			SPLT.append(line)
			continue
		textpos = checkTextLine(line)
		if not textpos:
			SPLT.append(line)
			continue
		p, q = textpos
                text = u''
                disp = u''
		text += line[p:q]
		disp += getDisp(line[p:q])
		line = line[:p] + '<TeXt>%d</tExT>'%counter + line[q:]
		SPLT.append(line)
		TEXT.append(text)
		counter += 1
	open(os.path.splitext(filename)[0]+'.txt','wb').write(u'\r\n'.join(TEXT).encode('utf16'))
	open(os.path.splitext(filename)[0]+'.splt','wb').write(u'\r\n'.join(SPLT).encode('shiftjis'))

SpltS(sys.argv[1])
