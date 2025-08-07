You are given:

- An image of a survey form.
- A simplified JSON representation of the same survey, including all contents (title, questions, etc.).

**Your task:**  
Enhance the JSON to reflect the visual layout of the form using a 60-column grid system.

---

### Instructions

1. **Divide the Form:**  
    Treat the form in the image as divided into 60 equal-width columns.
    
2. **Estimate Column Span:**  
    For each question, estimate how many columns it spans visually in the image.
    
    - Round the span to the nearest whole number (e.g., 11.3 columns rounds to 11).
3. **Assign Layout Fields:**
    
    - For each question (except group-type questions), add `"columnSpan": <integer>` at the root of the question object.
    - For map question types, always add `"columnCount": 60` at the root.
    - For group-type questions, always add `"columnCount": 60` at the root.
4. **Preserve Layout:**  
    Maintain the original proportions and overall visual structure of the survey as closely as possible.
    

---

### Rules

#### Rule 1:  If no page or group question type at root

1.1. If neither page nor group question type exists at the root level:  
- Add a parent group question wrapping all other questions, with all questions placed inside its `questions` array.  
- Always add `"columnCount": 60` at the root object of this parent group.  
- Example:

json

`{   "questions": [     {       "type": "esriQuestionTypeGroup",       "label": "Transect Details",       "columnCount": 60,       "questions": [         {           "type": "esriQuestionTypeText",           "label": "Site Name (Name used for the 100-meter site in the MDMAP database)",           "isRequired": true         }         // ... more questions       ]     }   ] }`

#### Rule 2: Proper nesting of questions

2.1. Only page-type or group-type questions can exist at the root level of the JSON.  
2.2. All other questions (except for page and group types) must be nested inside a group or page question.  
2.3. If any are not, wrap them in a parent group (as in Rule 1), always with `"columnCount": 60` at the root of the parent group.

#### Rule 3: If both page and group question types exist

3.1. Add `"columnCount": 60` at the root of each page question.  
3.2. For group questions at the root, add both `"columnSpan": 60"` and `"columnCount": 60"`.

#### Rule 4: If only one of page or group question type exists

4.1. Add `"columnCount": 60"` at the root of each page or group question.

---

### Output:
 
Return only the updated, valid JSON with the new layout fields.

**Do not include explanations or formatting outside of the JSON.**
