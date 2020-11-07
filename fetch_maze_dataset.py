#!/usr/bin/python

import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

""" This script is downloading generated maze from mazegenerator website using
selenium"""

url = "http://www.mazegenerator.net/" 
dataset_dir = "maze_dataset" # path to which mazes will be saved into
num_maze = 5 # number of maze we want to generate

if __name__ == "__main__":
    # create path if it doesnt exist
    if os.path.exists(dataset_dir) == False:
        print("Creation of directory: ", dataset_dir)
        os.mkdir(dataset_dir)

    # automatically download file in dataset directory instead of default 
    #  Note: selenium only works with absolute path, not relative path
    absolute_dataset_path = os.path.dirname(os.path.abspath(__file__)) + "\\" + dataset_dir 
    options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : absolute_dataset_path}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options = options) # initializing chrome as web browser
    driver.get(url) # opening the website

    # download the maze into the directory
    for i in range(num_maze):
        generate_button = driver.find_element_by_id("GenerateButton") # find generate button
        generate_button.click()

        # select file format as png
        file_dropdown = Select(driver.find_element_by_id("FileFormatSelectorList"))
        file_dropdown.select_by_visible_text("PNG")
        
        # download empty maze
        download_button = driver.find_element_by_id("DownloadFileButton")
        download_button.click()

        # download maze solution
        file_dropdown.select_by_visible_text("PNG (with solution)")
        download_button.click()

        """ Note: selenium doesn't allow us to change the filename, so we find
        the latest file downloaded by their download time. However, we don't
        want to sort the file everytime we download a maze"""


