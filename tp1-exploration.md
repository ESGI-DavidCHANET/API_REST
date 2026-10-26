# API_REST -- TP1
## 1 ##

C:\Users\david\Desktop\ESGI\M1\API_REST\Github>docker run -d --name web1 --label adminapi.managed=true nginx:alpine
830fcda23bef9665a69710d318eebc07b96cf9f0900400e939257a891a54b003

C:\Users\david\Desktop\ESGI\M1\API_REST\Github>docker run -d --name intrus nginx:alpine
e570fb9ea4a1c9157e9fe518840e1bb5959ca9a3c14133592730dddb024f6b20

C:\Users\david\Desktop\ESGI\M1\API_REST\Github>docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
e570fb9ea4a1   nginx:alpine   "/docker-entrypoint.…"   17 seconds ago   Up 16 seconds   80/tcp    intrus
830fcda23bef   nginx:alpine   "/docker-entrypoint.…"   18 seconds ago   Up 18 seconds   80/tcp    web1

## 2 ##

### Lisez la version

C:\Users\david\Desktop\ESGI\M1\API_REST\Github>curl.exe -s "http://localhost:2375/version" | python -m json.tool
{
    "Platform": {
        "Name": "Docker Desktop 4.83.0 (234302)"
    },
    "Version": "29.6.2",
    "ApiVersion": "1.55",
    "MinAPIVersion": "1.40",
    "Os": "linux",
    "Arch": "amd64",
    "Components": [
        {
            "Name": "Engine",
            "Version": "29.6.2",
            "Details": {
                "ApiVersion": "1.55",
                "Arch": "amd64",
                "BuildTime": "2026-07-16T16:12:20.000000000+00:00",
                "Experimental": "false",
                "GitCommit": "3d80467",
                "GoVersion": "go1.26.5",
                "KernelVersion": "6.18.33.2-microsoft-standard-WSL2",
                "MinAPIVersion": "1.40",
                "Module": "github.com/moby/moby/v2",
                "ModuleVersion": "v2.0.0+unknown",
                "Os": "linux"
            }
        },
        {
            "Name": "containerd",
            "Version": "v2.2.5",
            "Details": {
                "GitCommit": "e53c7c1516c3b2bff98eb76f1f4117477e6f4e66"
            }
        },
        {
            "Name": "runc",
            "Version": "1.3.6",
            "Details": {
                "GitCommit": "v1.3.6-0-g491b69ba"
            }
        },
        {
            "Name": "docker-init",
            "Version": "0.19.0",
            "Details": {
                "GitCommit": "de40ad0"
            }
        }
    ],
    "GitCommit": "3d80467",
    "GoVersion": "go1.26.5",
    "KernelVersion": "6.18.33.2-microsoft-standard-WSL2",
    "BuildTime": "2026-07-16T16:12:20.000000000+00:00"
}

### Listez tous les conteneurs

