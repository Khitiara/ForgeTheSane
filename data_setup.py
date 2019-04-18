import os
import mvn
import mcdl
import json
import os.path
from zipfile import ZipFile


def data_setup(installer_jar):
    with ZipFile(installer_jar, 'r') as forge_archive:
        install_profile = get_install_profile(forge_archive)
        base = os.path.join('data', install_profile['version'])
        os.makedirs(base, exist_ok=True)
        mcpath = mcdl.download_minecraft(install_profile, base)
        libs = mvn.get_libraries(install_profile, forge_archive, base)
        data = mvn.get_data(install_profile, forge_archive, base)
        data['MINECRAFT_JAR'] = mcpath
        # put output jar in the base directory, so we don't need to
        # dig it out of several nested directories
        data['PATCHED'] = os.path.join(base, os.path.split(data['PATCHED'])[1])
        return parse_processors(install_profile, libs, data, base)

def get_install_profile(archive):
    with archive.open('install_profile.json') as prof:
        return json.load(prof)

def parse_processors(install_profile, libraries, data, root):
    """Returns the list of processors to run from the install profile.

    This method transforms {data} and [maven] references into paths, including
    maven references in the 'jar' and 'classpath' sections.
    """
    def resolve_arg(arg):
        """Resolves {data} and [maven] references."""
        if arg[0] == '[':
            # maven reference
            return libraries[arg[1:-1]]
        elif arg[0] == '{':
            # data reference
            return data[arg[1:-1]]
        else:
            # unchanged
            return arg
    procs_prof = install_profile['processors']
    procs = []
    for proc_prof in procs_prof:
        proc = {}
        proc['jar'] = libraries[proc_prof['jar']]
        proc['classpath'] = [libraries[el] for el in proc_prof['classpath']]
        proc['args'] = [resolve_arg(arg) for arg in proc_prof['args']]
        # (ignore outputs)
        procs.append(proc)
    return procs
