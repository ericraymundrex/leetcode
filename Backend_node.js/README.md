![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

#### <u>Web request</u>


<div class="container">
	<div class="row">
		<div class="col-lg-1"></div>
		<div class="col-lg-10">
			<table class="table table-hover table-bordered">
				<thead>
				<tr>
					<th>Name</th>
					<th>Path</th>
					<th>HTTP Verb</th>
					<th>Purpose</th>
					<th>Mongoose Method</th>
				</tr>
				</thead>
				<tbody>
				<tr>
					<td>Index</td>
					<td>/dogs</td>
					<td>GET</td>
					<td>List all dogs</td>
					<td>Dog.find()</td>
				</tr>
				<tr class="success">
					<td>New</td>
					<td>/dogs/new</td>
					<td>GET</td>
					<td>Show new dog form</td>
					<td>N/A</td>
				</tr>
				<tr class="success">
					<td>Create</td>
					<td>/dogs</td>
					<td>POST</td>
					<td>Create a new dog, then redirect somewhere</td>
					<td>Dog.create()</td>
				</tr>
				<tr class="info">
					<td>Show</td>
					<td>/dogs/:id</td>
					<td>GET</td>
					<td>Show info about one specific dog</td>
					<td>Dog.findById()</td>
				</tr>
				<tr class="warning">
					<td>Edit</td>
					<td>/dogs/:id/edit</td>
					<td>GET</td>
					<td>Show edit form for one dog</td>
					<td>Dog.findById()</td>
				</tr>
				<tr class="warning">
					<td>Update</td>
					<td>/dogs/:id</td>
					<td>PUT</td>
					<td>Update particular dog, then redirect somewhere</td>
					<td>Dog.findByIdAndUpdate()</td>
				</tr>
				<tr class="danger">
					<td>Destroy</td>
					<td>/dogs/:id</td>
					<td>DELETE</td>
					<td>Delete a particular dog, then redirect somewhere</td>
					<td>Dog.findByIdAndRemove()</td>
				</tr>
				</tbody>
			</table>
		</div>
		<div class="col-lg-1"></div>
	</div>
</div>

**Backend Development Framework :**
1. Express
2. Kova
3. Sails

**npm init**
- This means we are initialising a project which is governed by the npm.

**package.json script :**

<code>"start":"nodemon index.js"</code>

**Simple Route and deploy it in Heroku**
```
const express=require('express');

const app=express()

const PORT=process.env.PORT || 3000;

app.get("/",(req,res)=>{
    res.status(200).send("Hello");
});
app.get("/api/instagram/v1/:name",(req,res)=>{
    inst_res={
        name:"Eric",
        followers: 2000,
        following: 4000,
        name:req.params.name
    };

    res.status(200).json(inst_res);
})
app.listen(PORT,()=>{
    console.log(`Server is running at : ${PORT}\nReach http://localhost:${PORT}/`);
});
```

- To deploy this we have to add the .gitignore and add node_modules/
- Here, process.env.PORT should be before the 3000, this is because Heroku hide the environment variables for security reasons.
```
heroku git:clone -a testericrexx
```
To clone the repository.
```
git push heroku master
```
To push it to the server.

#### <u>Swagger - Documentation</u>
- When our application have a lot of features, and many front end and other developers look into the API, then haveing a amazing documentation is very useful.

- In node.js application we use <code>swagger-ui-express</code> from npm.
- We can store our documentation in ==YAML or JSON==. 
```
const swaggerUi = require('swagger-ui-express');
const YAML=require('yamljs');

const swaggerDocument = YAML.load('swagger.yaml');
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

```

- For this we have to download <code>yamljs</code> along with swagger-ui-express.

**FUN NOTE :**
- When you edit the yaml file this will not refelect in the nodemon, even the nodemon is running.
- To resolve this, create a **_nodemon.json_** file and add:
```
{
	"ext" : ".js, .json, .yaml"
}
```
- But default nodemon will only monitor the change in js, mjs file only.
- To resolve this we have to add the extensions.