import yaml

devices = {"devices":
           [{"nxos-1": {"ip": "192.168.181.21"}},
            {"nxos-2": {"ip": "192.168.181.22"}},
            {"nxos-3": {"ip": "192.168.181.23"}},
            {"nxos-4": {"ip": "192.168.181.24"}}
            ]
           }

with open("devices.yml", "w") as fobj:
    yaml.dump(devices, fobj)