const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function menu(){
    rl.question(
    `\nEscolha uma opção abaixo:
    - Exercício: 1
    - Exercício: 2
    - Exercício: 3 
    - Sair: Ctrl+D
    - Opção: `,
    (input_) => {
        switch (input_) {
            case '1':
                console.log('======================================================================')
                let albuns_fav = ['\nRaven, by Kelela', '\nFull Moon, by Brandy', '\nEUSEXUA Afterglow, by FKA Twigs']
                console.log(`______________________________\nÁlbuns favoritos: ${albuns_fav}\n______________________________`)
                albuns_fav.push('\nFancy That, by PinkPantheress')
                console.log(`Álbum favorito do momento: ${albuns_fav[1]}`)
                console.log('======================================================================')
                break;

            case '2':
                console.log('======================================================================')
                let carro = {
                marca: 'Chevrolet',
                modelo: 'Agile 1.4',
                ano: 2011
                }
                console.log(`O carro é um ${carro.marca} ${carro.modelo}, ano ${carro.ano}`)
                console.log('======================================================================')
                break;

            case '3':
                console.log('======================================================================')
                class Produto {
                    constructor(nome, preco){
                        this.nome = nome
                        this.preco = preco
                    }
                    exibir(){
                        console.log(`O produto ${this.nome} custa R$${this.preco}`)
                    }
                }

                let p1 = new Produto('Banana', 2.47)
                let p2 = new Produto('Tomate', 3.25)
                let p3 = new Produto('Maçã', 4.10)
                let p4 = new Produto('Batata', 3.80)
                let p5 = new Produto('Cenoura', 2.90)
                let p6 = new Produto('Alface', 1.75)
                let p7 = new Produto('Cebola', 3.20)
                let p8 = new Produto('Pimentão', 5.50)

                let carrinho_compras = []
                carrinho_compras.push(p1)
                carrinho_compras.push(p2)
                carrinho_compras.push(p3)
                carrinho_compras.push(p4)
                carrinho_compras.push(p5)
                carrinho_compras.push(p6)
                carrinho_compras.push(p7)
                carrinho_compras.push(p8)

                carrinho_compras.forEach((produto, index) => {
                    console.log(`Produto ${index}: ${produto.nome}`)
                });
                console.log('======================================================================')
                break;

            default: 
                console.log("\n>>Opção incorreta ou inexistente. Tente novamente<<")
        }
        menu()
    }) 
}  
menu();    