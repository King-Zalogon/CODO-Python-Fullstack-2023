

var a = 0
var b = 1

console.log("a =", a, " y b =", b)
document.write("<p>Hola Codo a Codo</p>")

if (a == b) {console.log("a = b")}

if (a != b) {console.log("a != b")}

console.log("*** THE END ***")

// var nota = prompt("Nota?")
var nota = 8


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

// do {
//     document.write("<p>Hola</p>")
//     veces++
// } while (veces >= 10)

// for ( var i = 1 ; i <= 10 ; i++) {
//     document.write("<p>Ya te los dije ", i, " veces!</p>")
// }

for (var i = 1 ; i <= 10; i++) {
    document.write("<p>" + i + " es ")
    if (i % 2 == 0) {
        document.write("par</p>")
    } else {
        document.write("impar</p>")
    }
}

