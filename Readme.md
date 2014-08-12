#gspread_d3_network_graph
This is a very simple [flask app][1].  It exists to do one thing, pull data from a google spreadsheet and display it as a network graph using [D3.js][2].  To do this, it relies heavily on the [gspread library][3].

A `requirements.txt`file is included for setting up your python virtual environment, which by default assumes you are using your system python2.7.  See `config/wsgi.py` for more assumptions about the larger project structure.  If you are unfamiliar with [pip][4] and [virtualenv][5] here is a [good blog post][6] to get you started.

For security, all variables are kept in a separate file *which should never be checked into the repository.*  Instead you have a dummy file, `fake_variables.py`. Fill in the relevant values, and change the filename to `variables.py` before running the code.

There is also a `test-data folder` included in the root of the project with two files, `Test-Nodes.csv` and `Test-Edges.csv` that describe a mini social network dataset based on the family and friends of John and Abigail Adams. See `fake_variables.py` for suggested file names for your test spreadsheet.

If you want to run this on a live server, I *strongly* suggest looking into encrypting your password file, or setting up a separate google account just for your project.


  [1]: http://flask.pocoo.org/
  [2]: http://d3js.org
  [3]: https://github.com/burnash/gspread
  [4]: https://pypi.python.org/pypi/pip
  [5]: http://virtualenv.readthedocs.org/en/latest/
  [6]: http://www.jontourage.com/2011/02/09/virtualenv-pip-basics/