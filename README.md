# BoMBR_dataset_preprocessing
# Research Code for Image Annotation and Dataset Conversion

This repository contains code used for the research paper titled **[Your Paper Title]**. The code includes tools for converting images to annotations and for converting Pascal VOC datasets to an integer-encoded format.

## Files

1. `1_Images_to_Annotations_using_SAM.ipynb`: Jupyter notebook for converting images to annotations using the SAM method.
2. `2_Pascal_to_Integer_Encoded_Dataset.py`: Python script for converting Pascal VOC datasets to an integer-encoded format.

## Installation

1. Clone the repository:
   git clone https://github.com/AI-in-Medicine-IIT-Ropar/BoMBR_dataset_preprocessing.git

2. cd BoMBR_dataset_preprocessing

# Usage
## Converting Images to Annotations
1. Open the Jupyter notebook 1_Images_to_Annotations_using_SAM.ipynb in your preferred environment (e.g., Jupyter Lab, Jupyter Notebook).
2. Follow the instructions within the notebook to convert your images to annotations using the SAM method.
 
# Converting Pascal VOC to Integer-Encoded Dataset
1. Open the 2_Pascal_to_Integer_Encoded_Dataset.py file.
2. Set the paths for the segmentation class of the Pascal VOC dataset, the original images, and the output directory within the script.
3. Run the script
4. The script will convert the Pascal VOC dataset to an integer-encoded format and save it in `finalCompletedir`.


