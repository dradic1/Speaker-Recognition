'''
Audio file to be predicted is kept inside the predict folder.
'''

import os
import pickle
import numpy as np
from scipy.io.wavfile import read
import time
import sys
from ExtractFeature import ExtractFeature
import warnings
warnings.filterwarnings('ignore', module='sklearn')
#Used to ignore this warning:
#UserWarning: Trying to unpickle estimator GaussianMixture from version 0.20.3 
#when using version 0.21.3. This might lead to breaking code or invalid results. Use at your own risk.

def testPredict(audio_path):
    '''
    @:param audio_path : Path to the audio which needs to be predicted

    @:return: Returns the speaker thus detected by comparing to the model
    '''

    modelpath = "speakers_model/"

    ef = ExtractFeature

    # list of gmm_files available
    gmm_files = [os.path.join(modelpath, fname) for fname in
                os.listdir(modelpath) if fname.endswith('.gmm')]

    # name of the model of speaker = same as the name of speaker
    speakers = [fname.split("/")[-1].split(".gmm")[0] for fname in gmm_files]


    #list of existing models
    models   = [pickle.load(open(gmm_file,'rb')) for gmm_file in gmm_files] # rb stands for  reading the binary file


    # features of the file to be predicted
    feature = ef.extract_features(audio_path)

    score_of_individual_comparision = np.zeros(len(models))
    speaker_detected = []
    for i in range(len(models)):
        gmm = models[i]  # checking with each model one by one
        scores = np.array(gmm.score(feature))
        score_of_individual_comparision[i] = scores.sum()
    
        if np.max(score_of_individual_comparision)>-25  and np.max(score_of_individual_comparision)!=0:
            #Need to determine a threshold!
            print(np.max(score_of_individual_comparision))
            winner = np.argmax(score_of_individual_comparision)
            speaker_detected = speakers[winner]
            #print(f"Predicted speaker for {audio_path} is: {speaker_detected}")
            
        elif np.max(score_of_individual_comparision)<-25:
            print(np.max(score_of_individual_comparision))
            speaker_detected = "No matching speaker."
    

    return speaker_detected



def predict(file_name):
    '''
    @param file_name : name of the file inside the dataset/predicted to be predicted
    @return: name of the speaker predicted
    '''
    audio_path=file_name
    speaker_predicted = testPredict(audio_path)
    print(f"Predicted speaker for {file_name} is: {speaker_predicted}")
    return speaker_predicted

if __name__ == "__main__":
    predict_dir_path = 'dataset/predict/'
    dir_list = os.listdir(predict_dir_path)
    length = len(dir_list)
    for i in range (length):
        predicted =  predict(predict_dir_path+dir_list[i])
        #print(f'{i+1}. Predicted speaker for {dir_list[i]} is: {predicted}')
    


