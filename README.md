Dataset Description:
The MUSAN dataset is a comprehensive collection of labeled audio files designed for speech, music, and noise classification tasks. Created to support various audio classification and speech processing projects, MUSAN includes diverse audio content suitable for real-world applications such as voice activity detection (VAD), speech enhancement, and environmental sound classification. The dataset is structured into three main categories: Speech, Music, and Noise, each containing different sources and types of audio that add variability and depth to the dataset, making it robust for training and evaluation in machine learning projects.

The MUSAN dataset, with its structured organization, high-quality audio, and well-labeled categories, serves as an ideal resource for developing models in audio classification tasks, ensuring reliability and performance across diverse applications.



Experimental Procedure (or Methodology):
In this section, describe each step of your experimentation as a sequence of actions taken to achieve the final optimized model. Each step should include:

Step 1: Initial Training Using an SVM Model (Non-Random Split 80-20)

Objective: To establish a baseline performance using the SVM model with an RBF kernel and default feature extraction settings.
Configuration:
Data Split: 80% of the dataset was used for training, and 20% for testing.
Feature Extraction: MFCCs were used with a window size of 2048 samples and hop length of 512 samples.
Results:
Accuracy: 0.96
F1 Score: 0.90
Observation: This initial training served as a reference for further optimization.

Step 2: Adding a Validation Split (80-10-10 Random Split)

Objective: To add a validation set for evaluating the model more comprehensively and reduce overfitting risks.
Configuration:
Data Split: The dataset was split into 80% training, 10% validation, and 10% test set in a randomized manner.
Results:
Validation Accuracy: 0.97
Validation F1 Score: 0.93
Test Accuracy: 0.95
Test F1 Score: 0.86
Observation: The validation results indicated the model was slightly overfitting, prompting further adjustments.

Step 3: Filtering the Dataset

Objective: To test if denoising the dataset can improve model accuracy.
Configuration: Aggressive spectral gating was applied to filter out noise before training.
Results:
Accuracy: 0.93
F1 Score: 0.81
Observation: The denoising process negatively impacted accuracy, likely due to the loss of relevant frequency components. This approach was therefore abandoned.

Step 4: Comparing with Hidden Markov Model (HMM)

Objective: To compare the SVM's performance with an HMM for classification purposes.
Results:
HMM Accuracy: 0.70
HMM F1 Score: 0.58
Observation: The HMM underperformed compared to SVM, confirming that SVM was the more suitable choice for this data.

Step 5: Applying t-Test Before and After Training

Objective: To evaluate the statistical significance of the feature distribution before and after training.
Procedure:
Before Training: A t-test was performed to compare the feature distributions between training and testing sets.
After Training: A t-test was performed to compare predicted labels against actual labels.
Results:
Pre-Training t-Test: t-statistic = -2.79, p-value = 5.48e-03
Post-Training t-Test: t-statistic = 0.73, p-value = 4.68e-01

Step 6: Applying PCA

Objective: To reduce feature dimensionality and possibly improve training efficiency.
Configuration: Principal Component Analysis (PCA) was applied to the dataset.
Results:
Accuracy: 0.95
F1 Score: 0.88
Observation: PCA slightly reduced accuracy, indicating that the removed features may have contained some useful information.

Step 7: Adding Zero Crossing Rate (ZCR) to MFCC Features

Objective: To enhance the model's ability to differentiate between speech and non-speech using ZCR in combination with MFCC.
Results:
Accuracy: 0.96
F1 Score: 0.91
Observation: Adding ZCR slightly improved the F1 score, indicating it provided complementary information to MFCC.

Step 8: Modifying Window and Hop Length (20 ms and 10 ms, respectively)

Objective: To apply more commonly accepted standard settings for window size and hop length in speech processing.
Results:
Accuracy: 0.97
F1 Score: 0.91
Observation: The standard settings for window and hop length further improved model accuracy.

Step 9: Combined Optimizations for Final Evaluation (Non-Random Split 80/20)

Objective: To evaluate the model performance after applying all of the best optimizations together.
Features Used: MFCC + ZCR with window size of 20 ms and hop length of 10 ms.
Results:
Pre-Training t-Test: t-statistic = -3.07, p-value = 2.32e-03
Accuracy: 0.97
F1 Score: 0.91
Post-Training t-Test: t-statistic = 1.07, p-value = 2.86e-01

Step 10: Combined Optimizations for Final Evaluation (Random Split 80/10/10)

Objective: To evaluate the optimized model on the random split dataset.
Results:
Pre-Training t-Test: t-statistic = 2.01, p-value = 4.65e-02
Accuracy: 0.99
F1 Score: 0.97
Post-Training t-Test: t-statistic = 0.00, p-value = 1.00e+00
Observation: This was the best-performing setup with a nearly perfect accuracy and F1 score.

Step 11: K-fold Cross-Validation (5-fold)

Objective: To evaluate the robustness of the final model using cross-validation.
Results:
Cross-Validation Accuracy Scores: [0.86, 0.88, 0.99, 0.93, 0.97]
Mean Accuracy: 0.93
Cross-Validation F1 Scores: [0.62, 0.63, 0.98, 0.85, 0.94]
Mean F1 Score: 0.80
Test Set Evaluation: Accuracy = 0.96, F1 Score = 0.89
By presenting each step clearly in a sectioned manner, your reader will be able to follow the chronological development and understand the motivation, methods, and results at each stage.