C:\Users\david\Desktop\ESGI\M1\API_REST\Github>curl.exe -s "http://localhost:2375/containers/json?all=true" | python -m json.tool
[
    {
        "Id": "e570fb9ea4a1c9157e9fe518840e1bb5959ca9a3c14133592730dddb024f6b20",
        "Names": [
            "/intrus"
        ],
        "Image": "nginx:alpine",
        "ImageID": "sha256:892bb2152464f0c5d8972593a5f5afaf8054552580b699d95f8ff4af08c2d33d",
        "ImageManifestDescriptor": {
            "mediaType": "application/vnd.oci.image.manifest.v1+json",
            "digest": "sha256:138af827713b7671ef4ee2deea73bc6f08ae265130ce350307e3e7b52cd4b51b",
            "size": 2495,
            "annotations": {
                "com.docker.official-images.bashbrew.arch": "amd64",
                "org.opencontainers.image.base.digest": "sha256:ee49b03f56b9a8b01fbbef655495d9feaa2e22169b2a4f8a3f2972f16e05f711",
                "org.opencontainers.image.base.name": "nginx:1.31.7-alpine-slim",
                "org.opencontainers.image.created": "2026-10-14T18:51:30Z",
                "org.opencontainers.image.revision": "4b9f658be76820b24e4ef4605413a5c08707a512",
                "org.opencontainers.image.source": "https://github.com/nginx/docker-nginx.git#4b9f658be76820b24e4ef4605413a5c08707a512:mainline/alpine",
                "org.opencontainers.image.url": "https://hub.docker.com/_/nginx",
                "org.opencontainers.image.version": "1.31.7-alpine"
            },
            "platform": {
                "architecture": "amd64",
                "os": "linux"
            }
        },
        "Command": "/docker-entrypoint.sh nginx -g 'daemon off;'",
        "Created": 1793006473,
        "Ports": [
            {
                "IP": "",
                "PrivatePort": 80,
                "Type": "tcp"
            }
        ],
        "Labels": {
            "desktop.docker.io/ports.scheme": "v2",
            "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
        },
        "State": "running",
        "Status": "Up 9 minutes",
        "HostConfig": {
            "NetworkMode": "bridge"
        },
        "Health": {
            "Status": "none",
            "FailingStreak": 0
        },
        "NetworkSettings": {
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "DriverOpts": null,
                    "GwPriority": 0,
                    "NetworkID": "b027ecd4720145c85534def96c657b853141e71cb50bcc2c09ab09b2ecae6820",
                    "EndpointID": "e265d1d0c27fb8a72b35591e41103f8bb1b15c22f91f443889d1f884c749020d",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.3",
                    "MacAddress": "5e:2a:95:39:27:26",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": null
                }
            }
        },
        "Mounts": []
    },
    {
        "Id": "830fcda23bef9665a69710d318eebc07b96cf9f0900400e939257a891a54b003",
        "Names": [
            "/web1"
        ],
        "Image": "nginx:alpine",
        "ImageID": "sha256:892bb2152464f0c5d8972593a5f5afaf8054552580b699d95f8ff4af08c2d33d",
        "ImageManifestDescriptor": {
            "mediaType": "application/vnd.oci.image.manifest.v1+json",
            "digest": "sha256:138af827713b7671ef4ee2deea73bc6f08ae265130ce350307e3e7b52cd4b51b",
            "size": 2495,
            "annotations": {
                "com.docker.official-images.bashbrew.arch": "amd64",
                "org.opencontainers.image.base.digest": "sha256:ee49b03f56b9a8b01fbbef655495d9feaa2e22169b2a4f8a3f2972f16e05f711",
                "org.opencontainers.image.base.name": "nginx:1.31.7-alpine-slim",
                "org.opencontainers.image.created": "2026-10-14T18:51:30Z",
                "org.opencontainers.image.revision": "4b9f658be76820b24e4ef4605413a5c08707a512",
                "org.opencontainers.image.source": "https://github.com/nginx/docker-nginx.git#4b9f658be76820b24e4ef4605413a5c08707a512:mainline/alpine",
                "org.opencontainers.image.url": "https://hub.docker.com/_/nginx",
                "org.opencontainers.image.version": "1.31.7-alpine"
            },
            "platform": {
                "architecture": "amd64",
                "os": "linux"
            }
        },
        "Command": "/docker-entrypoint.sh nginx -g 'daemon off;'",
        "Created": 1793006472,
        "Ports": [
            {
                "IP": "",
                "PrivatePort": 80,
                "Type": "tcp"
            }
        ],
        "Labels": {
            "adminapi.managed": "true",
            "desktop.docker.io/ports.scheme": "v2",
            "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
        },
        "State": "running",
        "Status": "Up 9 minutes",
        "HostConfig": {
            "NetworkMode": "bridge"
        },
        "Health": {
            "Status": "none",
            "FailingStreak": 0
        },
        "NetworkSettings": {
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "DriverOpts": null,
                    "GwPriority": 0,
                    "NetworkID": "b027ecd4720145c85534def96c657b853141e71cb50bcc2c09ab09b2ecae6820",
                    "EndpointID": "9bee9d5402c4767ab53fa237c6c0aec17edb631c6fb302749e2e9bfe3f40bb50",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "MacAddress": "0a:8b:48:a5:34:c9",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": null
                }
            }
        },
        "Mounts": []
    }
]

### Listez seulement ceux qui portent le label

