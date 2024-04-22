.PHONY: set-env
set-env:
	@tlmgr conf texmf $(KEY) $(VALUE)
	@echo '\CatchFileEdef{\\var$(KEY)}{|"kpsewhich -var-value=$(KEY)"}{\\endlinechar=-1 }' >> ./src/styles/env.sty

.PHONY: clean
clean:
	@rm -rf ./**/dist/

.PHONY: venv
venv:
	@python3 -m venv venv
