### Sports League

##### Stories
- User can upload well formed CSV file
- System should be able to process CSV files and output ranking
- User can edit, delete and add game to the generated list via web interface
- User can display the ranking table based on the uploaded data.
- System should rank the teams by their points then alphabetically if points are equal
- System awards 1 point if it is a draw, 3 points if it the team won and no point for loser

##### Requirements
- Implementation framework: Django.
- Allow the user to upload a CSV file containing the results of the games and display the ranking table based on the uploaded data.
- Allow the user to add, edit, and delete games from the list through the web interface.
- Include unit tests for the Django models and views.
- Document any steps necessary to run the web application and the tests.
- Use the following minimum versions:
    - Python: 3.9
    - Django: 3.2