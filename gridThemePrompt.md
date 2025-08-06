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
    
    - For each question (except group-type questions), add `"columnSpan": <integer>` at the question’s root object.
    - For group-type questions, always add `"columnCount": 60` at the root object.

4. **Preserve Layout:**  
    Preserve the original proportions and visual structure of the survey as closely as possible.
    
5. **Output:**  
    Return only the updated, valid JSON including the new layout fields. 
 
**Do not include explanations or formatting outside of the JSON.**
