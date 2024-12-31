#!/bin/bash

#create virtual environment
python3 -m venv ecommerce

#activate virtual environment
source ecommerce/bin/activate

#create project structure 
mkdir app
mkdir media
mkdir static
mkdir media/products
mkdir media/products/main
mkdir media/products/additional
mkdir media/categories

