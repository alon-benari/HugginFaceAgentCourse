import random

hp_template = """
    History and Physical (H&P)

    **Date:** {date}

    {name} is a {age}-year-old {gender} with a history of {conditions} who presents with {symptoms}.
    The patient {cpap_use} machine for {condition_related_to_CPAP} and requires a walker to ambulate.
    Currently, the patient reports {current_complaints}, including {specific_symptoms}.
    Relevant medical history includes {medical_history}.
    The patient denies {negative_findings}.

    **Pertinent Medications:**
    - {medication_1}
    - {medication_2}
    - {medication_3}

    **Assessment and Plan:**
    1. {assessment_1}
    2. {assessment_2}
    3. {assessment_3}

    **Plan:** {treatment_plan}
    """






thoracic_aneurysm = """\
Here is an example of a CT scan report for a patient with a thoracic aortic aneurysm:

---

**CT Thorax Report**  
**Patient Name:** {name}  
**Patient ID:** 123456  
**Date of Examination:** {date} 
**Referring Physician:** Dr. Jane Smith  
**Indication:** Evaluation of thoracic aortic aneurysm. History of hypertension.  

---

**Technique:**  
CT angiography of the thorax was performed with intravenous contrast administration. Axial, coronal, and sagittal reconstructions were obtained.  

---

**Findings:**  

1. **Thoracic Aorta:**  
- There is fusiform dilation of the ascending thoracic aorta measuring **{aneurysm_size}** in maximum diameter.  
- The aortic arch and descending thoracic aorta are within normal limits, measuring **3.0 cm** and **2.8 cm**, respectively.  
- No evidence of dissection flap or intramural hematoma.  

2. **Heart:**  
- Normal size and configuration of the cardiac chambers.  
- No pericardial effusion.  

3. **Lungs and Pleura:**  
- No focal pulmonary consolidation, pleural effusion, or pneumothorax.  

4. **Mediastinum:**  
- No significant lymphadenopathy.  
- Normal appearance of the trachea and main bronchi.  

5. **Chest Wall:**  
- No evidence of rib fractures or soft tissue abnormalities.  

---

**Impression:**  
1. Fusiform aneurysm of the ascending thoracic aorta measuring **{aneurysm_size} cm** in maximum diameter.  
2. No evidence of aortic dissection or rupture.  
3. Recommend cardiothoracic surgical consultation for further evaluation and management.  

---

**Radiologist:**  
Dr. Emily Carter, MD  
Board-Certified Radiologist  

---

This is a sample report and should be tailored to the specific findings and clinical context of the patient."""

echo_report = """\

**Cardiac Echo Report**  
**Patient Name:** {name} 
**Patient ID:** 123456  
**Date of Examination:** {date}  
**Referring Physician:** Dr. Jane Smith  
**Indication:** Evaluation of cardiac function and aortic valve pathology.  

---

**Technique:**  
Transthoracic echocardiography was performed with standard imaging planes. Doppler and color flow imaging were utilized.  

---

**Findings:**  

1. **Left Ventricular Function:**  
   - The left ventricular ejection fraction (LVEF) is **{EF}%**, indicating normal systolic function.  
   - Mild concentric left ventricular hypertrophy is present, with an interventricular septal thickness of **1.3 cm** (normal ≤ 1.1 cm).  

2. **Aortic Valve:**  
   - The aortic valve is trileaflet with mild calcification.  
   - The aortic valve area (AVA) is **{av_area} cm²**,
   - Peak aortic velocity is **2.8 m/s**, and mean gradient is **15 mmHg**.  

3. **Other Valves:**  
   - Mitral valve: No significant regurgitation or stenosis.  
   - Tricuspid valve: Trace regurgitation with normal right ventricular systolic pressure (RVSP).  
   - Pulmonic valve: Normal.  

4. **Chambers:**  
   - Left atrium is mildly dilated with a diameter of **{la_diameter} cm**.  
   - Right atrium and right ventricle are normal in size and function.  

5. **Pericardium:**  
   - No pericardial effusion.  

---

**Impression:**  
1. Normal left ventricular systolic function with an ejection fraction of **{EF}%**.  
2. Mild concentric left ventricular hypertrophy.  
3. Mild aortic stenosis with an aortic valve area of **{av_area}cm²**.  
4. Mild left atrial dilation.  

---

**Recommendations:**  
1. Continue medical management for hypertension and follow up with cardiology for surveillance of aortic stenosis.  
2. Repeat echocardiogram in 6-12 months to monitor progression of aortic stenosis and left ventricular hypertrophy.  

---

**Cardiologist:**  
Dr. Emily Carter, MD  
Board-Certified Cardiologist  

--- 

"""

