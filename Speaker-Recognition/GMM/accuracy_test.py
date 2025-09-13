from GetFiles import GetFiles
import predict as pred
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

def getActualPredictedList():
    '''
    @return pd.DataFrame : list of the actual and predicted list for confusion matrix calculation
    '''
    data_frame_row = []
    
    gf = GetFiles(dataset_path="dataset")
    testing_files = gf.getTestFiles()

    for index, row in testing_files.iterrows():
        audio_path = row["audio_path"]
        predicted = pred.testPredict(audio_path)
        actual = row["actual"]
        data_frame_row.append([actual, predicted])

    # Alphabetic sorting by column 'actual' without affecting the predicted column
    actual_predicted = pd.DataFrame(data_frame_row, columns=['actual', 'predicted']).sort_values(by='actual')
    return actual_predicted

def showAccuracyPlotAndMeasure():
    actual_pred = getActualPredictedList()
    actual = actual_pred["actual"].tolist()
    predicted = actual_pred["predicted"].tolist()
    
    # Ensure we have all unique labels from both actual and predicted
    unique_labels = sorted(list(set(actual + predicted)))
    
    # Compute confusion matrix
    cm = confusion_matrix(actual, predicted, labels=unique_labels)
    
    # Display numeric accuracy
    display_numeric_accuracy(actual, predicted, unique_labels)
    
    # Plot confusion matrix
    fig, ax = plt.subplots()
    cax = ax.matshow(cm)
    plt.title('Confusion matrix of Recognition Model')
    fig.colorbar(cax)
    
    # Set x and y axis labels
    ax.set_xticks(range(len(unique_labels)))
    ax.set_yticks(range(len(unique_labels)))
    ax.set_xticklabels(unique_labels, rotation=90)
    ax.set_yticklabels(unique_labels)
    bottom, top = ax.get_ylim()

    ax.set_ylim(bottom+0.5, top-0.5) # set the ylim to bottom, top)
    
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()

def display_numeric_accuracy(actual, predicted, labels):
    '''
    @param list actual : actual label for the speaker's audio
    @param list predicted : predicted label by the GMM classifier
    @param list labels : name of the distinct speaker
    '''
    print("\n")
    print(classification_report(actual, predicted, labels=labels))

showAccuracyPlotAndMeasure()

