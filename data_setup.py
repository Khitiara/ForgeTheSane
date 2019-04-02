import os
import mvn
import mcdl


def data_setup(install_profile, installer_jar):
    base = 'data/' + install_profile['version']
    os.makedirs(base, exist_ok=True)
    mcdl.download_minecraft(install_profile, base)
    mvn.get_libraries(install_profile, base)
