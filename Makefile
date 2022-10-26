PHONY = help run test install init-db

help:
	@echo "---------------HELP-----------------"
	@echo "To run the project -> make run"
	@echo "To run the tests -> make test"
	@echo "To install the project -> make install"
	@echo "To create empty tables -> make init-db"
	@echo "------------------------------------"

run:
	flask --app src.adapters.app.application run --host 0.0.0.0 --port 8080 --reload

init-db:
	flask --app src.adapters.app.application init-db

test:
	@echo "Test placeholder"

install:
	@echo "Install placeholder"