def note_generator( template, data):

    """
    A function to generate a report, note, or summary based on the provided template and parameters.
    Parameters: **kwargs: Keyword arguments containing the template and parameters.
    Returns: A formatted report string.
    """     

    return template.format( **data)

def choose_random_string(string1, string2):
   # Generate a random number between 0 and 1
   random_number = random.random()
   
   # Choose string1 if the random number is less than 0.5, otherwise choose string2
   if random_number < 0.5:
      return string1
   else:
      return string2
   

def note_concatenate(ct_aneurysm, echo, hp):
    """
    A function to concatenate the generated notes into a single string.
    Parameters:
        ct_aneurysm (list): List of CT aneurysm notes.
        echo (list): List of echo notes.
        hp (list): List of H&P notes.
    Returns:
        str: Concatenated string        of all notes.
    """
    return "\n".join(ct_aneurysm + echo + hp)   

ct_kwargs_list = [
    {"date": "April 4, 2024", "name": "Donald Duck", "aneurysm_size": 5.5},
    {"date": "April 5, 2023", "name": "Donald Duck", "aneurysm_size": 4.9},
      {"date": "April 6, 2021", "name": "Donald Duck", "aneurysm_size": 3.5},
      {"date": "April 7, 2024", "name": "Mickey Mouse", "aneurysm_size": 6.5},
      {"date": "April 8, 2022", "name": "Mickey Mouse", "aneurysm_size": 4.8},
      {"date": "April 9, 2020", "name": "Mickey Mouse", "aneurysm_size": 3.1},
      {"date": "April 10, 2025", "name": "Bugs Bunny", "aneurysm_size": 4.6},
      {"date": "April 11, 2024", "name": "Bugs Bunny", "aneurysm_size": 4.6},
      {"date": "April 12, 2023", "name": "Bugs Bunny", "aneurysm_size": 4.0},
      {"date": "April 13, 2025", "name": "Elvis Presley", "aneurysm_size": 4.4},
      {"date": "April 14, 2023", "name": "Elvis Presley", "aneurysm_size": 4.1},
      {"date": "April 15, 2022", "name": "Elvis Presley", "aneurysm_size": 4.3},
      {"date": "April 16, 2022", "name": "Duffy Duck", "aneurysm_size": 4.7},
     

      
]

echo_kwargs_list = [
    {"date": "April 4, 2024", "name": "Donald Duck", "av_area": 0.8, "EF": 25, "la_diameter": 4.5},
       {"date": "April 8, 2022", "name": "Donald Duck", "av_area": 1.1, "EF": 29, "la_diameter": 4.7},
      {"date": "June 6, 2024", "name": "Bugs Bunny", "av_area": 0.9, "EF": 25, "la_diameter": 4.6},
      {"date": "June 7, 2023", "name": "Bugs Bunny", "av_area": 1.2 ,"EF": 32, "la_diameter": 4.3},
      {"date": "April 5, 2022", "name": "Bugs Bunny", "av_area": 1.8, "EF": 30, "la_diameter": 4.2},
      {"date": "April 6, 2021", "name": "Bugs Bunny", "av_area": 1.9, "EF": 28, "la_diameter": 4.4},
      {"date": "April 10, 2025", "name": "Elvis Presley", "av_area": 0.7, "EF": 35, "la_diameter": 4.8},
      {"date": "April 11, 2024", "name": "Elvis Presley", "av_area": 1.3, "EF": 35, "la_diameter": 4.9},
      {"date": "April 12, 2023", "name": "Elvis Presley", "av_area": 1.2, "EF": 33, "la_diameter": 5.0},
      {"date": "April 13, 2025", "name": "Duffy Duck", "av_area": 0.6, "EF": 18, "la_diameter": 4.6},
      {"date": "April 14, 2023", "name": "Duffy Duck", "av_area": 1.0, "EF": 27, "la_diameter": 4.7},
      {"date": "April 15, 2022", "name": "Duffy Duck", "av_area": 1.1, "EF": 31, "la_diameter": 4.5},
   

]

