async function loadExpenses(){

const res = await fetch("/expenses");

const data = await res.json();

let list = document.getElementById("list");

list.innerHTML = "";

data.forEach(expense => {

list.innerHTML += `
<li>
${expense[1]} - ₹${expense[2]} (${expense[3]})
</li>
`;

});

}

async function addExpense(){

const title = document.getElementById("title").value;

const amount = document.getElementById("amount").value;

const category = document.getElementById("category").value;

await fetch("/add",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
title:title,
amount:amount,
category:category
})

});

document.getElementById("title").value="";
document.getElementById("amount").value="";
document.getElementById("category").value="";

loadExpenses();

}

loadExpenses();