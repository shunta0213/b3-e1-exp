.PHONY: set-env
set-env:
	@tlmgr conf texmf $(KEY) $(VALUE)

.PHONY: clean
clean:
	@rm -rf ./**/dist/

.PHONY: venv
venv:
	@python3 -m venv venv
