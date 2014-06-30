# BlitzMax wrapper generator
# Thanks to James Boyd for help with this!

import soloud_codegen 

fo = open("soloud.bmx", "w")

"""
Global SoloudLib:Int = LoadLibraryA ("soloud_x86.dll")

If not SoloudLib Then Notify "soloud_x86.dll not found"; End

Const SFXR_BLIP:Int = 6

Global Soloud_destroy:Int (aSoloud:Byte Ptr) "win32" = GetProcAddress (SoloudLib, "Soloud_destroy")

"""

C_TO_BMX_TYPES = {
    "int":"Int",
    "void":"Int",
    "const char *":"Byte Ptr",
    "unsigned int":"Int",
    "float":"Float",
    "double":"Double",
    "float *":"Float Ptr",
    "unsigned char *":"Byte Ptr"
}

for soloud_type in soloud_codegen.soloud_type:
    C_TO_BMX_TYPES[soloud_type + " *"] = "Byte Ptr"

fo.write("' SoLoud wrapper for BlitzMax\n")
fo.write("' This file is autogenerated; any changes will be overwritten\n")
fo.write("\n")
fo.write('Global SoloudLib:Int = LoadLibraryA ("soloud_x86.dll")\n')
fo.write('If not SoloudLib Then Notify "soloud_x86.dll not found"; End\n')
fo.write("\n")
fo.write("' Enumerations\n")
for x in soloud_codegen.soloud_enum:
   fo.write("Const " + x + ":Int = " + str(soloud_codegen.soloud_enum[x]) + "\n")
fo.write("\n")
fo.write("' Functions\n")
for x in soloud_codegen.soloud_func:
  funcdef = "Global " + x[1] + ":" + C_TO_BMX_TYPES[x[0]] + " ("
  first = True;
  for p in x[2]:
    if len(p) > 0:
      if not first:
         funcdef += ", "
      else:
         first = False
      funcdef += p[1] + ":" + C_TO_BMX_TYPES[p[0]]
  funcdef += ")" 
  funcdef += ' "win32" = GetProcAddress (SoloudLib, "'+x[1]+'")'
  fo.write(funcdef + "\n")
  
fo.close()
print "soloud.bmx generated"
