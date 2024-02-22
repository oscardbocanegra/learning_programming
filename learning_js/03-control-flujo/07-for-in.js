let user = {
    id: 1,
    name: 'Perro',
    age: '5'
}

for(let prop in user){
    console.log(prop, user[prop])
}