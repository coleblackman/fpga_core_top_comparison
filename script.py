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
for top_word in find_all(top_data, "prog_clk"):
    if(everyOther): # skip (prog_clk)
        if(verbose):
            print(top_data[top_word-26:top_word-1])
        totalNumberModules+=1
    everyOther = not everyOther

print('Total number of fpga_top modules: ', totalNumberModules)

# Print number of wires
print('Number of wires in fpga_core: ', core_occurences_of_wire)
print('Number of wires in fpga_top.v:', top_occurences_of_wire)
print('\nNumber of inputs in fpga_top.v: ', top_occurences_of_input)
print('Number of inputs in fpga_core.v: ', core_occurences_of_input)
print('\nNumber of outputs in fpga_top.v: ', top_occurences_of_output)
print('Number of outputs in fpga_core.v: ', core_occurences_of_output)

# Find instances of CLBs, SBs, etc:

# First, SBs:

print('Occurrences in fpga_top.v of sb_0__0_ sb: ', top_data.count("sb_0__0_ sb"))
print('Occurrences in fpga_top.v of sb_1__0_ sb: ', top_data.count("sb_1__0_ sb"))
print('Occurrences in fpga_top.v of sb_0__1_ sb: ', top_data.count("sb_0__1_ sb"))
print('Occurrences in fpga_top.v of sb_2__0 sb: ', top_data.count("sb_2__0_ sb"))
print('Occurrences in fpga_top.v of sb_2__1 sb: ', top_data.count("sb_2__1_ sb"))
print('Occurrences in fpga_top.v of sb_2__2 sb: ', top_data.count("sb_2__2_ sb"))
print('Occurrences in fpga_top.v of sb_1__2 sb: ', top_data.count("sb_1__2_ sb"))
print('Occurrences in fpga_top.v of sb_0__2 sb: ', top_data.count("sb_0__2_ sb"))


print('\nOccurrences in fpga_core.v of sb_0__0_ sb: ', core_data.count("sb_0__0_\n  sb_0__0_"))
print('Occurrences in fpga_core.v of sb_1__0_ sb: ', core_data.count("sb_1__0_\n  sb_1__0_"))
print('Occurrences in fpga_core.v of sb_0__1_ sb: ', core_data.count("sb_0__1_\n  sb_0__1_"))
print('Occurrences in fpga_core.v of sb_2__0 sb: ', core_data.count("sb_2__0_\n  sb_2__0_"))
print('Occurrences in fpga_core.v of sb_2__1 sb: ', core_data.count("sb_2__1_\n  sb_2__1_"))
print('Occurrences in fpga_core.v of sb_2__2 sb: ', core_data.count("sb_2__2_\n  sb_2__2_"))
print('Occurrences in fpga_core.v of sb_1__2 sb: ', core_data.count("sb_1__2_\n  sb_1__2_"))
print('Occurrences in fpga_core.v of sb_0__2 sb: ', core_data.count("sb_0__2_\n  sb_0__2_"))


