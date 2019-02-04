ENV = asp

.PHONY: init clean

init:
	conda env create -f environment.yml
	. activate $(ENV) && pip install -e .


clean:
	. deactivate && conda remove --yes -n $(ENV) --all	
