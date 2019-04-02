import urllib.request as req


def get_libraries(install_profile):
    libs_prof = install_profile['libraries']
    libs = {}
    for lib_prof in libs_prof:
        artifact = lib_prof['downloads']['artifact']
        path = artifact['path']
        libs[lib_prof['name']] = path
        if artifact['url']:
            with open(path, 'wb') as f:
                with req.urlopen(artifact['url']) as data:
                    f.write(data.read())
    return libs
