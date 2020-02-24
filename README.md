[![License](https://img.shields.io/badge/License-GPL%203.0-brightgreen.svg)](./LICENSE)
![GitHub stars](https://img.shields.io/github/stars/stocksmith/ml-research.svg)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/stocksmith/ml-research.svg?color=red)

# Machine Learning Research

<div><p align="center">
<center><h4>Meetsync is supported by:</h4><a href="https://umass.acm.org/"><img width="300" src="assets/acm_umass.jpg" target="_blank"></a>
<a href="https://umassdsc.com/" target="_blank"><img width="300" src="assets/dsc_umass.jpg"></a>
<!-- <img width="250" src="assets/acm_umass.jpg"> -->
</center></p></div>

An analysis of historic stock datasets and building a machine learning algorithm to predict stock behavior. 

## Project Structure 

**database-agg/**

Scripts to add data to database with proper time and json formatting, has firebase scripts that will add data directly to firestore.

**datasets/**

The collection of datasets we are using for sample analysis.

**r-analysis/**

Multiple R files with a reference inital markdown and inital .docx files to generate reports as well as understand how to analyze large CSVs with R. 

**real-time-data/**

Python API that uses Yahoo Finance API to get real time stock data. viz.py has plotting peaks of stocks over max 1 year. The folder also includes Go scripts for real time finance data scraping. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

* Python 3.6.9 or above with pip3
* Jupyter Notebook

### Installing

For Mac OS/Linux users:
```
git clone https://github.com/stocksmith/ml-research.git

sudo bash setup.sh
```

For windows users:
```
https://github.com/stocksmith/ml-research.git

setup.bat
```

## Built With

* [Jupyter](https://jupyter.org/) - Prototyping with Python
<!-- 
## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us. -->


<!-- 
## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
 -->
