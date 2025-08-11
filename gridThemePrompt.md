Return this exact JSON:

    json
    `{"header": "NOAA Marine Debris Monitoring and Assessment Project - Transect Survey", "subHeader": "Please complete this form for each transect surveyed at your designated site. Record site information, observations on debris, and upload relevant documentation. Accurate data supports marine debris tracking and mitigation efforts.", "questions": [{"type": "esriQuestionTypeGroup", "label": "Transect Information", "columnCount": 60, "questions": [{"type": "esriQuestionTypeText", "label": "Site Name (as listed in MDMAP database)", "isRequired": true, "columnSpan": 30}, {"type": "esriQuestionTypeDate", "label": "Date of Survey (MM/DD/YYYY)", "isRequired": true, "columnSpan": 30}]}, {"type": "esriQuestionTypeGroup", "label": "Location and Timing", "columnCount": 60, "questions": [{"type": "esriQuestionTypeNumber", "label": "Transect Start (0-95 in 5m increments)", "isRequired": true, "columnSpan": 30}, {"type": "esriQuestionTypeNumber", "label": "Beach Width (meters, water's edge to back barrier)", "isRequired": true, "columnSpan": 30}, {"type": "esriQuestionTypeTime", "label": "Search Start Time (HH:MM local)", "isRequired": true, "columnSpan": 15}, {"type": "esriQuestionTypeTime", "label": "Search End Time (HH:MM local)", "isRequired": true, "columnSpan": 15}]}, {"type": "esriQuestionTypeGroup", "label": "Site Conditions", "columnCount": 60, "questions": [{"type": "esriQuestionTypeSingleChoice", "label": "Slope (Standing at water's edge, back barrier height)", "isRequired": true, "choices": ["knees and below", "knees to shoulders", "shoulders and above"], "columnSpan": 20}, {"type": "esriQuestionTypeSingleChoice", "label": "Primary Substrate (Predominant surface)", "isRequired": true, "choices": ["mud/silt", "sand", "pebble/gravel", "cobble", "other (describe in notes)"], "columnSpan": 20}, {"type": "esriQuestionTypeSingleChoice", "label": "Back Barrier (Landward limit - check one)", "isRequired": true, "choices": ["dune", "cliff", "boulders", "parking lot", "vegetation", "wall/structure", "dense driftwood", "other (describe in notes)"], "columnSpan": 20}]}, {"type": "esriQuestionTypeGroup", "label": "Debris Search Details", "columnCount": 60, "questions": [{"type": "esriQuestionTypeSingleChoice", "label": "Search Team Size (Number of people, max 2)", "isRequired": true, "choices": ["1", "2"], "columnSpan": 20}, {"type": "esriQuestionTypeSingleChoice", "label": "Debris Removal (How much was removed from transect)", "isRequired": true, "choices": ["all/most", "some", "none"], "columnSpan": 20}, {"type": "esriQuestionTypeSingleChoice", "label": "Consistency Check (Was a consistency check conducted?)", "isRequired": true, "choices": ["yes", "no"], "columnSpan": 20}, {"type": "esriQuestionTypeNote", "label": "If a consistency check was required, take close-up photos of items that lacked consensus and describe them in the notes below.", "columnSpan": 60}]}, {"type": "esriQuestionTypeGroup", "label": "Documentation", "columnCount": 60, "questions": [{"type": "esriQuestionTypeImage", "label": "Debris Photo (Upload a clear photo documenting observed debris at this site)", "isRequired": true, "maxFileCount": 3, "columnSpan": 30}, {"type": "esriQuestionTypeTextArea", "label": "Notes (Describe debris observed, classify by type/category)", "isRequired": true, "columnSpan": 30}]}, {"type": "esriQuestionTypeGeoPoint", "label": "Transect Location (Provide GPS coordinates via map)", "isRequired": true, "columnSpan": 40}, {"type": "esriQuestionTypeAudio", "label": "Verbal Notes/Observations (Record optional audio notes about the transect)", "isRequired": false, "columnSpan": 30}], "thankYouScreen": "Thank you for submitting your transect data to the NOAA Marine Debris Monitoring and Assessment Project. Your participation helps us understand and address marine debris issues nationwide."}`


<!-- This is a comment that will not be visible in the rendered Markdown. 
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
-->
