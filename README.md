# Is it bin night?

<q>When is the next recycling day you ask?</q>

<q>This coming Tuesday</q>

# How to run

Grab a copy of the `rday.py` script and edit the following variable to 
suit your own street, using the last date you know your street had your
recycling bins collected:

```python
last_known_recycling_day = datetime.date(2018,4,10)
# Adjust the above value as necessary for your street
# (the format is year, month, day)
```

then run it with:

`python rday.py`

or modify your ~/.bashrc file to include a line like this:

```
alias isitbinnight='python /path/to/rday.py'
```

so that in future you can just type:

`isitbinnight`

example output:
```
When is the next recycling day you ask?
Tomorrow
```