
PROJECT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
BUILD_DIR = $(PROJECT_DIR)/app


all: release

release:
	cd $(BUILD_DIR); python3.9 setup.py py2app

development:
	cd $(BUILD_DIR); python3.9 setup.py py2app -A

clean:
	rm -r $(BUILD_DIR)/.eggs $(BUILD_DIR)/build $(BUILD_DIR)/dist