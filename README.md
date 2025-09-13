# Speaker Recognition  

This project is a **continuation and extension of the work** originally done by [Atul-Anand-Jha](https://github.com/Atul-Anand-Jha/Speaker-Identification-Python) in the implementation of MFCC (Mel-Frequency Cepstral Coefficient) and GMM (Gaussian Mixture Model).  

As part of our **faculty project**, we used a portion of the original codebase and adapted it to create our own solution.  
The project was developed for the course **Multimedia Systems** at the *Faculty of Electrical Engineering, Computer Science and Information Technology Osijek (FERIT)*.  

---

## 1. Project Description  
In the initial stage, we analyzed at least two existing algorithms for speaker recognition based on audio recordings of speech.  

The task was then to design and implement a computer algorithm for **student attendance registration** during classes, based on audio recordings captured at the entrance of the lecture hall. Each student entering the classroom pronounces the name of the course they are attending.  

At the entrance, an audio recording is made for every individual entering, with each recording not exceeding one minute. A total of **10 different audio signals** of students entering are recorded, in varying orders of entry. In total, 10 students should be registered for attendance, but not all will appear in every recording. Additionally, some recordings may include voices of individuals who are **not among the 10 students** to be registered.  

By comparing the entrance recordings with the student database of audio samples, the algorithm assigns a **“+” mark** for attendance each time it recognizes a student.  

The algorithm must handle three cases:  
- Correctly recognizing a student  
- Misidentifying a student  
- Failing to recognize a student (reporting that the person is not in the database)  

---

## 2. Algorithmic Details:
In the feature extraction, MFCC (Mel-Frequency Cepstral Coefficients) are used, which emphasize the extraction of the low-frequency components and their cepstral coefficients from the audio files. The procedure for feature extraction is illustrated in the figure below:

### a. Feature Extraction
![MFCC Feature Extraction Procedure](https://www.researchgate.net/profile/Ratnadeep_Deshmukh/publication/262794354/figure/fig1/AS:296064092524547@1447598588547/MFCC-Feature-Extraction.png)

The frequency is calculated at the frame level using a windowing technique, and each frame of audio is converted into the frequency domain representation with the Discrete Fourier Transform. From those frequencies, the mel cepstral coefficients (MCC) are calculated, converted into a logarithmic scale, and then transformed back into the time domain using the inverse Fourier transform. The entire MFCC feature extraction process takes place in the frequency domain.

### b. Model Representation using Gaussian Mixture Model (GMM)
To represent each speaker, a GMM is used. This technique relies on generalizing the Gaussians that arise from the extracted features of each speaker’s audio files during training.

![Gaussian Mixture Model Generalizing the individual Gaussians present in the feature array.](https://prateekvjoshi.files.wordpress.com/2013/06/multimodal.jpg)

The dotted line above represents the features present in each speaker’s audio file, while the solid line represents the generalized Gaussian distribution in the feature space.  

---
