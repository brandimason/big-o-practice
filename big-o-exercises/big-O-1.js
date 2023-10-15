// #34 - exercise: Big O Calculation

// What is the Big O of the below function? (Hint, you may want to go line by line)

// some notes: (based on convention)
// - some people say that assignment counts toward Big O and other's do not.
// - for the sake of this exercise, we will count everything


function funChallenge(input) { 
    let a = 10; // assigning variable a as 10 // O(1)
    a = 50 + 3; // reassigning a //  O(1)
  
    for (let i = 0; i < input.length; i++) { // O(n) - n is the input - loops are linear time
      anotherFunction(); // this is being called as many times as the length of input -  O(n) 
      let stranger = true; // assignment - this runs as many times as this loop happens - O(n)
      a++; // a+1  -- O(n)
    }
    return a; // O(1)
  }

// if we add all these up - we will see we have 3 steps (O(1) three times) + n + n + n + n
// BIG O(3 + 4N) -- this just turns in O(n)