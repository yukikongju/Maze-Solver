#!/usr/bin/python

import time
import os
from selenium import webdriver

""" This script is downloading generated maze from mazegenerator website using
selenium"""

url = "http://www.mazegenerator.net/" 
dataset_dir = "maze_dataset" # path to which mazes will be saved into
num_maze = 10 # number of maze we want to generate

if __name__ == "__main__":
    # create path if it doesnt exist
    if os.path.exists(dataset_dir) == False:
        print("Creation of directory: ", dataset_dir)
        os.mkdir(dataset_dir)

    # set download path to chosen directory
    absolute_dataset_path = os.path.dirname(os.path.abspath(__file__)) + "\\" + dataset_dir 
    #  print(dir_name)
    options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : absolute_dataset_path}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options = options) # initializing chrome as web browser
    driver.get(url) # opening the website

    # download the maze into the directory
    for i in range(num_maze):
        generate_button = driver.find_element_by_id("GenerateButton") # find generate button
        generate_button.click()
        download_button = driver.find_element_by_id("DownloadFileButton")
        download_button.click()







