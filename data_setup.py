import os
import mvn
import mcdl
import json
from zipfile import ZipFile


def data_setup(installer_jar):
    with ZipFile(installer_jar, 'r') as forge_archive:
        install_profile = get_install_profile(forge_archive)
        base = 'data/' + install_profile['version']
        os.makedirs(base, exist_ok=True)
        mcdl.download_minecraft(install_profile, base)
        mvn.get_libraries(install_profile, forge_archive, base)
        mvn.get_data(install_profile, forge_archive, base)

def get_install_profile(archive):
    with archive.open('install_profile.json') as prof:
        return json.load(prof)
