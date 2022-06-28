import sys

verbose=False
if sys.argv[1:] == ['verbose']:
    verbose = True

top_path = input('Input location of \033[1;32mfpga_top.v\033[m, type \"local\" for local directory, or type \"default\" for default.\n> ')

if top_path == "default":
    top_path = 'generated_fpga_top/fpga_top.v'

if top_path == "local":
    top_path = 'fpga_top.v'

core_path = input('Input location of\033[1;32m fpga_core.v\033[m, type \"local\" for local directory, or type \"default\" for default.\n> ')

if core_path == "default":
    core_path = 'SOFA_HD_fpga_core/fpga_core.v'

if core_path == "local":
    core_path = 'fpga_core.v'

with open(top_path, 'r', encoding="utf-8") as top:
    top_data = top.read();
top_occurences_of_wire = top_data.count("wire")
top_occurences_of_input = top_data.count("input")
top_occurences_of_output = top_data.count("output")


with open(core_path, 'r', encoding="utf-8") as core:
    core_data = core.read();
core_occurences_of_wire = core_data.count("wire")
core_occurences_of_input = core_data.count("input")
core_occurences_of_output = core_data.count("output")



#########################################################################
totalNumberModules = 0
everyOther = True
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)
print("---------------------------------------")
# Uses prog_clk as indicator of module
for top_word in find_all(top_data, "prog_clk"):
    if(everyOther): # skip (prog_clk)
        if(verbose):
            print(top_data[top_word-26:top_word-1])
        totalNumberModules+=1
    everyOther = not everyOther

# fpga_core.v uses clk_0_E
coreNumberModules = 0
for core_word in find_all(core_data, "(\n    ."):
    if(verbose):
        print(core_data[core_word-30:core_word-2])
    coreNumberModules+=1
#for core_word in find_all(core_data, "clk_0_E")
  #  if(verbose):
   #     print(core_data[core_word-30:core_word-2])
  #  coreNumberModules+=1

print('Total number of fpga_top modules: \033[1;32m', totalNumberModules)
print('\033[mTotal number of fpga_core modules: \033[1;32m', coreNumberModules)


# Print number of wires
print('\033[mNumber of wires in fpga_core: \033[1;32m', core_occurences_of_wire)
print('\033[mNumber of wires in fpga_top.v:\033[1;32m', top_occurences_of_wire)
print('\033[m\nNumber of inputs in fpga_top.v: \033[1;32m', top_occurences_of_input)
print('\033[mNumber of inputs in fpga_core.v: \033[1;32m', core_occurences_of_input)
print('\033[m\nNumber of outputs in fpga_top.v: \033[1;32m', top_occurences_of_output)
print('\033[mNumber of outputs in fpga_core.v: \033[1;32m', core_occurences_of_output)

# Find instances of CLBs, SBs, etc:

# First, SBs:

print('\033[mOccurrences in fpga_top.v of sb_0__0_ sb: \033[1;32m', top_data.count("sb_0__0_ sb"))
print('\033[mOccurrences in fpga_top.v of sb_1__0_ sb: \033[1;32m', top_data.count("sb_1__0_ sb"))
print('\033[mOccurrences in fpga_top.v of sb_0__1_ sb: \033[1;32m', top_data.count("sb_0__1_ sb"))
print('\033[mOccurrences in fpga_top.v of sb_2__0 sb: \033[1;32m', top_data.count("sb_2__0_ sb"))
print('\033[mOccurrences in fpga_top.v of sb_2__1 sb: \033[1;32m', top_data.count("sb_2__1_ sb"))
print('\033[mOccurrences in fpga_top.v of sb_2__2 sb: \033[1;32m', top_data.count("sb_2__2_ sb"))
print('\033[mOccurrences in fpga_top.v of sb_1__2 sb: \033[1;32m', top_data.count("sb_1__2_ sb"))
print('\033[mOccurrences in fpga_top.v of sb_0__2 sb: \033[1;32m', top_data.count("sb_0__2_ sb"))


print('\033[m\nOccurrences in fpga_core.v of sb_0__0_ sb: \033[1;32m', core_data.count("sb_0__0_\n  sb_0__0_"))
print('\033[mOccurrences in fpga_core.v of sb_1__0_ sb: \033[1;32m', core_data.count("sb_1__0_\n  sb_1__0_"))
print('\033[mOccurrences in fpga_core.v of sb_0__1_ sb: \033[1;32m', core_data.count("sb_0__1_\n  sb_0__1_"))
print('\033[mOccurrences in fpga_core.v of sb_2__0 sb: \033[1;32m', core_data.count("sb_2__0_\n  sb_2__0_"))
print('\033[mOccurrences in fpga_core.v of sb_2__1 sb: \033[1;32m', core_data.count("sb_2__1_\n  sb_2__1_"))
print('\033[mOccurrences in fpga_core.v of sb_2__2 sb: \033[1;32m', core_data.count("sb_2__2_\n  sb_2__2_"))
print('\033[mOccurrences in fpga_core.v of sb_1__2 sb: \033[1;32m', core_data.count("sb_1__2_\n  sb_1__2_"))
print('\033[mOccurrences in fpga_core.v of sb_0__2 sb: \033[1;32m', core_data.count("sb_0__2_\n  sb_0__2_"))
