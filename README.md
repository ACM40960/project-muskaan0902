## PREDICTIVE MODELING FOR EARLY PCOS RISK IDENTIFICATION

### OVERVIEW
Polycystic Ovary Syndrome (PCOS) is a prevalent endocrine disorder affecting women of reproductive age. It is characterized by hormonal imbalances, irregular menstrual cycles, and other health complications such as infertility, diabetes, and cardiovascular diseases.

### OBJECTIVE
This study aims to develop a machine learning model integrated into a web-based application to facilitate the early prediction of PCOS using patient data. 

### INSTALLATION
All the packages used are available in the Anaconda distribution of python

### DATASET
The dataset has been sourced from:  
https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos which contains all physical and clinical parameters to determine PCOS and infertility related issues .
It contains 541 patient records with 41 unique features, given as follows:
- PCOS (Y/N): Presence of Polycystic Ovary Syndrome.
- Age (yrs): Age of the individual in years.
- Weight (Kg): Body weight in kilograms.
- Height (Cm): Height in centimeters.
- BMI: Body Mass Index, a measure of body fat based on height and weight.
- Blood Group: The blood type of the individual.
- Pulse rate (bpm): Heartbeats per minute.
- RR (breaths/min): Respiratory rate, breaths per minute.
- Hb (g/dl): Hemoglobin concentration in the blood.
- Cycle (R/I): Regularity or Irregularity of menstrual cycle.
- Cycle length (days): Length of the menstrual cycle in days.
- Marriage Status (Yrs): Duration of marriage in years.
- Pregnant (Y/N): Pregnancy status.
- No. of abortions: Number of abortions.
- I beta-HCG (mIU/mL): First Beta-Human Chorionic Gonadotropin level.
- II beta-HCG (mIU/mL): Second Beta-Human Chorionic Gonadotropin level.
- FSH (mIU/mL): Follicle Stimulating Hormone level.
- LH (mIU/mL): Luteinizing Hormone level.
- FSH/LH: Ratio of FSH to LH.
- Hip (inch): Hip circumference in inches.
- Waist (inch): Waist circumference in inches.
- Waist/Hip Ratio: Ratio of waist to hip circumference.
- TSH (mIU/L): Thyroid Stimulating Hormone level.
- AMH (ng/mL): Anti-Mullerian Hormone level, indicating ovarian reserve.
- PRL (ng/mL): Prolactin hormone level.
- Vit D3 (ng/mL): Vitamin D3 level in the blood.
- PRG (ng/mL): Progesterone hormone level.
- RBS (mg/dl): Random Blood Sugar level.
- Weight gain (Y/N): History of weight gain.
- Hair growth (Y/N): Presence of excessive hair growth.
- Skin darkening (Y/N): Hyperpigmentation of the skin.
-Hair loss (Y/N): Presence of hair loss.
- Pimples (Y/N): Occurrence of acne.
- Fast food (Y/N): Consumption of fast food.
- Reg. Exercise (Y/N): Regularity of physical exercise.
- BP Systolic (mmHg): Systolic blood pressure.
- BP Diastolic (mmHg): Diastolic blood pressure.
- Follicle No. (L): Number of follicles in the left ovary.
- Follicle No. (R): Number of follicles in the right ovary.
- Avg. F size (L) (mm): Average follicle size in the left ovary.
- Avg. F size (R) (mm): Average follicle size in the right ovary.
- Endometrium (mm): Thickness of the endometrium.

### FILE DESCRIPTION
  * PCOS_data: original data file
  * pcodproject.ipynb : jupyter notebook that contains the code of data preparation, exploration, model tuning and evaluation
  * App: folder that contains all the files for the web page development
    1. pcos_app.py: Flask API that bind between the classification model and the web page.
    2.  best_model.pkl: The classification model
    3. Templates:
    - PCOS_Classifier.html: A webpage that takes all the health parameters as inputs and gives a prediction that the patient will have pcos or not
   
### HOW TO RUN THE PROJECT
*  Clone the Repository:
 - Download the project files by cloning the repository to your local machine:
   'git clone [https://github.com/ACM40960/project-muskaan0902]'

* Install Dependencies:
 - Navigate to the project directory and install the required Python packages using:
    'pip install -r requirements.txt'

* Run the Jupyter Notebook:
 - Open and run the Jupyter Notebook to train the models and analyze the results:
    'jupyter notebook pcodproject.ipynb'

* Start the Web Application:
 - Launch the web application to interact with the model via a user-friendly interface:
    'python pcos_app.py'

* Access the Web Interface:
 - Open your web browser and navigate to http://127.0.0.1:5000/ to use the PCOS prediction form and view the results.  


