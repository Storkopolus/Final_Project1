# Fetal Health ML Classifier
Fetal Health Classifier App:
https://fetal-health.herokuapp.com/

Our team utilized fetal health data from Kaggle ["Fetal Health Classification." Accessed: December 23, 2020](https://www.kaggle.com/andrewmvd/fetal-health-classification) to create a machine learning model that will predict the probable outcome of the health of a fetus based on user input. The possible fetal health outcomes are:

1. Normal 
2. Suspect 
3. Pathological

The original fetal health dataframe started with 22 columns(histograms of input data are shown below). Our goal was to narrow down to the most pertinent columns while still maintaining the highest possible accuracy. We originally narrowed the dataframe down to 11 columns.

![image of input_histograms](https://github.com/Storkopolus/Final_Project1/blob/master/fetal-health/static/images/Algorithm_Comparison.png)

We initially tested the model utilizing the following machine learning algorithms in Jupyter notebook:

1. Logistic Regression
2. Linear Discrimination Analysis
3. K Neighbors Classifier
4. Random Forest Classifier
5. Decision Tree Classifier
6. Gaussian NB
7. Linear SVC

![image of Algorithm_Comparison](https://github.com/Storkopolus/Final_Project1/blob/master/fetal-health/static/images/Algorithm_Comparison.png)

The result that gave the highest accuracy was the Random Forest Classifier with a predictability accuracy outcome of 94%. We continued to narrow down to create the least amount of columns with the highest accuracy above 90%. We were able to narrow the dataframe down to 6 columns and maintain a predictability outcome of 93% accuracy. The final model was saved to be incorporated into our Flask app.

After the group decided on the six inputs it was determined that we needed to optimize the model, by tuning the parameters. A random forest regressor was used to tune the following parameters: n_estimators, min_samples_split, min_samples_leaf, max_features, max_depth, and bootstrap. Once the optimization was complete there was a slight increase in the accuracy from approximately 93% to 94%, which matched the original accuracy when all 11 inputs were used, and no optimization was utilized. These optimized settings were then used when the machine learning model was saved for import into the flask app.
