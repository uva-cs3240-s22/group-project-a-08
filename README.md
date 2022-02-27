# Word of Mouth
**Table of Contents**
1. [Getting started](#getting-started)
	1. [Installation](#installation)
	1. [Setup](#setup)
1. [Contributing](#contributing)
	1. [Branch structure](#branch-structure)
	1. [Deployment structure](#deployment-structure)

## Getting started
This project is built off of
- Django
- PostgreSql

See installaion and setup information before contributing

### Installation
Empty for now..

### Setup
Empty for now..

## Contributing
### Branch structure
The following tier branch structure shall exist for the duration of the project
1. main
	- This is the main branch 
	- **Never directly commit to this branch**
		- Instead commit to a lower tier branch
1. testing
	- This is the branch where new features are to be tested via heroku
	- For more infomation regarding the heroku deployment structure, please visit the deployment section
1. push
	- This is a catch-all term for any new pushes made by contributors
	- Naming convention should go as follows `<description>-<FIX/bug>-<name>`, see bullet points below
    	- description
			- This should be a brief name for why your branch exists in the first place
    	- bug/fix
			- This is a term that switches between bug or fix, see descriptions below
			- bug
				- Add this if there is a bug that you are fixing in this commit
					- If this is an [known issue](https://github.com/uva-cs3240-s22/group-project-a-08/issues), do not add this tag
			- fix
				- Add this if there is a particularly [known issue](https://github.com/uva-cs3240-s22/group-project-a-08/issues) that you are fixing
				- Be sure to add the issue number that this commit corresponds to
				- This tag supersedes bug if the bug, do not add both to the branch name

**Ideally, the flow of commits should go as follows**
- code is push to a tier 3 branch
- a pull request is created to merge from the tier 3 branch to the testing branch
- after testing, a pull request should to created to merge from the testing branch to the main branch

The reason for this is mainly due to the nature in which the repo is deployed.
See details in deployment structure for more infomation.

### Deployment structure
This project already has an associated heroku team which oversees all environments that are plugged in
Throughout the project there will be two environments plugged into the repo
1. [Production](uva-cs3240s22a08-word-of-mouth)
	- This is where all final changes are to be demonstrated
	- Builds from the main branch
1. [Testing](https://uva-cs3240s22-womt.herokuapp.com/)
	- All new features will be tested here before making their way to production
	- Builds from the testing branch