C:\Users\david\Desktop\ESGI\M1\API_REST\Github>curl.exe -s "http://localhost:2375/containers/json?all=true&filters=%7B%22label%22%3A%5B%22adminapi.managed%3Dtrue%22%5D%7D" | python -m json.tool
[
    {
        "Id": "830fcda23bef9665a69710d318eebc07b96cf9f0900400e939257a891a54b003",
        "Names": [
            "/web1"
        ],
        "Image": "nginx:alpine",
        "ImageID": "sha256:892bb2152464f0c5d8972593a5f5afaf8054552580b699d95f8ff4af08c2d33d",
        "ImageManifestDescriptor": {
            "mediaType": "application/vnd.oci.image.manifest.v1+json",
            "digest": "sha256:138af827713b7671ef4ee2deea73bc6f08ae265130ce350307e3e7b52cd4b51b",
            "size": 2495,
            "annotations": {
                "com.docker.official-images.bashbrew.arch": "amd64",
                "org.opencontainers.image.base.digest": "sha256:ee49b03f56b9a8b01fbbef655495d9feaa2e22169b2a4f8a3f2972f16e05f711",
                "org.opencontainers.image.base.name": "nginx:1.31.7-alpine-slim",
                "org.opencontainers.image.created": "2026-10-14T18:51:30Z",
                "org.opencontainers.image.revision": "4b9f658be76820b24e4ef4605413a5c08707a512",
                "org.opencontainers.image.source": "https://github.com/nginx/docker-nginx.git#4b9f658be76820b24e4ef4605413a5c08707a512:mainline/alpine",
                "org.opencontainers.image.url": "https://hub.docker.com/_/nginx",
                "org.opencontainers.image.version": "1.31.7-alpine"
            },
            "platform": {
                "architecture": "amd64",
                "os": "linux"
            }
        },
        "Command": "/docker-entrypoint.sh nginx -g 'daemon off;'",
        "Created": 1793006472,
        "Ports": [
            {
                "IP": "",
                "PrivatePort": 80,
                "Type": "tcp"
            }
        ],
        "Labels": {
            "adminapi.managed": "true",
            "desktop.docker.io/ports.scheme": "v2",
            "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
        },
        "State": "running",
        "Status": "Up 10 minutes",
        "HostConfig": {
            "NetworkMode": "bridge"
        },
        "Health": {
            "Status": "none",
            "FailingStreak": 0
        },
        "NetworkSettings": {
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "DriverOpts": null,
                    "GwPriority": 0,
                    "NetworkID": "b027ecd4720145c85534def96c657b853141e71cb50bcc2c09ab09b2ecae6820",
                    "EndpointID": "9bee9d5402c4767ab53fa237c6c0aec17edb631c6fb302749e2e9bfe3f40bb50",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "MacAddress": "0a:8b:48:a5:34:c9",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": null
                }
            }
        },
        "Mounts": []
    }


### Lisez le détail de web1

