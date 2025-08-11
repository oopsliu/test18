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

3. **Examine root level questions**  
    Examine the structure of the JSON, and ensure that only `esriQuestionTypePage` or `esriQuestionTypeGroup` questions can exist in the root `questions` array.
    
    - All other question types (except for page and group types) must be nested inside a group or page question. If any are not, wrap them in a parent group.

4. **Exam group and page questions**

    - `esriQuestionTypeGroup` and `esriQuestionTypePage` must always have a `questions` property. This property's value must be an array of question objects.
    - An `esriQuestionTypePage` can contain `esriQuestionTypeGroup` objects and other standard question objects within its `questions` array. Nested `esriQuestionTypePage` objects (a page within a page) are not supported.
    - An `esriQuestionTypeGroup` can only contain other standard question objects within its `questions` array. Nested `esriQuestionTypeGroup` objects (a group within a group) are not supported.
    - Don't create empty `esriQuestionTypeGroup`or `esriQuestionTypePage` objects. At least one question should be included in a group or page.
    - If any `esriQuestionTypePage` presents, all direct elements of the top-level `questions` array must be `esriQuestionTypePage` (cannot be group or standard question).
    
5. **Example:**
        
        json
        
        `{ "questions": [ { "type": "esriQuestionTypeGroup", "label": "Transect Details", "questions": [ { "type": "esriQuestionTypeText", "label": "Site Name (Name used for the 100-meter site in the MDMAP database)", "isRequired": true } // ... more questions ] } ] }`
        
6. **Assign Layout Columns:**
    
    - For each question (except `esriQuestionTypeGroup` and `esriQuestionTypePage` questions), add `"columnSpan": <integer>` at the root of the question object.
    - For `esriQuestionTypeGroup` and `esriQuestionTypePage` questions, always add `"columnCount": 60"` at the root, as these always occupy all 60 columns. If `esriQuestionTypeGroup` is inside a `esriQuestionTypePage` question, also add `"columnSpan": 60"` at it's root.
    - For esriQuestionTypeGeoPoint, esriQuestionTypePolyline, and esriQuestionTypePolygon question types, always add `"columnSpan": 40"` at the root of the question object.

7. **Preserve Layout:**  
    Maintain the original proportions and overall visual structure of the survey as closely as possible.
    

### Output:

Return only the updated, valid JSON with the new layout fields.

**Do not include explanations or formatting outside of the JSON.**

