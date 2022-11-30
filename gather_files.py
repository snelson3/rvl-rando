# Loop through all bdscript files
# If they contain trap_enemy_set_karma_limit, copy the file over
# At the same time grab the argument and print it and filename to screen (use regex)

# Then the main file generation will be really easy, an argument to set 0, infinite, random swap, random values, and an openkh location

# Then it's just making the mod.yml and recreating the files

import os, re, shutil

values = []
files_found = 0
for root, dirs, files in os.walk(os.path.join("..", "kh2-ai-decompilation", "bdscript")):
    for ff in files:
        fn = os.path.join(root, ff)
        txt = open(fn).read()
        matches = re.findall(r'pushImmf (.*)\n.*; trap_enemy_set_karma_limit', txt)
        if matches:
            outfn = os.path.join("bdscript", re.findall(r'bdscript.obj.*', fn)[0])
            outdir = os.path.dirname(outfn)
            if not os.path.exists(outdir):
                os.makedirs(outdir)
            shutil.copy(fn, outfn)
            print(fn, matches)
            values += matches
            files_found+=1

values = [float(v) for v in values]
print("total",len(values))
print("files",files_found)
print(min(values),"-",max(values))
print(values)