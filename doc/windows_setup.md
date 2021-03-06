# Installation under Windows 10

## Why Windows?
Well, if you have the possibility to just use Linux, work in a dual-boot configuration or have an GPU-equipped Linux server available, thats clearly 
the preferred way to work with pytorch and is currently also the preferred environment for developing deep learning solutions. Nevertheless, Windows 10 is
a big step-up for developers and users, supports multiple desktops, the Linux subsystem, and more. So if you don't want to split your hard disk space
for a dual-boot configuration or don't know Linux well, this document may be useful to you.
## Ubuntu Linux subsystem?
Windows 10 Professional (version 1709) makes it possible to activate a natively running Linux sub-system directly within Windows (Ubuntu Linux). 
Under this sub-system python and pytorch and thus the whole fastai framework (including Jupyter server etc.) may be installed and used. 

Unfortunately, it is currently not possible to utilize GPU acceleration under this environment. 
Therefore, the Linux subsystem is not recommended to be used. The training speed would in most cases be too slow for practical work.

If you still would like to use this environment, first activate the subsystem, then install Ubuntu from the store.
Then you can proceed by cloning the git repo, installing python 3.6 and then by installing all 
required Linux and python packages as normal. If you get a UTF-8 error during the PyYAML installation (required for Keras), 
you need to install that python package separately (the package is not yet adapted for Python 3.6). Before installing the PyYAML package, you need to enter a command to 
switch the current code page (enter 'chcp 1252'). After issuing that command the install should work.

## Windows Python installation (Anaconda)

The GPU-accelerated version of pytorch for Windows is currently only available as an Anaconda package. Therefore, the standard Windows python 
distribution can not be used. The pytorch package is not part the official pytorch distribution. This means, Windows is not a 
supported platform for pytorch and the package maintainer mentioned, that not the full capabilities of
pytorch are available. In my initial tests using a single GPU, I did not yet observe problems, though.

### Download Anaconda
1. Go to https://conda.io/docs/user-guide/install/windows.html and choose the Anaconda installer for Windows. 
Then choose Python 3.6 version and there 64-bit Graphical Installer. Proceed with the installation as explained on the site.

### Start Anaconda
1. Click Start and search for Anaconda Prompt, start the program.

### Create and activate Anaconda environment
Anaconda makes it possible to install packages in separated environments. This allows separation of different 
work environments, which may use different packages and versions. This documentation is based on version 5.0.1 of Anaconda.

1. Create once the new environment: 
```sh
conda create --name development
```

2. Now (and in the future before starting work) activate environment:
```sh
activate development
```

### Install python packages
After activating the environment (see last section), enter the following commands to install the development environment:

