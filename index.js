
const axios = require('axios');
const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const https = require("https");
app.set("view engine", "ejs");

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

const chatdata = [];


  


app.get("/", (req, res) => {
    res.render("home",{response:0})
});

app.post("/", (request,res)=>{
    
    axios.post('http://10.19.99.156:5000/get_response', {
        user_input: request.body.text
      })
      .then(function (response) {
         chatdata.push(response.data.response)
         res.render("home",{response:chatdata});
      })
      .catch(function (error) {
        console.log(error);
      });

});


app.listen(7000);

