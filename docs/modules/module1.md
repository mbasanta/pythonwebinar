# 1. Geoprocessing and Modelbuilder

## Toolbox

- Majority of ArcGIS functionality is contained here
- Manipulate and process data
- Extensive functionality
    - Some tools seem redundant (Joins, Calculate Field, etc.)
    - Many aimed directly at Model Builder
- Not neccesarily user friendly or intuitive
    - Each tool is an individual action
    - Often must use multiple tools to accomplish task
    - Repeat the same action on multiple similar datasets
    - Leads us to...
- Example
    - Buffer points by 300 feet
    - Whoop big deal

## ModelBuilder

- Drag and Drop interface for automating Toolbox
- Save as new tool in Toolbox
- Export to Python Script
- Example
    - Add Buffer at 300'
    - Add Layer
    - Connect
    - Run and Show
    - Add another buffer 600'
    - Connect
    - Rename Output
    - Run and Show
    - Save and Close
    - Add Toolbox
    - Open and show parameters warning
    - Edit to add parameter
    - Export Model to Script
        - Six lines of code
- Also have the ability to run that from python window

## Script Example

- Points To Line
- Execute and show results
- Open script to show code
- Homework to read over this and try to make heads from tails
