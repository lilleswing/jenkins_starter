.PHONY : clean run install uninstall

install:
	bash devtools/install.sh
	@echo Please activate the ml_starter conda environment

uninstall:
	conda remove --name ml_starter --all -y

clean:
	rm -f nosetests.xml

run:
	nosetests test_all.py --with-xunit
	python my_experiment.py

