.PHONY : clean install uninstall run test all

install:
	bash devtools/install.sh
	@echo Please activate the ml_starter conda environment

uninstall:
	conda remove --name ml_starter --all -y

log.log: my_experiment.py
	python my_experiment.py | tee log.log

clean:
	rm -f nosetests.xml log.log

run: log.log

all: run
