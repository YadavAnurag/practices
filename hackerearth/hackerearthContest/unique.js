process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function (input) {
    if (input == "-1\n") {
        process.exit();
    }
    console.log(input);
    stdin_input += input; // Reading input from STDIN
});

process.stdin.on("end", function () {
    main(stdin_input);
});

function main(input) {
    process.stdout.write("Hi, " + input + ".\n"); // Writing output to STDOUT
}


// var t = 1;
// var n = 10
// var u = [15, 15, 12, 13, 13, 13, 1, 1, 1, 1];
// var a = [20, 30, 15, 16, 12, 1, 23, 24, 1, 2];

// var c = [];
// i = 0
// u.forEach(function (element) {
//     c.push([a[i], element]);
//     i++;
// });


// prev = -1, sum = 0;
// max = 0;
// c.forEach(elem => {
//     if (prev === -1) {
//         prev = elem[1];
//         max = elem[0];

//     } else {
//         if (prev == elem[1]) {
//             if (max < elem[0]) {
//                 max = elem[0];
//             }
//         } else {
//             sum += max;
//             max = elem[0];
//             prev = elem[1];

//         }

//     }
// })
// sum += max;
// console.log(sum);