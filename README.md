# Cancer-Detection-model
End-to-end machine learning project for breast cancer classification. Includes data preprocessing, exploratory data analysis, and model evaluation using various classification algorithms such as Logistic Regression, Decision Trees, Random Forest, SVM, KNN, and more to determine the best-performing model.

After training multiple classification algorithms, we evaluate their performance using accuracy and confusion matrices.

## What is Confusion Matrix and what does it mean

| Actual \ Predicted | Benign (2) | Malignant (4) |
|-------------------|------------|---------------|
| Benign (2)        | 102        | 5             |
| Malignant (4)     | 5          | 59            |

### Interpretation:

True Negatives (TN = 102): Correctly predicted benign samples

False Positives (FP = 5): Benign samples incorrectly predicted as malignant

False Negatives (FN = 5): Malignant samples incorrectly predicted as benign

True Positives (TP = 59): Correctly predicted malignant samples

# Results

## Logistic Regression
![image (1)](https://github.com/user-attachments/assets/7642d297-de86-4b29-b69f-65ea6ab46b13)

## K nearest Neighbors
#### Accuracy Score: 94.73%
<img width="527" height="400" alt="image" src="https://github.com/user-attachments/assets/031fbd22-1d0e-4c07-87f3-2263dff50c7c" />


## Kernel SVM
#### Accuracy Score: 95.32%
<img width="605" height="409" alt="image" src="https://github.com/user-attachments/assets/af49ed5f-ae7a-4ff6-9100-518d6668c2a7" />


## Naive Bayes
#### Accuracy Score: 94.15%
<img width="511" height="405" alt="image" src="https://github.com/user-attachments/assets/fc4274d6-1a4a-413d-8f3c-11e35e630d6a" />


## Decision Tree Regression
#### Accuracy Score: 95.90%
<img width="519" height="404" alt="image" src="https://github.com/user-attachments/assets/9f047aa8-14dd-443f-9d00-ef9600a04887" />

## Random Forest Classification
#### Accuracy Score: 93.56%
<img width="528" height="408" alt="image" src="https://github.com/user-attachments/assets/6fb4524d-b912-4268-a821-b274d16c7bd4" />


## Support Vector Machine
#### Accuracy Score: 94.15%
<img width="516" height="410" alt="image" src="https://github.com/user-attachments/assets/0a96d7be-7590-41fa-a231-217c3feb401a" />

