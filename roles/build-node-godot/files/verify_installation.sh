#!/bin/bash

# Executed in ansible task to verify 
# build node has required dependencies installed


# strict mode
set -euo pipefail

which clang++-7
which wget
which curl
which perf
which scons

which dot
which doxygen

