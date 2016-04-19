# Week 10 - Fullstack project 

## Stories

### New repository
Create a repository on your github profile, make sure that all the necessary
files are ignored, and you are able to push to github your changes.
Initialize your app with npm and create your package.json file.

### Main page
The app should contain a server.js file that runs the server.
It should have a directory called public, that contains all the client relate

assets. 
You shuld be able to run the server with: `node server.js`
If your server is running it should be accesable from: `http://localhost:3000`
It should show "Calorie counter" as a title in a `<h1>` element.

### Add meal backend
#### Create a database scheme for meals.
Each meal should have:
a name (string),
a calorie (number),
a date (date)
#### Create an endpoint: "/meals"
With a "POST" request it should add a new meal to the database, it should
receive the meal in the post data.
Use the "body-parser" module for decoding the post data.
You can try your application with the following command:
`curl --data '{"name": "something", "calories": 200, "date": "2016-01-26:12:03:10"}' -H 'content-type:application/json'  http://localhost:3000/meals`
It should reply with `{"status": "ok"}` if the request was successfull


### Add meal frontend
#### Create a form for adding a new meal
- Create an input field for the name of the meal
- Create an input field for the calories
- Create an input field for the date
- Create a button that sends an "POST" http request to the server, to the
"/meals" endpoint with the fields from the inputs.

### List meals backend
#### Create an endpoint: "/meals"
With a "GET" request, it should respond the list of meals.
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
With a "DELETE" request, it should delete the meal with the given id.
If the delete was successfull it shoud response `{"status": "ok"}`,
`{"status": "not exists"}` otherwise

You can try your application with the following command:
`curl -H 'content-type:application/json' -X 'DELETE' http://localhost:3000/meals/3`

### Filter meals fronted
Add a form for filtering on days, it should have a date input and a button called filter, and one called all.
If the filter is clicked it should only show the given day.
If the all is clicked it shoud show all.

### Sum calories
Add a field that always shows the sum of calories
