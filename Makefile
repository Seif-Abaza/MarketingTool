# Makefile for MarketMiner
# Variables
RELEASE := $(shell egrep 'version.*=' __init__.py 2>/dev/null | awk '{print $$3}' | tr -d "'" || echo "1.0.0")
PLATFORM := $(shell python3 -c 'import sys; print(sys.platform)')
DISTRO := $(shell python3 -c 'import platform; print(platform.dist()[0].lower())' 2>/dev/null || echo "unknown")
LINUX_VERS := $(shell python3 -c 'import platform; print(platform.dist()[1].lower())' 2>/dev/null | cut -f1-2 -d'.' || echo "unknown")
MACOS_VERS := $(shell sw_vers -productVersion 2>/dev/null | cut -f1-2 -d'.' || echo "unknown")

# Main build targets
build: build-$(PLATFORM)

# Platform-specific instructions
build-linux: dist/MarketMiner
#(cd dist; tar czf MarketMiner-LINUX_VERS.tar.gz MarketMiner)

build-darwin: dist/MarketMiner.app
	packagesbuild dev/installer-builders/macos/packages-config/MarketMiner.pkgproj 2>/dev/null || echo "macOS package build skipped"
	mv dist/MarketMiner-mac.pkg dist/MarketMiner-MACOS_VERS.pkg 2>/dev/null || true

build-win32: dist/MarketMiner.exe
	(cd dist; zip -r MarketMiner-windows.zip MarketMiner.exe)

dist/MarketMiner dist/MarketMiner.exe dist/MarketMiner.app:
	pyinstaller --clean MarketMiner.spec

# Clean up
clean:
	-rm -rf build/ dist/

.PHONY: build clean