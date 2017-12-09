# OneClick-JobQuest
We have built an efficient system for the job-seekers where job recommendation is based on their resume.

### Prerequisites
```
Install python 3 or anaconda python 3
Required python packages : pymongo, pyPDF2, nltk, re, scipy and
```

### Installations - Meteor Application

Install Meteor with :

```
curl https://install.meteor.com/ | sh
```

Clone the application with :

```
git clone https://github.com/Nish05/OneClick-JobQuest
```
Setup Meteor with :

Change your current directory to meteor application directory
```
nohup meteor --port 8080 &
meteor add session
meteor add themeteorchef:html5-sortable
meteor remove autopublish
```
### Installations - Load Data 
Load data into meteor mongo with :

```
$ iPython
$ %run WebScraper_3.ipynb
$ %run Resume_Parser.ipynb
$ %run Resume_Cleaner.ipynb
$ %run IntersectionResumePosting.ipynb
$ %run Stable-Matching-Jobs-Resume.ipynb
```

## Built With

* [MeteorJS](http://docs.meteor.com/#/full/) - The web framework used
* [Jupyter Notebooks](http://jupyter.org/) - Data Management

## Authors

* **Nisha Bhanushali** - *Initial work* - [Nish05](https://github.com/Nish05)

## Acknowledgments

* Prof. Christopher M. Homan (Rochester Institute of Technology)

