You are given:

- An image of a survey form.
- A simplified JSON representation of the same survey, including all contents (title, questions, etc.).

**Your task:**  
Enhance the JSON to reflect the visual layout of the form using a 60-column grid system.

**Instructions:**

1. **Divide the Form:**  
    Treat the form in the image as divided into 60 equal-width columns.
    
2. **Estimate Column Span:**  
    For each question, estimate how many columns it spans in the image.
    
    - Round to the nearest integer (e.g., 11.3 columns rounds to 11).
3. **Assign Layout Fields:**
    
    - For each question (except group-type questions), add `"columnSpan": <integer>` at that question’s root object.
    - For group-type questions, always add `"columnCount": 60` at the root object.
4. **Preserve Layout:**  
    Preserve the original proportions and visual structure of the survey as closely as possible.
    
5. **Scenarios:**
    
    - **If both page and group question types exist:**  
        Always add `"columnCount": 60` at the root object for page questions, and add both `"columnSpan": 60`, `"columnCount": 60` at the root object of group questions.
        
    - **If only one of page or group question type exists:**  
        Always add `"columnCount": 60` at the root object for page or group questions.
        
    - **If neither page nor group question type exists:**  
        Add a parent group question wrapping all other questions, and put all questions inside its `questions` list. Always add `"columnCount": 60` at the root object of this parent group question. For example:
        
        json
        
        `{   "questions": [     {       "type": "esriQuestionTypeGroup",       "label": "Transect Details",       "columnCount": 60,       "questions": [         {           "type": "esriQuestionTypeText",           "label": "Site Name (Name used for the 100-meter site in the MDMAP database)",           "isRequired": true         }         // ... more questions       ]     }   ] }`
        
    - **All questions (except for page and group question types) should be inside a group or page question.** If any are not, add a parent group wrapping those questions, and always add `"columnCount": 60` at the root object of this parent group question.
        
6. **Output:**  
    Return only the updated, valid JSON including the new layout fields.
    
    **Do not include explanations or formatting outside of the JSON.**