C:\Users\david\Desktop\ESGI\M1\API_REST\Github>curl.exe -s "http://localhost:2375/containers/web1/json" | python -m json.tool
{
    "Id": "830fcda23bef9665a69710d318eebc07b96cf9f0900400e939257a891a54b003",
    "Created": "2026-10-26T09:21:12.373522042Z",
    "Path": "/docker-entrypoint.sh",
    "Args": [
        "nginx",
        "-g",
        "daemon off;"
    ],
    "State": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 1064,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-10-26T09:21:12.431574068Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
    },
    "Image": "sha256:892bb2152464f0c5d8972593a5f5afaf8054552580b699d95f8ff4af08c2d33d",
    "ResolvConfPath": "/var/lib/docker/containers/830fcda23bef9665a69710d318eebc07b96cf9f0900400e939257a891a54b003/resolv.conf",
    "HostnamePath": "/var/lib/docker/containers/830fcda23bef9665a69710d318eebc07b96cf9f0900400e939257a891a54b003/hostname",
    "HostsPath": "/var/lib/docker/containers/830fcda23bef9665a69710d318eebc07b96cf9f0900400e939257a891a54b003/hosts",
    "LogPath": "/var/lib/docker/containers/830fcda23bef9665a69710d318eebc07b96cf9f0900400e939257a891a54b003/830fcda23bef9665a69710d318eebc07b96cf9f0900400e939257a891a54b003-json.log",
    "Name": "/web1",
    "RestartCount": 0,
    "Driver": "overlayfs",
    "Platform": "linux",
    "MountLabel": "",
    "ProcessLabel": "",
    "AppArmorProfile": "",
    "ExecIDs": null,
    "HostConfig": {
        "Binds": null,
        "ContainerIDFile": "",
        "LogConfig": {
            "Type": "json-file",
            "Config": {}
        },
        "NetworkMode": "bridge",
        "PortBindings": {},
        "RestartPolicy": {
            "Name": "no",
            "MaximumRetryCount": 0
        },
        "AutoRemove": false,
        "VolumeDriver": "",
        "VolumesFrom": null,
        "ConsoleSize": [
            57,
            108
        ],
        "CapAdd": null,
        "CapDrop": null,
        "CgroupnsMode": "private",
        "Dns": null,
        "DnsOptions": [],
        "DnsSearch": [],
        "ExtraHosts": null,
        "GroupAdd": null,
        "IpcMode": "private",
        "Cgroup": "",
        "Links": null,
        "OomScoreAdj": 0,
        "PidMode": "",
        "Privileged": false,
        "PublishAllPorts": false,
        "ReadonlyRootfs": false,
        "SecurityOpt": null,
        "UTSMode": "",
        "UsernsMode": "",
        "ShmSize": 67108864,
        "Runtime": "runc",
        "Isolation": "",
        "CpuShares": 0,
        "Memory": 0,
        "NanoCpus": 0,
        "CgroupParent": "",
        "BlkioWeight": 0,
        "BlkioWeightDevice": [],
        "BlkioDeviceReadBps": [],
        "BlkioDeviceWriteBps": [],
        "BlkioDeviceReadIOps": [],
        "BlkioDeviceWriteIOps": [],
        "CpuPeriod": 0,
        "CpuQuota": 0,
        "CpuRealtimePeriod": 0,
        "CpuRealtimeRuntime": 0,
        "CpusetCpus": "",
        "CpusetMems": "",
        "Devices": [],
        "DeviceCgroupRules": null,
        "DeviceRequests": null,
        "MemoryReservation": 0,
        "MemorySwap": 0,
        "MemorySwappiness": null,
        "OomKillDisable": null,
        "PidsLimit": null,
        "Ulimits": [],
        "CpuCount": 0,
        "CpuPercent": 0,
        "IOMaximumIOps": 0,
        "IOMaximumBandwidth": 0,
        "MaskedPaths": [
            "/proc/acpi",
            "/proc/asound",
            "/proc/interrupts",
            "/proc/kcore",
            "/proc/keys",
            "/proc/latency_stats",
            "/proc/sched_debug",
            "/proc/scsi",
            "/proc/timer_list",
            "/proc/timer_stats",
            "/sys/devices/virtual/powercap",
            "/sys/firmware"
        ],
        "ReadonlyPaths": [
            "/proc/bus",
            "/proc/fs",
            "/proc/irq",
            "/proc/sys",
            "/proc/sysrq-trigger"
        ]
    },
    "Storage": {
        "RootFS": {
            "Snapshot": {
                "Name": "overlayfs"
            }
        }
    },
    "Mounts": [],
    "Config": {
        "Hostname": "830fcda23bef",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "ExposedPorts": {
            "80/tcp": {}
        },
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "NGINX_VERSION=1.31.7",
            "PKG_RELEASE=1",
            "DYNPKG_RELEASE=1",
            "NJS_VERSION=1.0.2",
            "NJS_RELEASE=1",
            "ACME_VERSION=0.4.1"
        ],
        "Cmd": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "Image": "nginx:alpine",
        "Volumes": null,
        "WorkingDir": "/",
        "Entrypoint": [
            "/docker-entrypoint.sh"
        ],
        "Labels": {
            "adminapi.managed": "true",
            "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
        },
        "StopSignal": "SIGQUIT"
    },
    "NetworkSettings": {
        "SandboxID": "4d925368b29a5bb26281095708f1cf830a08ab75750e15d8d85a8db944021d52",
        "SandboxKey": "/var/run/docker/netns/4d925368b29a",
        "Ports": {
            "80/tcp": null
        },
        "Networks": {
            "bridge": {
                "IPAMConfig": null,
                "Links": null,
                "Aliases": null,
                "DriverOpts": null,
                "GwPriority": 0,
                "NetworkID": "b027ecd4720145c85534def96c657b853141e71cb50bcc2c09ab09b2ecae6820",
                "EndpointID": "9bee9d5402c4767ab53fa237c6c0aec17edb631c6fb302749e2e9bfe3f40bb50",
                "Gateway": "172.17.0.1",
                "IPAddress": "172.17.0.2",
                "MacAddress": "0a:8b:48:a5:34:c9",
                "IPPrefixLen": 16,
                "IPv6Gateway": "",
                "GlobalIPv6Address": "",
                "GlobalIPv6PrefixLen": 0,
                "DNSNames": null
            }
        }
    },
    "ImageManifestDescriptor": {
        "mediaType": "application/vnd.oci.image.manifest.v1+json",
        "digest": "sha256:138af827713b7671ef4ee2deea73bc6f08ae265130ce350307e3e7b52cd4b51b",
        "size": 2495,
        "annotations": {
            "com.docker.official-images.bashbrew.arch": "amd64",
            "org.opencontainers.image.base.digest": "sha256:ee49b03f56b9a8b01fbbef655495d9feaa2e22169b2a4f8a3f2972f16e05f711",
            "org.opencontainers.image.base.name": "nginx:1.31.7-alpine-slim",
            "org.opencontainers.image.created": "2026-10-14T18:51:30Z",
            "org.opencontainers.image.revision": "4b9f658be76820b24e4ef4605413a5c08707a512",
            "org.opencontainers.image.source": "https://github.com/nginx/docker-nginx.git#4b9f658be76820b24e4ef4605413a5c08707a512:mainline/alpine",
            "org.opencontainers.image.url": "https://hub.docker.com/_/nginx",
            "org.opencontainers.image.version": "1.31.7-alpine"
        },
        "platform": {
            "architecture": "amd64",
            "os": "linux"
        }
    }
}

