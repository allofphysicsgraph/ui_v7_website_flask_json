# Physics Derivation Graph
# https://allofphysics.com
# Ben Payne, 2026

# Creative Commons Attribution 4.0 International License
# https://creativecommons.org/licenses/by/4.0/

# Get the machine architecture.
# On arm64 (Apple Silicon M1/M2/etc.), `uname -m` outputs "arm64".
# On amd64 (Intel), `uname -m` outputs "x86_64".
ARCH := $(shell uname -m)

ifeq ($(ARCH), arm64)
        this_arch=arm64
else ifeq ($(ARCH), x86_64)
        this_arch=amd64
else
        @echo "Unknown architecture: $(ARCH). Cannot determine if Mac is new (arm64) or old (amd64)."
endif

CONTAINER_TAG=latest-$(this_arch)

DOCKER_OR_PODMAN=docker
#DOCKER_OR_PODMAN=podman

# .PHONY is special target used to declare that a target name does not correspond to an actual file to be built.
.PHONY: help clean webserver typehints flake8 pylint doctest mccabe

# todo: $(DOCKER_OR_PODMAN) kill $(docker ps -q); make up

launch_webserver:
	$(DOCKER_OR_PODMAN) compose up --build --force-recreate --remove-orphans --detach

launch_webserver_interactive:
	$(DOCKER_OR_PODMAN) compose up --build --force-recreate --remove-orphans

down:
	# https://docs.docker.com/compose/reference/down/
	$(DOCKER_OR_PODMAN) compose down --volumes --remove-orphans

# This will remove:
#  - all stopped containers
#  - all networks not used by at least one container
#  - all dangling images
#  - unused build cache
clear_containers:
	docker system prune


# EOF
