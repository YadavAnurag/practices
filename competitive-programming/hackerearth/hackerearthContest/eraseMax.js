a = [1, 2, 3];

obj = {};
a.forEach(element => {
    if (!obj[element]) {
        obj[element] = 1;
    } else {
        obj[element] += 1;
    }
});
s = [];
sd = Object.keys(obj);
sd.forEach(element => {
    s.push(obj[element] * Number(element));
});

sum = 0;

s = s.sort((a, b) => {
    return a - b
});
for (var i = 1; i < s.length; i++) {
    sum += s[i];
}

console.log(sum);