import urllib.request as req
import os.path


def get_libraries(install_profile, root):
    libs_prof = install_profile['libraries']
    libs = {}
    for lib_prof in libs_prof:
        artifact = lib_prof['downloads']['artifact']
        path = os.path.join(root, artifact['path'])
        libs[lib_prof['name']] = path
        if artifact['url']:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            if not os.path.exists(path):
                with open(path, 'wb') as f:
                    with req.urlopen(artifact['url']) as data:
                        f.write(data.read())
    return libs
