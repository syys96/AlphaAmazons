import codecs
import os
import re

src_dir = "cpp/"

src = ["Action.h", "Action.cpp", "ChessBoard.h", "ChessBoard.cpp",
       "EvalField.h", "EvalField.cpp", "MCTree.h", "MCTree.cpp", ]
src += ["main.cpp"]
src = [src_dir + x for x in src]

lines = []
for filename in src:
    assert (os.path.isfile(filename))
    fobj = codecs.open(filename, "r", "utf-8")
    lines += fobj.readlines()
    lines[-1] += "\n"
    fobj.close()

lines = "".join(lines)

# suppress redundant include header macros
lines = re.sub(r"\s*#include *\"(?!json).*\".*\n", "\n", lines)

target = "main_merge.cpp"

fobj = codecs.open(target, "w", "utf-8")
fobj.writelines(lines)
fobj.close()