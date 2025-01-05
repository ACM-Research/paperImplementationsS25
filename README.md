paperImplementationsS25
Preparing for the upcoming semester!

# Exoplanet Detection Using Neural Networks

## Motivation and Overview
Detecting and classifying exoplanets is essential for understanding planetary system formation and evolution. Furthermore, Identifying Earth-like planets within the habitable zone provides insights into the potential for extraterrestrial life.

This project uses Artificial Intelligence (AI), specifically Convolutional Neural Networks (CNNs), to classify and identify Earth-like exoplanets that could be habitable. By leveraging data from the Kepler Mission, the aim is to create a model that improves the detection of planetary candidates in large astronomical datasets. The model combines both global and local views of light curves to better detect transit events, with a focus on finding planets that might support life. The implementation is based on methods reviewed in the research paper, "A Review of Exoplanet Detection Processes Using Artificial Intelligence and Neural Networks." The paper discusses how AI and deep learning can automate and enhance exoplanet detection processes.

## Advantages, disadvantages, and nuances of the findings.
Advantages:- Automation reduces manual work and speeds up discoveries, while CNNs improve accuracy by detecting subtle transit signals that traditional methods might miss. The approach is scalable, handling large datasets like those from Kepler and TESS, and flexible enough to work with noisy or incomplete data.
Disadvantages:- The approach requires significant computational resources for training deep learning models. It does not employ transfer learning or any data augmentation to get a higher accuracy.

## The novelty and key takeaways of the method.
The novelty of this project lies in identifying better candidates for Earth-like habitable planets using data from the Kepler Mission along with developing a multi-class classification model to distinguish between exoplanet candidates, false positives, and non-candidates. The model uses dual-branch CNNs, which analyze both global views of the entire light curve and local, zoomed-in views of transit events for more accurate detection.



