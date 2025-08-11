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
    Examine the structure of the JSON, and ensure that only `esriQuestionTypeGroup` questions can exist in the root `questions` array.
    
    - All other question types (except for group types) must be inside a group question. If any are not, wrap them in a parent group.
4. **Handle page and group questions**

    - **Page elimination**: Convert all `esriQuestionTypePage` objects to `esriQuestionTypeGroup` objects. Change their `type` property from `esriQuestionTypePage` to `esriQuestionTypeGroup`.
        
    - **⚠️ Critical Requirements:**
        
        - **No empty groups**: Empty `esriQuestionTypeGroup` objects are strictly forbidden. Every group must contain at least one question.
        - **All questions must be grouped**: All question types (except `esriQuestionTypeGroup`) must be placed inside a group. No standalone questions are allowed at the root level.
        - **No nested groups**: Nested `esriQuestionTypeGroup` objects (a group within a group) are strictly prohibited.
    - **Group structure**: `esriQuestionTypeGroup` must always have a `questions` property with an array of question objects as its value.
        
    - **Handling nested groups**: If nested groups are detected, automatically move the nested child group up to its parent's level to eliminate nesting violations. Distribute the child group's questions among sibling groups or create new groups as needed to maintain logical organization.
        
    - **Validation checklist**:  
        ✓ Every group contains at least one question  
        ✓ All non-group questions are inside a group  
        ✓ No group contains another group as a child
5. **Example:**
    
    json
    
    `{ "questions": [ { "type": "esriQuestionTypeGroup", "label": "Transect Details", "questions": [ { "type": "esriQuestionTypeText", "label": "Site Name (Name used for the 100-meter site in the MDMAP database)", "isRequired": true } // ... more questions ] } ] }`
    
6. **Assign Layout Columns:**
    
    - For each question (except `esriQuestionTypeGroup` questions), add `"columnSpan": <integer>` at the root of the question object.
    - For `esriQuestionTypeGroup` questions, always add `"columnCount": 60"` at the root, as these always occupy all 60 columns.
    - For esriQuestionTypeGeoPoint, esriQuestionTypePolyline, and esriQuestionTypePolygon question types, always add `"columnSpan": 30"` at the root of the question object.
7. **Preserve Layout:**  
    Maintain the original proportions and overall visual structure of the survey as closely as possible.
    
8. **Add appearance at root level**
    
    Always add this to the root level:
    
    json
    
    `"appearance": { "grid": { "layout": "dynamic-grid" }, "width": "100%" },`
    

### Output:

Return only the updated, valid JSON with the new layout fields.

**Do not include explanations or formatting outside of the JSON.**
