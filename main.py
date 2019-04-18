import data_setup
import procedures
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '<forge-installer-jar>')
    else:
        forge_name = sys.argv[1]
        procs = data_setup.data_setup(forge_name)
        procedures.run_procs(procs)
