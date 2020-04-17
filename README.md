# ml_jenkins_starter
A Starter Repository for ML Team Experimentation

## Getting Started
1. Branch off of this repo
2. Copy the Template Job naming it what you want.
3. On Jenkins Change the "Branch Specifier" to your branch.

When run the jenkins job it will run `my_experiment.py` with the python environment described in `devtools/requirements.json`

### Interesting Settings
#### Build Triggers
By default this will run every day unless you remove "Build Periodically".

"Poll SCM" is a good choice if you want automatic builds on every push.

#### Post-build Actions
You can select "Archive Artifacts".
Here you can select outputs of your experiment to save for posterity.
File paths are relative to the git root.