1. Install windows version of pytorch (see https://discuss.pytorch.org/t/solved-windows-anaconda-pytorch/11080) for details:
```sh
conda install -c peterjc123 pytorch cuda90
```
2. Install jupyter notebook, and helper libraries:
```sh
conda install jupyter matplotlib seaborn pillow bcolz
pip install opencv-python graphviz sklearn_pandas isoweek pandas_summary tqdm torchvision torchtext feather-format spacy scikit-image
conda install -c conda-forge ffmpeg
```
3. Enable jupyter widgets (see http://ipywidgets.readthedocs.io/en/stable/user_install.html for more details):
```sh
jupyter nbextension enable --py widgetsnbextension
```
4. Install keras and tensorflow-gpu (eventually optional step):
```sh
pip install keras tensorflow-gpu
```
If there is a problem in installing PyYAML (utf-8 related error with python 3.6), then enter the following commands to install the program independently:
```sh
chcp 1252
pip install PyYAML
chcp 65001
```
Then try to install keras and tensorflow again.

### Download fastai framework
You may utilize different approaches to download the fastai framework from GitHub. One way would be to use the command line git client using the Linux 
sub-system (see second paragraph of this page). Another quite comfortably to use variant would be to use the GUI client GitHub Desktop:
1. Download GitHub Desktop from this site: https://desktop.github.com/
2. Install and then start the program.
3. Select the menu command File/Clone repository
4. Activate the third URL-tab in the dialog
5. Enter the following URL in the dialog: https://github.com/fastai/fastai.git
   You could also clone instead this repository (https://github.com/cklukas/fastai.git). 
   That could eventually be useful at one point in the future, once there would be further adaptations or extensions.
6. Select some target folder for the local copy of the repository and then click 'Clone'.

## Start jupyter notebook for development
Under Windows, the link to the fastai library folder is not resolved after checking out the repository using conventional git commands. 
The link is shown as an file ('fastai') in the file browser (e.g. under courses/dl1). 
As a workaround, the variable PYTHONPATH needs to be set (or extended) accordingly (second command).
```sh
activate development
set PYTHONPATH=C:\Users\MY USERNAME\Documents\GitHub\fastai
jupyter notebook
```

## Additional requirements for specific lesson notebooks

### lesson1-rxt50

This lession requires the download of pre-trained model weights from the fastai webserver.
Open the Anaconda prompt and go to the fastai library folder (folder names are examples):

```sh
cd Documents\GitHub\fastai\fastai
```

Then download the weights file. If you can't execute the curl command, use your web-browser to download the file and save it in the target directory (see previous paragraph).
```sh
curl -O http://files.fast.ai/models/weights.tgz
```

If don't yet have installed 7-zip, its a good idea to download and install the flexible compression/decompression program (go to http://www.7-zip.org/download.html and download the 64-bit Windows version).
Open the windows file manager (explorer) and go to the fastai library folder. Then right-click the file weights.tgz and choose the context menu command '7-ZIP/Extract here'. Then right-click the extracted 
file weights.tar and choose the same menu item again. There will be a new sub-directory 'weights' with the according weight data for the various models.


### lesson3-rossmann

Don't just download the datasets from the kaggle website, additional files are required as explained in the notebook itself.

## Results of testing the notebooks
### Lesson 1 (3 variants) (Jan 7, 2018)
* Work after adaption of learn.TTA result processing and adaptations of shell script calls.
* Long / float tensor format errors are fixed by adding conversion code in model.py class Stepper.

### Lesson 2 (Jan 8, 2018)
* The same fixes as for lesson 1 were needed.
* In addition the f2 calculation was not working, changed by supplying log-prob values instead of probabilities to the function.

### Lesson 3 (Jan 8, 2018)
* Does not currently work in my test. Columns 'BeforeSchoolHoliday', 'AfterStateHoliday', 'BeforeStateHoliday' are not calculated correctly.

### Lesson 4 (Jan 8, 2018)
* I get the following warning: "Warning: no model found for 'en' Only loading the 'en' tokenizer."
* Script calls are partially adapted to work also for Windows. Word count calculation shell commands not yet converted to be portable.
* Some of the imdb text files can't be opened in default encoding (ISO-8859-1=Latin 1). Also utf8 does not work for these files. 
  To prevent these errors, the default error handling in this notebook for codec errors is set in the beginning of the
  workbook to ignore such errors.  The error otherwise would appear in nlp.py (where it could be fixed probably by setting 
  to ignore the error in some system call), but later in the sentiment analysis section the error appears from the external package.

### Lesson 5 (Jan 9, 2018)
* Error: torch.index_select received an invalid combination of arguments - got (torch.cuda.FloatTensor, int, torch.cuda.IntTensor), but expected (torch.cuda.FloatTensor source, int dim, torch.cuda.LongTensor index)
* Notebook does not yet work...

### Lesson 6 (Jan 10, 2018)
* Added long-cast in Char3Model, CharLoopModel and CharLoopConcatModel models, to prevent Int/Long tensor error.
  Fix indexing problem (from https://github.com/hiromis/fastai/commit/131e230dd915b0998b8afe9603a183c001422da8#diff-24cf862482118c2f3e52f9d4234825ac)
  
### Lesson 6 SGD
* Use torch clamp instead of np.clip to avoid boolean/byte tensor error
* Print exp(log_loss) in SGD example
* Added ffmpeg install note (using conda)

### cifar10 (Jan 10, 2018)
* Added method to move input files into sub-folders.
* Fixed processing TTA results so that accuracy can be calculated.
* Convert some model results to long-vectors, so that there is no Int / Long
  mismatch tensor error.