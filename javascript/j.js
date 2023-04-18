// optional chaining
const a = obj.b?.value ?? 'hoho'
const obj = {
  a:1
}

console.log(obj.a.b)
console.log(obj.b?.a)
