

var a = 0
var b = 1

console.log("a =", a, " y b =", b)
document.write("<p>Hola Codo a Codo</p>")

if (a == b) {console.log("a = b")}

if (a != b) {console.log("a != b")}

console.log("Praise the Omnissiah!")

// var nota = prompt("Nota?")
var nota = 6


if (nota > 0 && nota <= 10) {
    if (nota < 4) {
        document.write("<p>En proceso</p>")
    } else if (nota <= 7) {
        document.write("<p>Aprobado</p>")
    } else if (nota <= 9) {
        document.write("<p>Muy bien</p>")
    } else {
        document.write("<p>Excelente</p>")
    }
} else {
    document.write("<p>***ERROR***</p>")
}

var veces = 1

/* while (veces <= 10) {
    document.write("<p>Ya te los dije ", veces, " veces!</p>")
    veces++
} */

do {
    document.write("<p>Hola</p>")
    veces++
} while (veces >= 10)

for ( var i = 1 ; i <= 10 ; i++) {
    document.write("<p>Ya te los dije ", i, " veces!</p>")
}

for (var i = 1 ; i <= 10; i++) {
    document.write("<p>" + i + " es ")
    if (i % 2 == 0) {
        document.write("par</p>")
    } else {
        document.write("impar</p>")
    }
}


let suma=0;

for(var i=0;i<=5;i++){

  suma=suma+i;

}

console.log(i);


fc = ((a) => a + 100)

console.log( fc(10) )

const IVA = Number('21')
const PI = new Number('3.141592')

console.log(PI);
console.log(typeof(PI))

var num1 = 27
console.log( num1**(1/3))

Number.isSafeInteger(3); // true
Number.isSafeInteger(2 ** 53); // false
Number.isSafeInteger(2 ** 53 - 1); // true
Number.isSafeInteger(NaN); // false
Number.isSafeInteger(Infinity); // false
Number.isSafeInteger("3"); // false
Number.isSafeInteger(3.1); // false
Number.isSafeInteger(3.0); // true

var str1 = '27'

console.log(num1 == str1)
console.log(num1 === str1)

// Escribe un programa que pida una frase y escriba cuantas veces aparece la letra a

var frase = prompt("Ingrese una frase: ")
var count_a = 0

for (var i=0; 101; ++i){
  console.log(frase[i])
}

  

console.log(count_a)