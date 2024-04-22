.PHONY: set-env
set-env:
	@tlmgr conf texmf $(KEY) $(VALUE)
	@echo '\CatchFileEdef{\\var$(KEY)}{|"kpsewhich -var-value=$(KEY)"}{\\endlinechar=-1 }' >> ./src/styles/env.sty

.PHONY: venv
venv:
	@python3 -m venv venv


.PHONY: clean
clean:
	@find . -type f -name "*.bak0" -exec rm {} +
	@find . -type f -name "indent.log" -exec rm {} +
