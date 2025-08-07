You are given:

- An image of a survey form.
- A simplified JSON representation of the same survey, including all contents (title, questions, etc.).

### Your task:

Enhance the JSON to reflect the visual layout of the form using a 60-column grid system.


### Instructions

1. **Divide the Form:**  
    Treat the form in the image as divided into 60 equal-width columns.
    
2. **Estimate Column Span:**  
    For each question, estimate how many columns it spans visually in the image.
    
    - Round the span to the nearest whole number (e.g., 11.3 columns rounds to 11).
3. **Construct Proper Nesting of Questions:**  
    Examine the structure of the JSON, and ensure that only page-type or group-type questions can exist inside the root "questions" array.
    
    - All other question types (except for page and group types) must be nested inside a group or page question. If any are not, wrap them in a parent group.
    - Example:
        
        json
        
        `{   "questions": [     {       "type": "esriQuestionTypeGroup",       "label": "Transect Details",       "questions": [         {           "type": "esriQuestionTypeText",           "label": "Site Name (Name used for the 100-meter site in the MDMAP database)",           "isRequired": true         }         // ... more questions       ]     }   ] }`
        
4. **Assign Layout Columns:**
    
    - For each question (except group-type and page-type questions), add `"columnSpan": <integer>` at the root of the question object.
    - For group-type and page-type questions, always add `"columnCount": 60"` at the root, as these always occupy all 60 columns.
    - For esriQuestionTypeGeoPoint, esriQuestionTypePolyline, and esriQuestionTypePolygon question types, always add `"columnCount": 40"` at the root of the question object.
5. **Preserve Layout:**  
    Maintain the original proportions and overall visual structure of the survey as closely as possible.
    

### Output:

Return only the updated, valid JSON with the new layout fields.

**Do not include explanations or formatting outside of the JSON.**