def hp_kwargs_list(name,date):
   """
   A method to return H&P for a given a patient wit a bit of random generation of clinical features
   Parameters:
       name (str): The name of the patient.
       date (str): The date of the examination. 
   Returns:
         dict: A dictionary containing the patient's information and clinical features. To be passed to the note_generator metho
   
   """
   return {"name" :name,
        "date":date,
        "age":"58",
        "gender":choose_random_string("female","male" ),
        "conditions":choose_random_string("obesity and diabetes mellitus type 2", "Diabetes,Ischemic Heart Disease"),
        "symptoms":choose_random_string("shortness of breath at rest", "shortness of breath on exertion"),
        "cpap_use":choose_random_string("uses a CPAP","does not use a CPAP"),
        "condition_related_to_CPAP": choose_random_string("OSA","COPD"),
        "current_complaints": choose_random_string("difficulty breathing and fatigue", "chest pain and palpitations"),
        "specific_symptoms":choose_random_string("shortness of breath at rest","chest pain on exertion"),
        "medical_history":"hypertension, hyperlipidemia, and osteoarthritis",
        "negative_findings":"fever, or recent infections",
        "medication_1":choose_random_string("Metformin 1000 mg twice daily","Empagliflozin 10 mg daily"),
        "medication_2":"Lisinopril 20 mg daily",
        "medication_3":choose_random_string("Plavix 75 mg daily","Apixaban 5 mg twice daily"),
        "assessment_1":"Optimize glycemic control and weight management",
        "assessment_2":"Evaluate for potential cardiac or pulmonary causes of dyspnea",
        "assessment_3":"Ensure compliance with CPAP therapy and assess functional capacity",
        "treatment_plan":"adjustments to diabetes medications, pulmonary function testing, weight loss counseling, and follow-up in 2 weeks"
    }

patient_names = ["Donald Duck", "Bugs Bunny", "Daffy Duck", "Elvis Presley"]

kw_dict = {
   "ct":ct_kwargs_list,
   "echo":echo_kwargs_list,
}

def render_patient_chart(patient_name, kw_dict):
    """
    A method to return the patient chart for a given a patient.
    Parameters:
        patient_name (str): The name of the patient.
         kwargs_list (list): A list of dictionaries containing the patient's information and clinical features.
    return: str: A string containing the patient's chart.
    """
    hp_data=hp_kwargs_list(name = patient_name, date = 'May 28,2025')
    #   
    ct_aneurysm = [note_generator(template = thoracic_aneurysm, data = d) for d in kw_dict.get('ct') if d["name"] == patient_name]
    echo = [note_generator(template = echo_report, data = d) for d in kw_dict.get('echo') if d["name"] == patient_name]
    hp = [ note_generator(template = hp_template, data = hp_data)]
    return note_concatenate(ct_aneurysm, echo, hp)


## run, create a little emr.
emr = []
for i, patient_name in enumerate(patient_names):
   emr.extend([i, patient_name, render_patient_chart(patient_name = patient_name, kw_dict = kw_dict)]) 
   
rows, cols = len(patient_names), 3

# Reshape using list comprehension
emr_df = [emr[i * cols:(i + 1) * cols] for i in range(rows)]

print(emr_df)

        
        
