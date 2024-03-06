# nightguard-thermal_human_presence_detection

## Overview

Nightguard is a project aimed at developing a robust system for detecting human presence in low light conditions using thermal images. This project utilizes the YOLOv8 object detection architecture trained on custom thermal image datasets to create an efficient nightguard system. Once trained, the model is then used to detect human presence from sample thermal imaging footage.

## Project Structure

The project is organized into the following main components:

1. **Dataset Collection and Preprocessing**: Thermal image datasets are collected and preprocessed to prepare them for training the YOLOv8 model.

2. **Training YOLOv8**: The YOLOv8 architecture is customized and trained on the collected thermal image dataset to accurately detect human presence in low light conditions.

3. **Model Evaluation**: The trained model's performance is evaluated using various metrics to ensure its effectiveness in detecting human presence.

4. **Deployment**: The trained model is deployed to create the Nightguard system, which has the ability to take real-time thermal imaging feeds for human presence detection in low-light conditions.

## Dataset

The dataset used for training the YOLOv8 model consists of thermal images captured in low light conditions. The dataset includes images with annotated bounding boxes around human subjects to facilitate supervised training. You can access dataset from [here](https://www.kaggle.com/datasets/niteshc7r/datasets-for-object-detection-night-and-thermal).

## Training

The YOLOv8 model is trained using the collected thermal image dataset. Training involves optimizing the model's parameters to minimize detection loss and improve its ability to accurately detect human presence in low-light conditions. The model was trained for 10 epochs with a batch size of 30. You can access model training source code from [here](https://github.com/umairsiddique3171/nightguard-thermal_human_presence_detection/tree/main/custom_yolov8).

## Model Evaluation

The trained YOLOv8 model achieved precision, recall, and mAP of 0.924, 0.929, and 0.977, respectively, on 95 validation images with 438 instances. Model speed per frame is given as : 
- 0.7ms **preprocess**
- 18.0ms **inference**
- 0.0ms **loss**
- 1.8ms **postprocess**

## Sample Video Detection

Once trained and evaluated, the model is used to detect human presence from sample thermal imaging footage. You can access the results from [here](https://github.com/umairsiddique3171/nightguard-thermal_human_presence_detection/blob/main/results.mp4). 


## Conclusion

Nightguard demonstrates the effectiveness of using custom-trained YOLOv8 models for human presence detection in low light conditions. By leveraging thermal imaging technology and deep learning techniques, Nightguard offers a reliable solution for enhancing security and surveillance in low light environments.


## License 
This project is licensed under the [MIT License](https://github.com/umairsiddique3171/nightguard-thermal_human_presence_detection/blob/main/LICENSE).

## Author 
[@umairsiddique3171](https://github.com/umairsiddique3171)


