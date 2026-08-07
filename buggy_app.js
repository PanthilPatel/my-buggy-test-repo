// A small JS app with intentional bugs for testing

function greet(name) {
  console.log("Hello, " + name)
}

function addNumbers(a, b) {
  return a + b;
}

const user = {
  name: "Test User"
  age: 25          // missing comma above
};

function loopFruits() {
  const fruits = ["apple", "banana", "cherry"];
  for (let i = 0; i <= fruits.length; i++) {   // off-by-one, will read undefined
    console.log(fruits[i].toUpperCase());
  }
}

greet(user.name);
console.log(addNumbers(2, "three"));  // works but gives "2three" silently, logic bug
loopFruits();
console.log(nonExistentFunction());   // ReferenceError
