# 美少女万華鏡 utils
omega star game engine tools.  

This is a collection of 3rd party tools, all grats goes to its authors.

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
