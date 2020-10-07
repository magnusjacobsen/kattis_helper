import sys
import os
from io import BytesIO
from zipfile import ZipFile
import requests, zipfile, io

#
# Kattis helper (for open.kattis.com problems)
# By Frank Andersen (2020)
# Git: https://github.com/dkfrankandersen
# 
# How and why:
# Solving Kattis problems is a fun task, but it can be a cucumbersome task to prepare for a problem.
# So here is a small scripts that given an url of a kattis problem:
# - Creates a folder with the name of the problem
# - Creates a readme.md (for git mostly, with name and url)
# - Downloads the sample data and extracts into /sample-data
# - Creates a file, with standard content for solving the task, eg. for now python (solver.py)
#
# Requirements:
# - Python3.5 (test with 3.8)
# - pip install requests
#   

def make_dir(dir_name):
    # path = os.getcwd()
    try:
        os.mkdir(f"{dir_name}")
    except OSError:
        print ("Creation of the directory %s failed" % dir_name)
        return False
    else:
        print ("Successfully created the directory %s " % dir_name)
        return True

def create_readme_file(problem_id, problem_url):
    f = open(f"{problem_id}/readme.md", "x")
    f.write(f"Readme for Kattis problem {problem_id}\nProblem url: {problem_url}")
    f.close()

def download_samples(problem_id, problem_url):
    zip_url = f"{problem_url}/file/statement/samples.zip"
    print(f"Downloading sample data for {problem_id} at {zip_url}")
    sample_dir = f"{problem_id}/sample-data"
    if(make_dir(sample_dir)):
        print(f"Extracting to: {sample_dir}")
        r = requests.get(zip_url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(sample_dir)

def list_sample_files(problem_id):
    list_of_filenames = []
    for entry in os.scandir(f"{problem_id}/sample-data"):
        if entry.is_file():
            list_of_filenames.append(entry.name)
            print(entry.name)
    return list_of_filenames

def create_solution_file(problem_id, problem_url, list_of_samples):
    filename = "solver.rs"
    print(f"Creating solution file: {problem_id}/{filename}")
    f = open(f"{problem_id}/{filename}", "x")
    f.write(f"// Solution for Kattis problem: {problem_id}\n// Problem url: {problem_url}\n\n// Sample-data\n")
    for filename in list_of_samples:
        f.write(f"// * {filename}\n")

    f.write("\nuse std::io::{self, BufRead};\n")
    f.write("use std::str::FromStr;\n\n")
    f.write("fn main() {\n")
    f.write("  let stdin = io::stdin();\n")
    f.write("  let mut iter = stdin.lock().lines();\n")
    f.write("}")
    f.close()

def main():
    if len(sys.argv) > 1:
        problem_url = sys.argv[1].strip()
        print(problem_url)
        url_parts = problem_url.split("/")
        problem_id = url_parts[len(url_parts)-1]
        print(problem_id)

        if (make_dir(problem_id)):
            create_readme_file(problem_id, problem_url)
            download_samples(problem_id, problem_url)
            list_of_samples = list_sample_files(problem_id)
            create_solution_file(problem_id, problem_url, list_of_samples)
    else:
        print("Wrong arguments...")

if __name__ == "__main__":
    main()
