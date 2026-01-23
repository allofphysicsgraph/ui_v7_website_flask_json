# Physics Derivation Graph
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



# todo: docker kill $(docker ps -q); make up

launch_webserver:
	docker compose up --build --force-recreate --remove-orphans --detach

launch_webserver_interactive:
	docker compose up --build --force-recreate --remove-orphans
