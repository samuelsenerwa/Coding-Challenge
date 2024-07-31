#!/usr/bin/node

// A function that executes x times a function


const call_me_body = (x, theFunction) => {

for(let i = 0; i < x; i++ ) {
    theFunction();
}
}

export default call_me_body;

