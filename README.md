 # Sports Analytics Project

Welcome to the Sports Analytics project repository! This repository contains tools and scripts for analyzing soccer matches, particularly focusing on the FIFA World Cup tournaments from 1930 to 2018, with fixtures included for the 2022 Qatar World Cup. The project involves data collection, preparation, and modeling using statistical methods, particularly Poisson distribution, to predict match outcomes.

## Table of Contents

- [Introduction](#introduction)
- [Folder Structure](#folder-structure)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Sports analytics has become an essential part of understanding and predicting outcomes in various sports, including soccer. This project focuses on analyzing FIFA World Cup matches using historical data and statistical modeling techniques. The primary objectives include data collection, data preparation, and predictive modeling to forecast match results.

## Folder Structure

- **01_data_collect**: Contains scripts and data related to the collection of FIFA World Cup match data from 1930 to 2018, as well as fixtures for the 2022 Qatar World Cup.
  
- **02_prepare_data**: Includes scripts for cleaning and preprocessing the collected data to make it suitable for modeling.

- **03_EDA**: This folder can be added for exploratory data analysis if you decide to analyze the data before modeling.

- **04_model**: Contains scripts and models utilizing Poisson distribution to predict match outcomes based on historical data. Models are generated for each stage of the FIFA World Cup tournament.

## Usage

To use this repository:

1. Clone the repository to your local machine.
2. Navigate to the respective folders (`01_data_collect`, `02_prepare_data`, `04_model`).
3. Follow the instructions in each folder's README file to execute the scripts and utilize the tools.

## Dependencies

The project relies on the following dependencies:

- Python 3.x
- Libraries such as Pandas, NumPy, and Scipy for data manipulation and modeling.

To install the dependencies, please follow these steps:

1. Navigate to the root directory of the project where the `requirements.txt` file is located.
2. Run the following command in your terminal or command prompt:

pip install -r requirements.txt

This command will install all the required Python libraries listed in the requirements.txt file. Make sure you have Python and pip installed on your system before executing this command.