import urllib.request as req
import json


def minecraft_download_url(install_profile):
    mc_ver = install_profile['minecraft']
    mmc_meta_url = f"https://meta.multimc.org/v1/net.minecraft/{mc_ver}.json"
    with req.urlopen(mmc_meta_url) as url:
        data = json.loads(url.read().decode())
        return data['mainJar']['downloads']['artifact']['url']


def download_minecraft(install_profile):
    with open('client.jar', 'wb') as f:
        with req.urlopen(minecraft_download_url(install_profile)) as data:
            f.write(data.read())
