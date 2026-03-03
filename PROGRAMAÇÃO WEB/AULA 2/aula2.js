// ===1===

var nome = "João Vitor"
var sobrenome = "Rodrigues"
console.log("1. Olá, "+nome + " "+sobrenome+"\n")

// ===2===

var nasc = 2005
var ano = 2026
var iddAtual = ano - nasc
console.log(`2. Sua de idade é ${iddAtual}\n`)


//===3===

var a = 5
var b = 10

var aux = a
a = b
b = aux

console.log(`3. a = ${a}, b = ${b}\n`)

//===4===

var grausC = 32
var converterF = (grausC * 1,8) + 32
console.log(`4. Celsius: ${grausC}Cº -> Farenheit: ${converterF}ºF\n`)

//===5===
var nota1 = 9.8
var nota2 = 8.7
var nota3 = 9.6

var media = (nota1 + nota2 + nota3) / 3
console.log(`5. Média do aluno: ${media}\n`)

//===6===

var valorConta = 150
var gorgeta = valorConta * 0.10;

console.log(`6. Gorgeta: ${gorgeta}\n`)

//===7===

var rua = "Alí"
var num = 922
var cidade = "Lá"
var bairro = "Pra cá"

console.log(`7. Rua: ${rua}, Número: ${num}, Bairro: ${bairro}, Cidade: ${cidade}\n`)

//===8===

var valorProduto = 150
var valorDesconto = valorProduto * 0.15
console.log(`8. Valor do desconto: ${valorDesconto}\n`)

//===9===

var cont = 1
{
    console.log("9.")
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}`)
    console.log(`cont = ${cont++}\n`)
}

//===10===

var p = "Caneta"
var pre = 15
var quant = 2
 console.log(`10. Produto: ${p} | Quantidade: ${quant} | Preço: ${pre} | Total: ${pre*quant} `)