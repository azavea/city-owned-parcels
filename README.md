# City Owned Property

A web app to view properties owned by the City of Philadelphia.

This project is mainly to practice building a complete web app using Postgres, Nginx, Gunicorn, Flask, Docker, AWS EC2, and RDS. Some code was copied from pwd-stormdrain-marking and usace-program-analysis to get started.

### Requirements

* Vagrant 1.8.1
* VirtualBox 4.3
* Ansible 2.1

### Getting Started

#### Quick setup

Clone the project, `cd` into the directory, then run `./scripts/setup.sh` to create the Vagrant VM and then build the Docker containers.

To start the servers during development:

    vagrant ssh
    ./scripts/server.sh

#### Using Docker in the VM

The other project scripts are meant to execute in the VM in the `/vagrant` directory. To run the containers during development use the following commands:

    vagrant ssh
    ./scripts/server.sh

### Ports

| Port | Service |
| --- | --- |
| [9100](http://localhost:9100) | Nginx |
| [8080](http://localhost:8080) | Gunicorn |
| [8081](http://localhost:8081) | Flask debug server |

### Testing

To run linters and tests:

    vagrant ssh
    ./scripts/test.sh

### Scripts

| Name | Description |
| `clean.sh` | Clean up unused Docker resources to free disk space |
| `console.sh` | Login to a running Docker container's shell |
| `server.sh` | Run `docker-compose up` to start the containers |
| `setup.sh` | Bring up the VM, then build the Docker containers |
| `update.sh` | Rebuild the containers with current required dependencies |

### Docker

This project uses Docker containers inside the Vagrant box. Below are a few Docker commands you can use to get oriented to what's happening in the VM. You'll need to `vagrant ssh` into the VM to use them:

- `docker images` will show you a list of all your VM's installed images
- `docker rmi <IMAGE-NAME>` will delete the specified image
- `docker run -it usace-program-analysis-react /bin/sh` will log you into the `usace-program-analysis-react` image's shell
- `docker-compose up` will build and start containers according to the instructions in `docker-compose.yml` file
- `docker-compose ps` will show you a list of running containers
- `docker-compose down` will halt these running containers
- `docker-compose build` will rebuild all containers listed in the `docker-compose.yml` file
- `docker-compose build react` will rebuild only the react container per instructions listed in `docker-compose.yml`
- `docker-compose exec <SERVICE> /bin/sh` where `<SERVICE>` is a service name specified in `docker-compose.yml` will open a shell to a currently running container.

See the
[docker](https://docs.docker.com/engine/reference/commandline/) and  [docker-compose](https://docs.docker.com/compose/reference/overview/)
 command line reference guides for more information.
