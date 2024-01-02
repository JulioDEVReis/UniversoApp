![universoapp](https://github.com/JulioDEVReis/UniversoApp/assets/142347463/17a73c9f-4742-4773-b3e9-d32399bf0c46)

Aplicativo Mobile, para Android, desenvolvido em Kivy e KivyMD, com correlacionamento a um banco de dados criado, com frases em Português. Esse aplicativo foi desenvolvido em resposta a uma demanda para um aplicativo mobile que apresentasse frases aleatórias para motivação e elevação de moral e astral, bem como a possibilidade do usuário enviar desejos ao universo, e ver a lista de desejos realizados. Veja meu outro repositório chamado App Frases em Português para ver como contornei o problema de somente encontrar frases em inglês na API Forismatic. O aplicativo possui 4 telas, sendo a HomeScreen desenvolvida para o usuário ver uma mensagem aleatória e ter um campo para digitar um desejo para envio ao Universo, uma tela chamada Desejo, para ver o desejo que foi enviado ao Universo, e uma terceira tela chamada Lista de Desejos, com a lista de desejos que foi digitado pelo usuário e armazenado em um arquivo JSON para uso e manipulação, com inclusões e exclusões dos desejos pelo usuário. Há também uma tela chamada Frases, onde o usuário pode ver um conjunto de 3 frases aleatórias e renová-las para que procure mensagens que o permite melhorar seu astral e sua motivação.

Para a criação e gerenciamento das janelas, usei MDScreenManager, do KivyMD, sendo passado como classe principal à classe UniversoApp. Em seguida criei as classes correspondente a cada tela, passando a classe MDScreen a cada uma das classes. Criei em seguida meu arquivo Kivy, com linguagem Kivy, para incluir todos os layouts e widgets de cada tela. Como meu Aplicativo possui relacionamento com um banco de dados, criei um arquivo Python separadamente, com todas as funções para acesso, seleção e manipulação dos dados. O banco de dados contém as frases que usaremos no próprio aplicativo, na primeira e segunda telas. Ao final, o aplicativo foi entregue a cliente em formato APK, empacotado via BUILDOZER.


# O desenvolvimento:
Para a criação e gerenciamento das janelas, usei MDScreenManager, do KivyMD, sendo passado como classe principal à classe UniversoApp.
Em seguida criei as classes correspondente a cada tela, passando a classe MDScreen a cada uma das classes.
Criei em seguida meu arquivo Kivy, com linguagem Kivy, para incluir todos os layouts e widgets de cada tela.
Como meu Aplicativo possui relacionamento com um banco de dados, criei um arquivo Python separadamente, com todas as funções para acesso, seleção e manipulação dos dados. O banco de dados contém as frases que usaremos no próprio aplicativo, na primeira e segunda telas.
Ao final, o aplicativo foi entregue a cliente em formato APK, empacotado via BUILDOZER.

# Problemas e soluções no desenvolvimento:
– A maior dificuldade na realização desse projeto foi encontrar exemplos e materiais em linguagem KivyMD para executar a correta personalização dos layouts e estilização dos widgets. Foram muitos vídeos no youtube, com exemplos diferentes, até que eu pudesse ter condições de executar os códigos corretamente.


