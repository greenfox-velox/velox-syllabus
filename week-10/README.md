# Week 10 - Full Stack project

## Materials for Monday

### Organizing your JavaScript code, MVC
Learning JavaScript Design Patterns
book by Addy Osmani
https://addyosmani.com/resources/essentialjsdesignpatterns/book/   
Chapters to read:
- Introduction and everything until the patterns list
- Constructor Pattern
- Module Pattern
- Revealing Module Pattern
- Prototype Pattern
- Facade Pattern
- Factory Pattern
- JavaScript MV* Patterns (all)

Videos to watch when bored with reading:
- Factory Functions in JavaScript https://www.youtube.com/watch?v=ImwrezYhw4w
- Prototypes in JavaScript https://www.youtube.com/watch?v=riDVvXZ_Kb4
- Fast or flexible?  https://www.youtube.com/watch?v=R39zdSLd8ic

### Testing
- Unit testing: how to get your team started  https://www.youtube.com/watch?v=TWBDa5dqrl8 (3rd thing)
- The BEST way to do mocking https://www.youtube.com/watch?v=fgqh-OZjpYY

#### Nice to have
- The rest of Addy Osmani's book
- Example code to check: JavaScript TodoMVC https://github.com/tastejs/todomvc/tree/gh-pages/examples/vanillajs
- Losing motivation  https://www.youtube.com/watch?v=RQg_Q4HYYpg


---


## Stories

### New repository
Create a repository on your github profile, make sure that all the necessary
files are ignored, and you are able to push your changes to github.
Initialize your app with npm and create your package.json file.

### Main page
The app should contain a server.js file that runs the server.
It should have a directory called client, that contains all the client related assets.
You should be able to run the server with: `node server.js`
If your server is running it should be accesible from: `http://localhost:3000`
It should show "Calorie counter" as a title in a `<h1>` element.

### Add meal backend
#### Create a database scheme for meals.
Each meal should have:
a name (string),
a calorie (number),
a date (date)
#### Create an endpoint: "/meals"
When receiving the meal in the post data in a `POST` request, the server should add a new meal to the database.
Use the `body-parser` module for decoding the post data.
You can try your application with the following command:
`curl --data '{"name": "something", "calories": 200, "date": "2016-01-26:12:03:10"}' -H 'content-type:application/json'  http://localhost:3000/meals`
It should reply with the newly created meal object plus status ok if the request was successful. Example response:
```JavaScript
{
  "status": "ok",
  "meal": {
    "id": 123,
    "name": "something",
    "calories": 200,
    "date": "2016-01-04T23:00:00.000Z"
  }
}
```


### Add meal frontend
#### Create a form for adding a new meal
- Create an input field for the name of the meal
- Create an input field for the calories
- Create an input field for the date
- Create a button that sends an `POST` http request to the server, to the
`/meals` endpoint with the fields from the inputs.

### List meals backend
#### Create an endpoint: "/meals"
When receiving a `GET` request, the server should respond with the list of meals.
like:
```json
{
  "meals": [
    {"id": 1, "name": "steak", "calories": 890, "date": "2016-01-04T23:00:00.000Z"},
    {"id": 2, "name": "carrot", "calories": 200, "date": "2016-01-04T23:00:00.000Z"}
  ]
}
```
You can try your application with the following command:
`curl -H 'content-type:application/json'  http://localhost:3000/meals`

### List meals frontend
The fronted should list all the added meals below the form.
It should show the name, calories and date for each.

### Delete meals backend
#### Create an endpoint: "/meals/:id"
When receiving a `DELETE` request, the backend should delete the meal with the given id.
If the delete was successful, it should respond
```JavaScript
{
  "status": "ok",
  "meal": {
    "id": 123
  }
}
```
, otherwise it should respond
`{"status": "not exists"}`

You can try your application with the following command:
`curl -H 'content-type:application/json' -X 'DELETE' http://localhost:3000/meals/3`

### Delete meals frontend
Add a delete button to each row in the meals list. Clicking a button should send a `DELETE` http request to the server, to the
`/meals/:id` endpoint with the id of the corresponding meal, after a user confirmation asking "Are you sure you want to delete this meal?".

### Filter meals frontend
Add a form for filtering the meal list for days. The form should have a date input, a button called 'filter', and one called 'all'.
If the 'filter' button is clicked, it should only show meals for the given day.
If the 'all' button is clicked, it should show all meals.

### Sum calories
Add a field that always shows the sum of calories.
