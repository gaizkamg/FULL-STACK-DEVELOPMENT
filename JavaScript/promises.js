const fetch = require('node-fetch');

const fetchUserData = () => {
  return new Promise((resolve, reject) => {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(response => response.json())
      .then(data => resolve(data))
      .catch(error => reject(error));
  });
};

fetchUserData()
  .then(users => {
    console.log(users);
  })
  .catch(error => {
    console.error(error);
  });