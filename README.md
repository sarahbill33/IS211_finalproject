# IS211_finalproject

To create the book application I decided to start with the teacher app model we used in a previous week.
I broke down the requirements into 4 main methods: displaying books, searching books, adding books, and deleting books.

-- For displaying the books I used a python 'for loop' embedded in the html to iterate through the Books table.

-- For searching books I saved the user input (ISBN) as a variable, and used it within the Google Books API call.

-- For adding books, I used an ISBN table to save the user's last input value from their search (the ISBN) and then
   inserted that into another API call to get the data to store into the Books table.
   
-- For deleting books, I tried to add a 'delete' button to each row, but I couldn't figure out how to referencde the 
   right table id for deletion. So I added a user input form to select the row for deletion.
