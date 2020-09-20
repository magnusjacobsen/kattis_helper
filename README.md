# kattis_helper
A small Python3 script for enabling a faster local setup for working with problems from open.kattis.com

# Kattis helper (for open.kattis.com problems)
 By Frank Andersen (2020)
 Git: https://github.com/dkfrankandersen
 
# Why:
 Solving Kattis problems is a fun task, but it can be a cucumbersome task to prepare for a problem.
 So here is a small scripts that given an url of a kattis problem:
 - Creates a folder with the name of the problem
 - Creates a readme.md (for git mostly, with name and url)
 - Downloads the sample data and extracts into /sample-data
 - Creates a file, with standard content for solving the task, eg. for now python (solver.py)
 - a small video https://gyazo.com/c3362741db8acd10e7d106fbdd25c45a
 
 # How
 In your terminal run, were the argument is the url of a open.kattis.com problem:
 *python3 kattis_helper.py https://open.kattis.com/problems/listgame*
 
# Requirements:
 - Python3.5 (test with 3.8)
 - pip install requests   
