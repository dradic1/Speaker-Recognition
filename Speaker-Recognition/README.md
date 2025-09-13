# Speaker Recognition  

This project is a **continuation and extension of the work** originally done by [Atul-Anand-Jha](https://github.com/Atul-Anand-Jha/Speaker-Identification-Python) in the implementation of MFCC (Mel-Frequency Cepstral Coefficient) and GMM (Gaussian Mixture Model).  

As part of our **faculty project**, we used a portion of the original codebase and adapted it to create our own solution.  
The project was developed for the course **Multimedia Systems** at the *Faculty of Electrical Engineering, Computer Science and Information Technology Osijek (FERIT)*.  

---

## 1. Algorithmic Details:
In the feature extraction, MFCC (Mel-Frequency Cepstral Coefficients) are used, which emphasize the extraction of the low-frequency components and their cepstral coefficients from the audio files. The procedure for feature extraction is illustrated in the figure below:

### a. Feature Extraction
![MFCC Feature Extraction Procedure](https://www.researchgate.net/profile/Ratnadeep_Deshmukh/publication/262794354/figure/fig1/AS:296064092524547@1447598588547/MFCC-Feature-Extraction.png)

Basically, the frequency is calculated at the frame level by using the windowing technique, and each frame of audio is converted into the frequency domain representation using the Discrete Fourier Transform. From those frequencies, mel’s cepstral coefficient (MCC) is calculated, which is then converted into a logarithmic scale representation and finally back into the time domain representation using the inverse Fourier transform. The overall process of calculating an MFCC feature is performed in the frequency domain.

### b. Model Representation using Gaussian Mixture Model (GMM)
To represent the model of each speaker, GMM is used. This technique relies on generalizing the Gaussians that arise from the features extracted from the audio files of a particular speaker during the training phase.

![Gaussian Mixture Model Generalizing the individual Gaussians present in the feature array.](https://prateekvjoshi.files.wordpress.com/2013/06/multimodal.jpg)

The dotted line above can be inferred as the features present in each speaker’s audio file, while the solid line represents the generalized Gaussian in the feature space.  

---
