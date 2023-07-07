// title
// type of heading

// headingGenerator('hi there', 1) <h1> hi there </h1>

function headingGenerator(title, level) {
    return console.log(`<h${level}> ${title} </h${level}>`)
}

headingGenerator('me cago en dios bendito', '1');


const arrowHeadingGenerator = (title, level) => console.log(`<h${level}> ${title} </h${level}>`);

arrowHeadingGenerator('con flecha tb me rula', 2);//? 
