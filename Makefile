.PHONY : clean run install uninstall

install:
	bash devtools/install.sh
	@echo Please activate the ml_starter conda environment

uninstall:
	conda remove --name ml_starter --all -y

nosetests.xml: test_all.py
	nosetests test_all.py --with-xunit

log.log: my_experiment.py
	python my_experiment.py | tee log.log

clean:
	rm -f nosetests.xml
	rm -f log.log

run: nosetests.xml log.log