## 3 ##

C:\Users\david\Desktop\ESGI\M1\API_REST\Github>curl.exe -s -o NUL -w "%{http_code}" -X POST "http://localhost:2375/containers/web1/stop"
204

C:\Users\david\Desktop\ESGI\M1\API_REST\Github>curl.exe -s -o NUL -w "%{http_code}" -X POST "http://localhost:2375/containers/web1/stop"
304

C:\Users\david\Desktop\ESGI\M1\API_REST\Github>curl.exe -s -w "%{http_code}" "http://localhost:2375/containers/nexistepas/json"
{"message":"No such container: nexistepas"}
404

## 4 ##

### Obtention du token

C:\Users\david\Desktop\ESGI\M1\API_REST\Github\projet>curl -s -X POST http://127.0.0.1:8080/api/users/tokens/provision/ -H "Content-Type: application/json" -H "Accept: application/json" -d "{\"username\": \"admin\", \"password\": \"admin\"}"

{"id":1,"url":"http://127.0.0.1:8080/api/users/tokens/1/","display_url":"http://127.0.0.1:8080/users/tokens/1/","display":"q1QjvHx4BSTX","version":2,"user":{"id":1,"url":"http://127.0.0.1:8080/api/users/users/1/","display":"admin","username":"admin"},"key":"q1QjvHx4BSTX","created":"2026-10-26T10:31:34.946705Z","expires":null,"last_used":null,"enabled":true,"write_enabled":true,"description":"","allowed_ips":[],"token":"fddSBrCdBDlpv0JK5SnkOtvyEW8kWVnhoveKiGvf"}

### Vérification du token

C:\Users\david\Desktop\ESGI\M1\API_REST\Github\projet>curl -s http://127.0.0.1:8080/api/status/ -H "Authorization: Bearer nbt_q1QjvHx4BSTX.fddSBrCdBDlpv0JK5SnkOtvyEW8kWVnhoveKiGvf" -H "Accept: application/json"

{"django-version":"6.1.2","hostname":"574a0a11bda8","installed_apps":{"django_filters":"26.2","django_prometheus":"2.4.0","django_rq":"4.2.0","django_tables2":"3.0.1","drf_spectacular":"0.30.0","drf_spectacular_sidecar":"2026.10.1","mptt":"0.18.0","rest_framework":"3.18.0","social_django":"6.1.0","taggit":"6.1.0","timezone_field":"7.2.2"},"netbox-version":"4.7.3","netbox-full-version":"4.7.3-Docker-5.1.1","plugins":{},"python-version":"3.14.4","rq-workers-running":0}
C:\Users\david\Desktop\ESGI\M1\API_REST\Github\projet>

