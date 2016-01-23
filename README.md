# 美少女万華鏡 utils
QLIE game engine tools. Used by omega star for the series.  

This is a collection of 3rd party tools, all hail to its authors.

##Usage
##### To extract .pack:
```
exfp3 dataX.pack key.fkey 15
```  
[!] key.fkey is in the game directory: \美少女万華鏡－１－\DLL\key.fkey  
[!] Files are extracted to the current dir  
  
##### To build .pack: 
```
packer.py <INPUTDIR> <output.pack>
```
[!] This script is supported by python2  
  
##### To split text from script in .s file: 
```
splt.py <file.s>
```
[!] The script produces 2 files: file.txt and file.splt, which are used later to combine evrything back to the format, readable by the engine.  
[!] python2

##### To join previously splitted script: 
```
join.py <codefile.splt> <translated.txt> <file.s>
```
[!] translated.txt should be utf16/utf16_be/utf8/shiftjis textfile.  
[!] python2  
