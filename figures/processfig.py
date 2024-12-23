import sys
import os

fname = sys.argv[1]
fnameeps = fname+'.eps'
fnamepdf = fname+'.pdf'
fnamesvg = fname+'.svg'

print(fname)
os.system('epstopdf ' + fnameeps)
os.system('pdf2svg ' + fnamepdf + ' ' + fnamesvg)
os.system('cp ' + fnamepdf + ' ../assets/images')
os.system('cp ' + fnamesvg + ' ../assets/images')

