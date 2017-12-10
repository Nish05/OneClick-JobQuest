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
meteor npm install --save html5sortable
meteor npm install --save babel-runtime
meteor npm install --save core-js
meteor npm install --save bcrypt
meteor add session
meteor remove autopublish
meteor
```
### Installations - Load Data 
Load data into meteor mongo with :
Run the files in the Python_Script directory with :
```
$ python WebScraper_3.py (destination_filename) testData.xls
$ python ResumeParser.py (resume directory)
$ python ResumeCleaner.py
$ python IntersectionResumePosting.py
$ python Stable-Matching-Jobs-Resume.py
```

## Built With

* [MeteorJS](http://docs.meteor.com/#/full/) - The web framework used
* [Jupyter Notebooks](http://jupyter.org/) - Data Management

## Authors

* **Nisha Bhanushali** - *Initial work* - [Nish05](https://github.com/Nish05)

## Acknowledgments

* Prof. Christopher M. Homan (Rochester Institute of Technology)

