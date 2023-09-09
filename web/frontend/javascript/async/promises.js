// Promises are at the core of asynchronous programming in JavaScript.
// They are objects returned from async functions that represent the
// state of the operation. We can attach handlers to this objects that
// will be executed when operation has succeeded or failed. A promise
// can be in one of these states: pending, fulfilled or rejected. Even
// though server returns 404, it is still considered as fulfilled from
// server point of view. Sometimes, both fullfilled and rejected are
// considered as settled. If a promise is settled, it is resolved.


// then method of a promise is called when operation succeeds and it 
// receives response from the server
const fetchPromise = fetch(
    "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json",
);

console.log(fetchPromise);

fetchPromise.then((response) => {
console.log(`Received response: ${response.status}`);
});

console.log("Started request…");

  
// We can call other async functions in handlers and chain them
const fetchPromise2 = fetch(
    "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json",
);

fetchPromise2
  .then((response) => {
    if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
    }
    return response.json();
  })
  .then((data) => {
    console.log(data[0].name);
});

// catch is another handler similar to then, but called if one of
// the async calls in the chain throws error
const fetchPromise3 = fetch(
    "bad-scheme://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json",
);
  
fetchPromise3
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      console.log(data[0].name);
    })
    .catch((error) => {
      console.error(`Could not get products: ${error}`);
    });
  
// If we want to start promises that don't depend on each other,
// we can use Promise.all(). They will be started together, and 
// we'll be notified when they all are fulfilled. There are other
// Promise methods as well for example any() which fullfilled if
// any of the passed promises is fullfilled.
const fetchPromise4 = fetch(
    "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json",
);
const fetchPromise5 = fetch(
    "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/not-found",
);
const fetchPromise6 = fetch(
    "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json",
);

Promise.all([fetchPromise4, fetchPromise5, fetchPromise6])
    .then((responses) => {
        for (const response of responses) {
        console.log(`${response.url}: ${response.status}`);
        }
    })
    .catch((error) => {
        console.error(`Failed to fetch: ${error}`);
    });

// We can utilize async, await keywords as well. When await
// is used, code waits at that point until promise is settled,
// and it returns a normal object not a promise. It has same
// effect of promise chain which consists of promises that
// depend on each other. If there is no such a dependency,
// using Promise.all() is more performant.