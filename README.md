# My-library-of-babel
A place where you can find any text

"The Library of Babel" is a short story by Jorge Luis Borges that envisions a vast and labyrinthine library containing every possible book with a certain number of characters. The library is explored as a metaphor for the infinite possibilities of literature, knowledge, and the quest for meaning in the universe. The story delves into themes of randomness, order, and the human search for understanding within the vastness of an incomprehensible library.

Attempting to materialize this idea in real life, Jonathan Basile created a website (https://libraryofbabel.info/) that houses more than 10 to the power of 4677 'books.' Each book is a string of completely random characters, with the concept that any possible text can be found within such an extensive library. My project aims to achieve a similar concept using Flask and SQLite3 alongside HTML, CSS, and JS. It's important to note that the more 'books' the database contains, the higher the likelihood of finding your text. During development, I maintained the database at 2 million books, but before uploading, I reduced the number to 10,000 to make it lighter and easier to upload and download from GitHub. In a production server, the database must have many more books to function properly.

The web app I created features a search function to help locate any desired text in the database. It provides 20 pages containing the text, and when any of the pages is clicked, the required text is highlighted to facilitate easier identification.
