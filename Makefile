PHONY = help run test install

help:
	@echo "---------------HELP-----------------"
	@echo "To run the project -> make run"
	@echo "To run the tests -> make test"
	@echo "To install the project -> make install"
	@echo "------------------------------------"

run:
	flask --app src.adapters.app.application run --host 0.0.0.0 --port 8080 --reload

test:
	@echo "Test placeholder"

install:
	@echo "Install placeholder"