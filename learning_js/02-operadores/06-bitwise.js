// Byte: 00000000 -> 0
// Byte: 00000001 -> 1
// Byte: 00000010 -> 2
// Byte: 00000011 -> 3
// Byte: 00000100 -> 4
// Byte: 00000101 -> 5
// Byte: 00000110 -> 6

console.log(1 |3); // 00000011
console.log(1 | 4); // 00000101
console.log(3 | 5); // 00000111

console.log(1 & 3); // 00000001
console.log(1 & 4); // 00000000
console.log(1 & 4); // 00000001