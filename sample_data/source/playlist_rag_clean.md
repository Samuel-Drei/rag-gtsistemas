# 📹 Playlist YouTube — Documentação GT Sistemas

> **Playlist:** [Link](https://youtube.com/playlist?list=PLlKENpe5N_kKlM-HqhGuvp1jRyIE1V-Wv)  
> **Total de vídeos:** 97  
> **Vídeos com transcrição:** 97/97  
> **Data de extração:** 2026-04-14  
> **Canal:** GT Sistemas

---

## 1. NOVO ERP GT SISTEMAS LARAVEL 10

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, Automacao, sass |

### Acesso e Cadastro no ERP
O acesso inicial ao ERP é feito através de um login. O usuário com perfil de superadministrador tem acesso a todas as empresas cadastradas. É possível cadastrar empresas e gerenciar planos, onde se pode selecionar a empresa, definir o plano, a forma de pagamento e o valor. Informações básicas como responsável técnico e CNPJ também são inseridas nessa etapa.

### Emissão de Documentos Fiscais
Na parte de emissões, é possível visualizar as emissões de cada empresa, se são notas fiscais eletrônicas (NF-e) ou notas fiscais de consumidor eletrônicas (NFC-e). O usuário pode acessar os arquivos XML, apagar ou transmitir documentos fiscais diretamente pelo sistema.

### Painel do Usuário Comum
Ao acessar como usuário comum, o painel inicial apresenta gráficos e informações sobre o plano selecionado e as emissões realizadas. O usuário pode gerenciar produtos, categorias e estoque. A importação de clientes e fornecedores via Excel não é permitida, mas as compras podem ser feitas normalmente.

### Funcionalidades do PDV
O sistema possui um módulo de PDV (Ponto de Venda) que permite a realização de vendas. Além disso, o ERP também funciona via API, permitindo a transmissão de NF-e, NFC-e e CTE, além de cancelamentos e cartas de correção.

### Movimentação Financeira e Relatórios
Na parte financeira, é possível visualizar a movimentação de notas fiscais, contas pagas e recebidas. Todas as movimentações devem ser registradas com o caixa aberto. O sistema também oferece relatórios de produtos, clientes e outras informações relevantes. O cadastro inicial do cliente comum inclui a inserção de dados e a configuração do certificado digital.

---

## 2. Cadastrando Super usuário

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Cadastro do Super Usuário
Para cadastrar um super usuário, acesse a página de login do sistema. Insira o nome de usuário, que deve ser "super" e o e-mail deve ser igual ao nome de usuário. A senha também deve ser definida. O super usuário é configurado no arquivo M Super. Após o cadastro, o super usuário já poderá acessar o sistema.

### Cadastro de Empresas
Ao cadastrar uma nova empresa, insira o CNPJ e o sistema buscará automaticamente as informações necessárias. É obrigatório preencher todos os campos. O usuário da empresa será criado automaticamente ao salvar o cadastro. Não é necessário cadastrar usuários separadamente, pois isso pode ser feito posteriormente dentro do módulo da empresa.

### Gerenciamento de Planos
Para criar um novo plano, acesse a seção de planos. É necessário definir o nome, descrição, quantidade máxima de NFe e NFC, se o plano está ativo ou não, e se é visível para o cliente. Também é possível adicionar uma imagem ao plano. Ao editar um plano, as informações podem ser atualizadas conforme necessário.

### Cadastro de Cidades e Usuários
O sistema já traz uma lista de cidades preenchidas, mas é possível adicionar novas cidades. A lista de usuários exibe todos os usuários cadastrados, incluindo nome, e-mail e a empresa a qual pertencem. As ações disponíveis incluem exclusão de usuários.

### Atribuição de Planos
Para que uma empresa cadastrada possa acessar o sistema, é necessário atribuir um plano a ela. Se a atribuição não for feita, a empresa poderá acessar, mas ficará restrita na página inicial. Para atribuir um plano, selecione a empresa, o plano desejado, a forma de pagamento e o valor, e salve as informações.

### Emissão de Documentos Fiscais
Na lista de emissões, todas as NFe de todas as empresas aparecem, incluindo as que foram transmitidas e não transmitidas, além de seu status de aprovação. É possível imprimir, cancelar ou deletar os documentos conforme necessário.

---

## 3. Cadastro de usuário comum

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, sass |

### Cadastro de Empresa
O cadastro de uma empresa comum é realizado após o cadastro do superusuário. Ao criar a empresa, é necessário configurar os dados dela. Caso não seja feita a configuração, o sistema redirecionará para a tela inicial ao tentar acessar outras categorias ou menus.

### Configuração do CNJ
Na configuração da empresa, deve-se inserir o CNJ. Ao digitar o CNJ e realizar a busca, os dados disponíveis serão exibidos. Após inserir as informações, é necessário salvar as alterações.

### Atribuição de Plano
Para que o usuário consiga acessar todas as funcionalidades do sistema, é imprescindível que o superusuário atribua um plano à empresa cadastrada. O superusuário deve acessar o gerenciamento de planos, escolher a empresa e atribuir o plano correspondente.

### Acesso ao PDV
Após a atribuição do plano, o acesso ao PDV será liberado. No entanto, se não houver um caixa aberto, o sistema redirecionará para a tela de abertura de caixa ao tentar realizar uma venda ou acessar o MFC.

---

## 4. Configuração do Super

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Configuração do Super Admin
A configuração do Super Admin envolve o preenchimento dos dados do responsável técnico, como CNPJ, telefone e e-mail. Essas informações são essenciais para a geração do QR Code para pagamentos via Mercado Pago.

### Cadastro de Usuários
Quando um novo usuário realiza o cadastro, é necessário que ele complete a configuração do emitente. Após salvar essas informações, a empresa deve estar devidamente cadastrada para que o sistema funcione corretamente.

### Planos de Contratação
Os planos devem estar cadastrados no sistema para que os usuários possam contratá-los. O cliente pode escolher o plano desejado, mas é necessário que ele realize o pagamento para que a contratação seja efetivada.

### Processo de Pagamento
Após a escolha do plano, o sistema ficará buscando a confirmação do pagamento. Quando o pagamento for aprovado, o usuário será redirecionado e poderá utilizar o sistema normalmente.

---

## 5. Configuração do Emitente

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Configuração do Emitente
Na configuração do emitente, ao realizar o cadastro pela primeira vez, você deve acessar a seção de configuração do emitente. Caso não insira o certificado no momento, você pode ir até a opção de certificado, selecionar o arquivo e inserir a senha, em seguida, salvar.

### Ambiente de Operação
É necessário definir se o ambiente será de homologação ou produção. Essa configuração é importante para o correto funcionamento do sistema.

### Natureza de Operação
Na configuração, você deve cadastrar a natureza de operação. É possível definir uma natureza padrão ou específica para o PDV. Após cadastrar a natureza, não se esqueça de salvar as alterações.

### Seleção de Módulo de Operação
Na seção de emitente, você deve selecionar qual módulo de operação será utilizado. Essa escolha é fundamental para garantir que as operações sejam realizadas corretamente no sistema.

---

## 6. Cadastro de produtos

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Cadastro de Usuário e Atribuição de Plano
Após o cadastro do usuário comum e a atribuição do plano pelo super, o sistema está pronto para uso. O painel principal exibe informações sobre as emissões realizadas no dia e no mês, incluindo a quantidade de emissões de NF-e e o plano que foi tratado, além de um gráfico mensal de valores por dia.

### Emissões de Notas Fiscais
No dia 21, foram emitidas 3 notas e no dia 2, 1,5. O total acumulado para o mês de novembro foi de 4,5. Ontem, foram emitidas duas notas e hoje, uma nota.

### Cadastro de Produto
Para cadastrar um produto, a categoria não é obrigatória. Caso o usuário deseje, pode criar categorias para melhor organização do estoque. O cadastro do produto inclui campos como nome, valor de venda e referência. O campo de CFOP é obrigatório para emissão, e os dados devem ser preenchidos corretamente.

### Padrão de Tributação
Dentro do cadastro de produto, existe a opção de criar um novo padrão de tributação. O usuário deve preencher informações como nome, NCM e CMS. Após salvar, esse padrão pode ser utilizado ao cadastrar novos produtos, facilitando o preenchimento automático dos dados tributários.

---

## 7. Inserindo estoque e realizando compras

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Edição de Produtos e Estoque
No módulo de produtos, é possível listar todos os produtos disponíveis. Para editar um produto, selecione-o e adicione o estoque diretamente. Escolha o produto desejado e insira a quantidade. Essa ação atribui o estoque, que é independente do processo de compra.

### Realizando Compras
No módulo de compras, é possível listar e realizar novas compras. Para iniciar uma nova compra, selecione o fornecedor. Caso o fornecedor não esteja cadastrado, é possível inseri-lo manualmente. Após selecionar o fornecedor, escolha o produto e insira a quantidade. O sistema calculará automaticamente o subtotal.

### Informações da Compra
Durante o processo de compra, é necessário selecionar a transportadora, se houver. Caso contrário, é possível preencher os dados manualmente. Na seção de fatura, selecione o tipo de operação, que pode ser venda ou compra. O sistema traz automaticamente o último número de NFE registrado. É possível indicar se deseja gerar contas a pagar no financeiro.

### Pagamento da Compra
Se optar por gerar contas a pagar, selecione o tipo de pagamento, como dinheiro ou cheque, e insira a data. Caso haja mais de um pagamento, é possível adicionar mais entradas. Após preencher todas as informações, salve a compra.

---

## 8. Emissão de NFCe

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Emissão de NFCe pelo PDV
Para emitir uma NFCe através do PDV, é necessário que o cadastro do produto esteja completo, incluindo o CFOP referente ao estado e o NCM do produto. Além disso, os campos de PIS e COFINS devem estar preenchidos corretamente.

### Adicionando Produtos
Ao selecionar um produto, basta clicar sobre ele para adicioná-lo ao pedido. Caso deseje remover um produto, utilize a opção de exclusão. O sistema permite adicionar ou remover produtos conforme necessário.

### Seleção de Cliente e Forma de Pagamento
Ao selecionar um cliente, o nome ficará marcado no sistema. Para registrar o pagamento, escolha a forma de pagamento (por exemplo, dinheiro) e insira o valor recebido. O sistema calculará automaticamente o troco.

### Visualização de Vendas e Transmissão
É possível visualizar as vendas realizadas pelo PDV na lista de vendas, onde você pode editar, excluir ou imprimir. As vendas também são geradas na NFCe. Para transmitir uma venda, clique na opção de transmissão, especialmente se o estado da venda estiver como "novo".

### Configuração do Emitente
Caso ocorra duplicidade na emissão da NFCe, é necessário acessar a configuração do emitente e ajustar o número de série. Isso é importante para evitar problemas na transmissão de notas fiscais.

---

## 9. Emissão de NFe

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Emissão de NFe
Para emitir uma Nota Fiscal Eletrônica (NFe), você pode começar com uma NFe já existente ou criar uma nova. Se você já tiver um cliente cadastrado, basta buscá-lo. Caso contrário, é possível inserir os dados do cliente manualmente e salvá-los.

### Cadastro de Produtos
Após cadastrar o cliente, você deve adicionar os produtos à NFe. É importante garantir que todos os produtos estejam corretamente inseridos antes de prosseguir.

### Transportadora e Fatura
A inclusão da transportadora e da fatura na NFe é opcional. Você pode optar por preencher esses campos ou deixá-los em branco, conforme a necessidade da transação.

### Transmissão da NFe
Após preencher todos os dados necessários, você pode salvar a NFe e proceder com a transmissão. A transmissão da NFe é mais simples em comparação com a Nota Fiscal de Consumidor (NFC). 

### Impressão da NFe
Depois de transmitir a NFe, você pode gerar a impressão. O processo de impressão é simplificado, exigindo apenas que os dados do cliente e do produto estejam preenchidos, além das informações opcionais de transportadora e fatura.

---

## 10. Abertura e Fechamento caixa

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Movimentação de Caixas
Na movimentação de caixas, ao clicar na opção, é exibido o usuário logado, a data de abertura e o valor. A data de fechamento ainda não está disponível, pois o caixa não foi fechado. Os tipos de pagamento são variados e, conforme as vendas são realizadas, os cartões são abertos e o valor total é atualizado, incluindo o valor da venda e o valor de abertura.

### Pagamentos e Recebimentos
Na seção de movimentação, são apresentados os pagamentos e recebimentos. Quando uma conta é recebida, ela é marcada como paga e aparece na tabela. Há um totalizador que mostra o total recebido, total pago, suprimentos e sangrias. Suprimentos e sangrias são realizados dentro do PDV. Se um valor for adicionado como sangria, ele será registrado no totalizador.

### Fechamento de Caixa
Para realizar o fechamento do caixa, é necessário inserir o valor total em dinheiro, cheque e outras observações. Após salvar, se a movimentação for consultada, aparecerá uma mensagem informando que não há caixa aberto no momento. A lista de todos os caixas, com a data de abertura e fechamento, pode ser acessada. É possível imprimir um relatório que inclui a data de abertura, valor de abertura, moedas separadas por tipo de pagamento, cliente, estado, número e valor.

### Abertura de Caixa
Ao tentar realizar uma venda, o sistema solicitará a abertura do caixa. Para abrir um novo caixa, é necessário que haja uma NFe, e o sistema só permitirá essa operação se o caixa estiver aberto. Se não houver movimentação, não será possível realizar o fechamento.

---

## 11. Contas a pagar e receber

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Contas a Pagar
Na seção de contas a pagar, é possível filtrar por fornecedor e data. As contas aparecem com o estado "pendente". O pagamento deve ser feito pelo valor total, não sendo permitido pagamentos parciais. Após o pagamento, a conta é marcada como "pago" e não é possível realizar mais ações sobre ela. As contas a pagar são geradas automaticamente ao realizar uma compra e selecionar a opção de gerar contas a pagar. Também é possível criar uma conta a pagar manualmente, inserindo a descrição, fornecedor e valor integral. Existe uma funcionalidade que permite a repetição de vencimentos. Por exemplo, ao cadastrar uma conta com vencimento em 22, se a data de vencimento for até maio de 2024, o sistema repetirá automaticamente as contas até essa data.

### Contas a Receber
A funcionalidade de contas a receber é semelhante à de contas a pagar. Após o recebimento, a conta é marcada como "recebido" e desaparece da lista de ações. Para cadastrar uma conta a receber, é necessário informar o cliente, o tipo de pagamento e a data de vencimento. Caso a data de vencimento seja até junho de 2025, o sistema também repetirá automaticamente as contas até essa data.

---

## 12. Relatórios

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Relatórios Financeiros
Na parte financeira do ERP GT Sistemas, existem diversos relatórios disponíveis, como relatórios de produtos, clientes, fornecedores, CTE, NFC-e e NF-e. Cada um desses relatórios oferece mais de uma opção de seleção, permitindo filtrar por estoque positivo ou negativo, produtos mais vendidos ou menos vendidos.

### Filtragem de NF-e e NFC-e
Nos relatórios de NF-e e NFC-e, é possível selecionar por tipo, como NF-e de entrada ou saída, e também por estado, incluindo opções como novas, ajeitadas ou canceladas. Além disso, é viável buscar relatórios por cliente, permitindo visualizar quantas contas a pagar ou a receber.

### Relatório de Comissão
O relatório de comissão só funcionará se um vendedor for selecionado. Após a seleção, o sistema calculará automaticamente a comissão com base nas informações cadastradas no módulo de pessoas, especificamente na seção de vendedores, onde é possível definir o valor da comissão para o cálculo.

---

## 13. Importação de clientes e fornecedores

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Importação de Fornecedores
A importação de fornecedores pode ser realizada através de um arquivo Excel. É necessário preencher as informações corretamente, como a razão social, tipo de documento (texto ou numérico) e o campo "contribuinte final", que deve ser preenchido com 0. Após preencher, salve o arquivo e inicie o processo de importação.

### Importação de Clientes
O processo de importação de clientes é semelhante ao de fornecedores. Utilize o mesmo modelo de arquivo Excel, preenchendo as informações necessárias. Após completar o preenchimento, localize o arquivo e clique em salvar. O sistema realizará a importação automaticamente.

---

## 14. Importação xml compra

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Importação de XML em Compras
Para realizar a importação do XML em Compras, acesse o menu "Compras" e selecione a opção "Importação XML". 

### Seleção do Arquivo
Selecione o arquivo XML desejado. O sistema irá preencher automaticamente os campos com as informações dos produtos, transportador (se houver) e a parte da fatura.

### Natureza de Operação
Após a importação, é necessário selecionar a natureza de operação correspondente. Certifique-se de que a natureza de operação esteja cadastrada corretamente no sistema. 

### Simplicidade do Processo
O processo de importação é bastante simples e direto, facilitando a inclusão de dados no sistema.

---

## 15. Emissão Cte

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Cadastro de Veículos
Para emitir um Conhecimento de Transporte Eletrônico (CT-e), é necessário ter um veículo cadastrado. Acesse o módulo de veículos e clique em "Novo" para cadastrar um veículo. Preencha os dados iniciais, incluindo a natureza da operação, o CFOP e o estado correspondente, que no caso é 5352.

### Preenchimento de Campos Obrigatórios
Durante o preenchimento do CT-e, os campos obrigatórios aparecem em vermelho. É importante preencher todos os campos obrigatórios para que o botão "Salvar" fique habilitado. Caso algum campo obrigatório não seja preenchido, o botão permanecerá desabilitado.

### Referência e Chave de Acesso
Na parte de referência, adicione a chave de acesso do CT-e. Você pode adicionar mais de uma chave clicando em "Adicionar". O sistema irá clonar a linha para cada chave adicionada. Caso ocorra algum erro, como a linha de alerta sumindo, verifique se todos os campos obrigatórios foram preenchidos corretamente.

### Informações de Entrega
Na seção de informações de entrega, selecione o destinatário e o remetente. O sistema preencherá automaticamente a data de entrega e o valor a receber. Certifique-se de que todos os campos obrigatórios, indicados com asterisco vermelho, estejam preenchidos.

### Transmissão e Impressão
Após preencher todas as informações e salvar o CT-e, você pode realizar a transmissão. Se a transmissão for bem-sucedida, o sistema retornará uma mensagem de sucesso. Em seguida, você poderá proceder com a impressão do CT-e.

---

## 16. Emissão de MDFe

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Emissão de MDFe
Para emitir uma MDFe, é necessário preencher o campo "F Inicial" e "F Final". É importante consultar o contador para esclarecer dúvidas sobre esses dados e o tipo de emitente. O objetivo é demonstrar que a emissão está funcionando e transmitindo corretamente.

### Informações de Descarregamento
Na seção de informações de descarregamento, é necessário preencher alguns dados adicionais. O tipo de transporte deve ser especificado, e o ID deve incluir a placa do veículo. Se a NFe for preenchida, não é necessário incluir o CTe, e vice-versa. Também é necessário informar o município de carregamento e adicionar as informações, o que criará uma nova tabela.

### Configuração do Emitente
Após preencher os dados, é importante salvar as informações. Caso haja rejeição de unidade, é necessário acessar a configuração do emitente e verificar as emissões. Na seção de MDFe, deve-se colocar o número 613 e tentar transmitir novamente. Se houver documentos não encerrados, será necessário encerrá-los antes de prosseguir.

### Impressão e Download
Após a emissão da MDFe, é possível realizar a impressão. O sistema traz a chave e permite fazer o download do arquivo gerado. Após salvar o arquivo, a emissão da MDFe estará concluída.

---

## 17. Pré-venda, ou venda de balcão

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Módulo de Pré-venda
O módulo de pré-venda foi criado recentemente e permite gerenciar todas as pré-vendas. É semelhante ao layout do PDV e funciona com leitor de código de barras. O leitor pode ser ativado ou desativado clicando no botão correspondente.

### Finalização da Venda
Para finalizar uma venda, é necessário escolher uma forma de pagamento. É possível selecionar a data e, após salvar, finalizar a venda. O sistema redireciona para a lista de pré-vendas, onde é possível finalizar a venda escolhendo se irá gerar uma conta a receber. É importante que o cliente tenha o CPF na nota, pois isso permite gerar a NFe; caso contrário, apenas a NFC-e pode ser finalizada.

### Transmissão e Impressão
Após finalizar a venda, o sistema realiza a transmissão e informa se foi concluída corretamente. Também é possível utilizar um cupom fiscal. Após a finalização, é possível visualizar os detalhes da venda, incluindo cliente, produtos e tipo de pagamento. Há a opção de imprimir o comprovante da venda.

### Opções Adicionais
Na tela de pré-venda, é possível realizar mais ações, como visualizar o histórico do estado do cliente e do pagamento. O sistema também oferece opções para imprimir ou visualizar documentos relacionados à venda.

---

## 18. Relatório de Taxas

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao |

### Relatório de Taxas de Cartão

O relatório de taxas de cartão ou taxas de tipo de pagamento pode ser acessado no módulo Financeiro, na opção Taxa de Cartão. É possível escolher o tipo de pagamento, como cartão de crédito, débito, cheque ou dinheiro. Você pode inserir uma taxa específica para cada tipo de pagamento.

### Cadastro de Taxas

No sistema, é possível cadastrar taxas para diferentes tipos de pagamento. Por exemplo, ao selecionar cartão de crédito, você pode definir a taxa e escolher a bandeira, embora não seja obrigatório informar a bandeira. O cadastro de taxas é feito para facilitar a visualização e o controle das vendas.

### Geração de Relatórios

Após realizar as vendas, você pode acessar os relatórios de taxas. Para isso, selecione o período desejado e o sistema irá gerar um relatório que inclui informações como a taxa do cliente, valor total, percentual da taxa, data e tipo de pagamento (dinheiro, cartão, etc.).

---

## 19. App Auto atendimento - extensão do sistema Slym sass Laravel 10

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass |

### Aplicativo de Autoatendimento
O aplicativo de autoatendimento foi desenvolvido em Ionic e é integrado ao ERP Laravel 10. Ele é projetado para Android Tablet e possui um menu de cardápio. As principais telas e funcionalidades serão demonstradas, incluindo a configuração de produtos e comandas adicionais, que serão explicadas em vídeos futuros.

### Configuração do Aplicativo
Para configurar o aplicativo, é necessário acessar a seção de configuração, onde será solicitada uma senha. As informações que devem ser inseridas incluem a URL do servidor, o token de pagamento e o número da mesa. Após salvar essas informações, o aplicativo poderá se conectar ao servidor. O aplicativo suporta três idiomas: português, espanhol e inglês, e a configuração de idioma pode ser alterada nas opções de cadastro de produtos.

### Cadastro de Produtos
No cadastro de produtos, é possível definir se a aplicação deve analisar informações em diferentes idiomas. Se a opção estiver marcada, o sistema exibirá campos para nome e descrição em inglês e espanhol. Isso se aplica também a adicionais, como tamanhos de pizza. Os tamanhos de pizza e ingredientes podem ser configurados, permitindo que o usuário personalize seu pedido.

### Finalização de Pedidos
Ao finalizar um pedido, o cliente deve abrir a mesa informando o nome e telefone. O pedido é enviado e pode ser visualizado na tela de controle de pedidos, onde itens em aberto são listados. É possível alterar o tempo de preparo dos itens e chamar o garçom, que receberá um alerta sonoro no sistema.

### Emissão de Cupom Fiscal
Na finalização da mesa, o cliente pode avaliar o atendimento e escolher a forma de pagamento. Após informar o valor, o sistema permite finalizar a venda e emitir um cupom fiscal ou não fiscal. A nota fiscal eletrônica (NFC-e) é gerada automaticamente após a finalização do pedido. Para adquirir a solução, os interessados devem entrar em contato através do telefone ou WhatsApp fornecido na descrição do vídeo.

---

## 20. Módulo contador

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, Contador |

### Módulo de Contador
O módulo de contador permite visualizar os dados da empresa vinculada, podendo ser uma ou mais. É possível alterar a configuração do emitente, como subir um certificado e alterar o endereço. Também é viável visualizar e fazer o download de documentos, filtrando por período, incluindo vendas com notas fiscais eletrônicas (NFE) e notas fiscais de consumidor eletrônicas (NFC-e).

### Cadastro de Contadores
No super admin, no menu submenu contadores, é possível cadastrar contadores. O formulário de edição é semelhante ao de cadastro de empresas, com a diferença de incluir o percentual de comissão e o limite de cadastro de empresas, que é definido como dois. O contador pode cadastrar novas empresas, desde que não tenha atingido o limite.

### Financeiro do Contador
No módulo financeiro, ao clicar em novo pagamento, é possível selecionar o mês e o ano. O total de vendas é calculado com base nas vendas de planos. O percentual de comissão é aplicado, e o sistema não permite realizar um novo pagamento para o mesmo mês e ano, bloqueando a ação.

### Cadastro de Empresas e Produtos
O contador pode visualizar as empresas vinculadas e cadastrar novas, desde que tenha limite disponível. Ao alterar a empresa visualizada, o contador pode acessar o formulário de cadastro para modificar informações, que impactam no certificado e dados de emissão. No cadastro de produtos, é possível visualizar os produtos da empresa, mas não realizar alterações.

### Documentos Fiscais
Os documentos fiscais, como NFE e CTE, podem ser filtrados por período. É possível visualizar, imprimir e fazer o download do XML e do arquivo zip de cada documento. O sistema oferece a opção de download único por linha e download total, conforme o período filtrado.

---

## 21. Comissão de vendas

### Comissionamento de Vendas dos Funcionários
Neste vídeo, é abordado o comissionamento de vendas dos funcionários. Para acessar, é necessário abrir uma venda no PDV e clicar em "Comissão de Vendas". É possível visualizar todos os funcionários e filtrar por data e status, como pendente ou pago.

### Seleção de Funcionários e Comissões
Ao selecionar um funcionário, como o João, é possível definir uma comissão para ele. Após isso, ao retornar à tela de "Comissão de Vendas", é possível filtrar as comissões pendentes. Também é possível selecionar mais de uma comissão para pagamento.

### Pagamento de Comissões
Para realizar o pagamento de uma comissão, é necessário criar uma nova venda. Após selecionar o total e clicar em "Pagar", uma modal será exibida. Nela, é possível escolher entre gerar uma conta a pagar ou apenas mudar o status para pago. Se optar por gerar a conta a pagar, é obrigatório informar a data de vencimento.

### Alteração de Dados da Comissão
Na modal de pagamento, o valor da comissão é exibido e pode ser alterado. É necessário informar a data de vencimento e o tipo de pagamento, que pode ser qualquer um dos disponíveis, como dinheiro. Após salvar, o status da comissão será atualizado.

### Visualização em Contas a Pagar
Após o pagamento, ao acessar "Contas a Pagar", será exibido o registro do pagamento da comissão, permitindo o acompanhamento das transações realizadas.

---

## 22. Gestão Pessoal

### Funcionamento do Módulo de Gestão Pessoal
O módulo de Gestão Pessoal tem como objetivo criar a folha salarial dos funcionários. Nele, é possível definir eventos como o INSS, que possui campos como nome, tipo (mensal, anual, semanal), método (informado ou fixo), condição (soma ou diminui) e tipo (percentual sobre o salário ou valor fixo).

### Edição de Eventos
Para editar um evento, como o INSS, é necessário acessar o evento e preencher os campos adequadamente. Se o método for fixo, o campo correspondente ficará desabilitado na hora de gerar a apuração. Após salvar as alterações, é necessário vincular o evento aos funcionários.

### Vinculação de Eventos aos Funcionários
Após definir o evento, é preciso vincular aos funcionários. Por exemplo, ao editar o funcionário João, é possível incluir o INSS com um valor específico, como R$ 60. Após a inclusão, é possível realizar a apuração.

### Realização da Apuração
Para realizar a apuração, deve-se criar uma nova apuração para o funcionário, como João. Os campos definidos como informados aparecerão, enquanto os fixos não poderão ser modificados. É possível alterar o valor, por exemplo, para R$ 100, e escolher a forma de pagamento.

### Geração de Conta a Pagar
Após definir o valor final, que pode ser, por exemplo, R$ 1.130, há a opção de imprimir e gerar a conta a pagar dessa folha. É necessário definir o vencimento e a descrição, além de indicar se a conta está paga ou não. Após salvar, é possível verificar o status da conta em financeiro ou contas a pagar, onde o status pode ser atualizado para pago.

---

## 23. Configuração do delivery

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular |

### Configuração do Delivery
Neste vídeo, será abordada a configuração do delivery desenvolvido com Angular, que consome uma API criada no ERP. Para realizar o Build, é necessário apenas a URL do ERP e o token gerado para cada empresa. O token identifica qual empresa está buscando os dados na API.

### Formulário de Cadastro
O formulário de cadastro é simples e semelhante ao do cardápio. O token é um elemento crucial. Além disso, variáveis do Mercado Pago são utilizadas para gerar o QR Code no aplicativo PWA do cliente. 

### Autenticação de SMS
A autenticação de SMS é utilizada para novos cadastros. Se a opção estiver marcada como "sim", um SMS com um código de quatro dígitos é enviado para autenticação em dois fatores. O cliente também pode ter a opção de confirmar o pedido. Se a opção estiver marcada como "sim", uma janela aparecerá para aprovar ou recusar o pedido. Se estiver marcada como "não", o pedido é aprovado automaticamente.

### Configuração de Categorias e Produtos
As categorias e produtos podem ser ativados ou desativados. Para que uma categoria entre no delivery, deve estar definida como "sim". Os produtos também precisam estar configurados para o delivery, e é possível filtrar e editar os itens, incluindo ingredientes e adicionais.

### Valor de Delivery
No módulo de delivery, há um campo específico para o valor de entrega. Se este campo não estiver preenchido e a opção estiver marcada, o sistema utilizará o mesmo valor do produto.

---

## 24. Configuração de delivery  - video 2

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular |

### Funcionamento do Delivery
Na configuração do Delivery, é necessário informar os dias em que o serviço estará disponível, além dos horários de início e fim. Para editar, basta acessar a tela correspondente e selecionar o dia desejado, como por exemplo, a quarta-feira.

### Cadastro de Bairros
Na seção de bairros, é possível cadastrar todos os bairros da cidade. Para editar, acesse a tela de cadastro, onde você deve informar o nome do bairro, o valor da entrega e o status. É importante deixar o status ativado para que o bairro esteja disponível.

### Adicionais e Produtos
Na configuração de adicionais, há a opção de ativar ou desativar esses itens. Os adicionais são vinculados aos produtos do cardápio. Ao cadastrar um novo destaque, apenas a imagem é obrigatória.

### Cupons de Desconto
Os cupons de desconto podem ser definidos para um cliente específico ou para todos. Ao marcar a opção, um código de seis dígitos é gerado automaticamente, mas também é possível digitá-lo manualmente. É necessário informar o valor do desconto e se ele é percentual ou fixo, além do valor mínimo do pedido. Os cupons podem ser utilizados apenas uma vez; se um cliente tentar reutilizar um cupom já utilizado, o sistema informará que o cupom é inválido.

### Tamanhos de Pizza
O cadastro dos tamanhos de pizza segue a mesma lógica do cardápio. Ao cadastrar um produto do tipo pizza, é necessário marcar os valores correspondentes a cada tamanho disponível.

---

## 25. App de Delivery

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular |

### Adicionando Itens no Delivery
No módulo de Delivery, o usuário pode adicionar itens ao pedido. Após realizar o login, é possível escolher a forma de entrega. O sistema permite selecionar endereços já cadastrados ou cadastrar um novo endereço. O valor da entrega varia conforme o bairro.

### Finalizando o Pedido
Após adicionar os itens e escolher a forma de entrega, o usuário pode incluir observações e finalizar o pedido. O sistema informa que o pedido foi criado com sucesso e aparece no painel para confirmação. O usuário deve confirmar o pedido, que será registrado como aprovado.

### Opções de Impressão e Motoboy
Na tela de pedidos, há a opção de imprimir o pedido e adicionar mais itens. Ao finalizar, o usuário pode escolher um motoboy, que é uma etapa opcional. O sistema permite finalizar o pedido como fiscal ou não fiscal.

### Cadastro de Motoboys e Comissões
O sistema possibilita o cadastro de motoboys e a definição do tipo de comissão, que pode ser um valor fixo. No exemplo, a comissão cadastrada é de R$ 3. O usuário pode optar por gerar uma conta a pagar para as comissões, informando um vencimento e salvando a informação. O sistema cria a conta a pagar e marca as comissões como pagas.

---

## 26. Padrão de tributação para produtos

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular |

### Padrão de Tributação para Produtos
No sistema, é possível definir vários padrões de tributação para produtos. Um padrão pode ser marcado como padrão, o que significa que, ao cadastrar um novo produto, ele já trará automaticamente o padrão selecionado. Isso inclui o percentual de ICMS e o CFOP que estão definidos no cadastro.

### Cadastro de Novo Produto
Ao cadastrar um novo produto, é necessário preencher o nome, o valor de compra e o valor de venda. O sistema facilita esse processo, pois já traz as informações do padrão de tributação definido, tornando o cadastro mais rápido.

### Alteração de Padrão de Tributação
Se for necessário mudar o padrão de tributação durante o cadastro, ao selecionar um novo padrão, todas as informações do produto serão atualizadas automaticamente. Isso permite que o usuário tenha agilidade na configuração dos produtos.

---

## 27. Variações para produtos

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular |

### Cadastrando Variações de Produtos
No sistema, é possível cadastrar variações de produtos. Para isso, inicie o cadastro de uma nova variação e nomeie-a, por exemplo, "tamanhos". Cadastre as opções "P" e "M" e salve. As variações devem estar ativas.

### Cadastrando um Novo Produto
Ao cadastrar um novo produto, como uma camiseta, marque a opção de que ele possui variação. Você pode escolher entre todas as variações ativas no sistema. Os campos obrigatórios são: valor, código de barra e referência. A imagem é opcional. É possível adicionar novas variações, mas neste caso, apenas preencha os campos necessários e clique em salvar.

### Visualização na Lista de Produtos
Após salvar, a camiseta aparecerá na lista de produtos como do tipo "grade", mostrando as variações disponíveis, que neste caso são "P" e "M".

### Atualização no PDV
No ponto de venda (PDV), ao selecionar a camiseta, será exibida uma modal onde você pode escolher a variação desejada. Após selecionar, adicione ao pedido. A mesma funcionalidade se aplica a outras camisetas.

### Impressão de Cupom Não Fiscal
Ao finalizar a venda e optar por imprimir um cupom não fiscal, o sistema exibirá o nome do item e a variação correspondente.

---

## 28. Impressão de NFe - 3 modelos

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular |

### Impressão de NFe
No sistema, agora é possível realizar a impressão de três modelos de Nota Fiscal Eletrônica (NFe): a DF comum, a DF simples e a DF de etiqueta Y. Para acessar essa funcionalidade, é necessário abrir a modal que permite a escolha entre os modelos disponíveis. 

### Modelos de DF
Os modelos disponíveis para impressão são:
- DF comum: modelo que já estava presente no sistema.
- DF simples: novo modelo adicionado ao sistema.
- DF de etiqueta Y: outro modelo disponível para impressão.

---

## 29. CashBack

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular |

### Configuração do Cashback
A configuração do cashback no sistema permite definir alguns parâmetros. O percentual de crédito sobre a venda está definido como 10%, ou seja, uma venda de R$ 100,00 gera R$ 10,00 de cashback para o cliente. O percentual máximo por venda que pode ser utilizado também é de 10%. O valor mínimo para o cashback é de R$ 1,00, mas é possível ajustar esse valor conforme necessário. Além disso, é possível configurar uma mensagem padrão que será enviada via WhatsApp sempre que um crédito for gerado para o cliente, conforme o cadastro desse cliente.

### Realizando uma Venda no PDV
Ao realizar uma nova venda no PDV, é necessário selecionar um cliente. Após salvar, o sistema indicará que o cliente possui R$ 23,00 de crédito. Ao adicionar itens à compra, por exemplo, no valor de R$ 88,00, será gerado um crédito de R$ 8,80. Ao finalizar a compra, a tela do cashback do cliente será atualizada, mostrando que ele agora possui R$ 32,45 disponíveis para utilizar.

### Utilizando o Crédito de Cashback
Para utilizar o crédito de cashback, é necessário adicionar um item e selecionar o cliente novamente. O sistema mostrará que o cliente possui R$ 32,45 disponíveis. Ao informar que deseja utilizar R$ 2,00, o sistema aplicará automaticamente o desconto. Após finalizar a venda, o valor total será ajustado para R$ 30,45, e o status do cashback das compras anteriores será atualizado conforme as transações realizadas.

---

## 30. Módulo ecommerce

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular |

### Funcionamento do Módulo E-commerce
Neste vídeo, é demonstrado o funcionamento do módulo e-commerce integrado ao ERP GT Sistemas. O usuário inicia uma compra adicionando um item ao carrinho, como um fone e uma câmera. Para prosseguir com o pagamento, é necessário informar o CPF e completar o cadastro, caso não esteja logado. Após confirmar o cadastro, o usuário é redirecionado para o carrinho, onde o endereço é automaticamente preenchido.

### Tipos de Pagamento e Geração de NFE
O módulo permite selecionar diferentes tipos de pagamento, incluindo integração com o Mercado Pago. O usuário opta por pagar via Pix, gerando um QR Code. O sistema faz requisições para verificar o status do pedido e, ao aprovar, um alerta sonoro é emitido. O usuário pode visualizar o item e alterar o estado do pedido, como "preparando" ou "em transporte", além de poder gerar a Nota Fiscal Eletrônica (NFE) com as informações já preenchidas.

### Configuração do E-commerce
Na configuração do e-commerce, é possível definir categorias de produtos e o ID da loja, que deve ser único para cada empresa. O sistema não permite que duas empresas tenham o mesmo ID. O usuário pode configurar informações como endereço, links de redes sociais, valor de frete grátis e status da loja. Se a loja for desativada, o acesso ao sistema será bloqueado.

### Gestão de Pagamentos e Pedidos
O módulo permite gerenciar diferentes tipos de pagamento, como Pix, boleto e cartão. O usuário pode editar informações de conta, como e-mail e senha, além de cadastrar ou editar endereços. O sistema exibe o status dos pedidos, incluindo valor total e frete. Caso um pedido não seja pago, o usuário pode gerar uma nova chave Pix para efetuar o pagamento.

### Edição de Termos e Condições
O usuário pode editar a política de privacidade e os termos e condições do e-commerce. É possível adicionar imagens, formatar texto e centralizar informações. O sistema também permite que o usuário filtre produtos por categoria e busque itens específicos, como a câmera mencionada anteriormente.

---

## 31. Confirmação de itens para pré venda

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular |

### Configuração de Confirmação de Itens
No módulo de configuração geral, existe a opção "AC select". Se essa opção estiver marcada como "sim", a confirmação dos itens é obrigatória antes de finalizar a pré-venda, gerar uma venda, uma NFC-e ou uma NFe. O atendente do caixa deve confirmar todos os itens, seja utilizando o código de barras, o leitor de código de barras ou clicando diretamente sobre o item.

### Processo de Geração de Pré-venda
Para gerar uma nova pré-venda, é necessário adicionar os itens desejados. Após adicionar os itens, ao clicar no botão ou dar dois cliques sobre a linha, uma modal será aberta. Se a confirmação for obrigatória, o campo de código de barras e a coluna de status estarão visíveis. Caso contrário, esses campos não aparecerão e a finalização será habilitada sem a confirmação.

### Confirmação de Itens
Durante a confirmação, o atendente pode utilizar a leitura do código de barras ou clicar diretamente no item. Se um item não tiver código de barras, é possível clicar sobre ele para habilitar a finalização. Após a confirmação, o sistema permitirá adicionar mais pagamentos e finalizar a venda, seja com NFC-e ou apenas o cupom fiscal.

### Geração de NFe
Para gerar uma NFe, é necessário escolher um cliente durante a criação da pré-venda. Se não houver um cliente selecionado, a NFe não será gerada, e a finalização poderá ser feita apenas no formato fiscal, imprimindo o comprovante de venda.

---

## 32. Cotação

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular |

### Funcionalidade de Cotação no Módulo de Compras
O sistema possui uma nova funcionalidade no menu Compras, onde é possível criar cotações. O usuário pode escolher um ou mais fornecedores, e o sistema gerará uma cotação para cada fornecedor selecionado.

### Adição de Itens e Campos Opcionais
Na cotação, é possível adicionar itens e preencher observações, que são opcionais. O estado padrão é "Novo" e deve estar ativo. Ao clicar em "Salvar", o botão é desabilitado enquanto o sistema verifica se o cadastro do município e do fornecedor está correto, incluindo o preenchimento do campo e-mail.

### Envio de Links para Fornecedores
Caso o campo e-mail esteja preenchido no cadastro do fornecedor, o sistema enviará links para cada fornecedor. O fornecedor receberá um link que abrirá uma tela onde ele poderá preencher informações obrigatórias, como o valor unitário do item e o subtotal, que não podem ser alterados manualmente.

### Resposta à Cotação e Geração de Compra
Após o fornecedor responder à cotação, o sistema habilita um botão para visualizar a resposta, onde é possível imprimir e gerar a compra. A tela de compra já traz o fornecedor e os itens preenchidos, sendo necessário apenas selecionar a natureza de operação. O usuário pode adicionar mais itens, se desejar.

### Aprovação da Cotação
Após transformar a cotação em compra, ela é aprovada no sistema. Se o usuário tentar preencher uma nova cotação com a mesma referência, o sistema indicará que o fornecedor já foi escolhido, impossibilitando a geração de uma nova compra.

---

## 33. Emissão de Nota Fiscal de Serviço NFSe

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular, NFSe, Nota de serviço |

### Emissão de Nota Fiscal de Serviço (NFSe)
O vídeo demonstra o novo recurso do sistema para a emissão de Nota Fiscal de Serviço (NFSe). Primeiro, é necessário criar o documento e, em seguida, realizar a transmissão.

### Criação do Documento
No menu lateral, acesse a opção "NFC" e clique em "Listar". Para criar uma nova NFSe, clique em "Nova NFSe". Selecione o cliente e o serviço, que já deve estar pré-cadastrado. As informações do tomador (cliente) e do serviço serão preenchidas automaticamente. É possível alterar os dados antes de salvar.

### Pré-visualização e Transmissão
Após a criação, há a opção de pré-visualizar a Nota de Serviço, que ainda não foi transmitida. O sistema gera um arquivo PDF com a aparência da nota. Para transmitir, clique no botão verde "Transmitir NFSe". O processo pode levar alguns segundos, e é necessário aguardar a autorização da requisição.

### Impressão e Cancelamento
Após a transmissão, há a opção de imprimir a nota em PDF. Também é possível cancelar a Nota de Serviço, que abrirá uma modal para inserir o motivo do cancelamento e realizar a requisição. 

### Consulta de Status
Caso a nota fiscal fique em processamento após a transmissão, é possível consultar o status. Se a nota for aprovada, o sistema baixará o XML e registrará no banco de dados, associando a chave. Ao consultar, se autorizado, a janela para impressão da nota fiscal de serviço será exibida.

### Integração com API
O sistema utiliza o serviço da Integra Notas para a emissão das NFSe. Para mais informações, é possível acessar o site integranotas.com.br.

---

## 34. Lista de preços

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular, NFSe, Nota de serviço |

### Acesso à Lista de Preços
Para acessar a funcionalidade de lista de preços no sistema, vá até o menu Produtos e selecione a opção Lista de Preço.

### Criação de Nova Lista de Preço
É possível criar quantas listas de preços forem necessárias. Por exemplo, crie uma nova lista chamada "Venda no Boleto". Defina o valor de venda, o tipo de alteração como "Incremento" e insira um percentual de alteração de 4%. O tipo de pagamento pode ser definido como "Boleto Bancário". A criação de listas específicas para determinados funcionários ou tipos de pagamento é opcional.

### Salvando e Pesquisando Listas de Preço
Após criar a lista, salve-a. A lista aparecerá no PDV. Para pesquisar, utilize a opção de filtro por "Boleto". O sistema marcará as opções disponíveis. Se houver um funcionário associado, ele também será destacado.

### Alteração de Valores
Ao selecionar a lista de preços "Boleto", os valores dos produtos serão atualizados. Por exemplo, ao abrir o item "Coca-Cola", o preço será exibido como R$ 4,44. Se a lista de preços "Boleto" for escolhida, o valor mudará para R$ 45,76.

---

## 35. NCM e remoção em grupo

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular, NFSe, Nota de serviço |

### Seleção de Itens para Remoção
Neste vídeo, é demonstrada a funcionalidade de selecionar vários itens para remoção. Essa opção está disponível em marcas, categorias, produtos, clientes e fornecedores, onde há tabelas. O botão para realizar a remoção estará sempre localizado no final da tela.

### NCM Pré-Definido
Outra funcionalidade apresentada é a tabela de NCM já pré-definida. O sistema possui uma tabela em Excel que, se não estiver preenchida no banco de dados, será utilizada para preencher automaticamente as informações. É possível adicionar, editar a descrição e o código, e remover o NCM. Ao cadastrar um produto ou um padrão fiscal, ao buscar pelo NCM, o sistema já trará as informações pré-preenchidas. Por exemplo, ao buscar "madeira", o sistema exibirá todos os NCMs relacionados a esse material. Também é possível pesquisar pelo código ou pela descrição do NCM ao cadastrar um novo produto.

---

## 36. Abertura de chamados ticket

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular, NFSe, Nota de serviço |

### Abertura de Chamados (Tickets)
Uma nova funcionalidade do sistema é a abertura de chamados, ou tickets, utilizados para a resolução de problemas na aplicação, como erros ou outras questões. Para abrir um novo chamado, é necessário estar logado em uma empresa no sistema. O usuário deve selecionar o departamento, como financeiro ou suporte, e definir o assunto, por exemplo, "erro ao cadastrar produto". 

### Formatação e Anexos
No campo de descrição, é possível formatar o texto e adicionar imagens. Também há a opção de anexar arquivos, que podem ser imagens, XML ou qualquer outro tipo de arquivo. Após enviar a solicitação, o ticket é aberto e o usuário recebe uma notificação.

### Resposta e Anexação de Arquivos
O usuário pode acessar o ticket aberto e responder à mensagem, além de escolher um ou mais arquivos para enviar. O conteúdo anexado fica disponível para download.

### Edição e Alteração de Status
Como super admin, é possível editar o chamado e alterar seu status. O status pode ser mudado para "resolvido", o que impede que o usuário continue escrevendo no ticket. O super admin também pode alterar o status de "resolvido" para qualquer outro estado ou remover o ticket.

---

## 37. Notificações

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular, NFSe, Nota de serviço |

### Notificações no Sistema
As notificações no sistema são destinadas a contas a pagar e receber, além de alertas de estoque e vencimento de produtos. O sistema realiza pesquisas a cada hora, configuradas para 1 hora da manhã e 1 hora da tarde, para verificar se há registros a serem apresentados. Esses horários podem ser alterados ao modificar uma classe no sistema, permitindo definir mais horários ou deixar apenas um para a verificação.

### Tipos de Alerta
É possível configurar quais tipos de alerta o usuário deseja receber. Atualmente, os alertas disponíveis podem evoluir com o desenvolvimento do sistema. Ao clicar em "conta a receber", o sistema apresenta as informações da conta, permitindo ao usuário realizar alterações. O alerta de estoque exibe o produto, valor de compra e venda, e a quantidade disponível.

### Limpeza de Registros
O sistema oferece a opção de limpar todos os registros, que na verdade muda o status dos registros, mas ainda permite visualização no módulo. O usuário pode remover, editar ou criar novas notificações.

### Criação de Nova Notificação
Para criar uma nova notificação, o usuário deve informar o título, a prioridade (que pode ser alta, média ou baixa) e a descrição. Caso a empresa não seja selecionada, a notificação será gerada para todas as empresas. Após clicar em salvar, a notificação será criada e, na próxima atualização da página, o sistema realizará uma nova verificação, exibindo a notificação com a prioridade destacada em vermelho para alta e em amarelo para média.

---

## 38. App de Delivery por link

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular |

### Nova Funcionalidade do Módulo de Delivery
Neste vídeo, é demonstrada uma nova funcionalidade do módulo de delivery, que agora permite o uso de links, semelhante ao funcionamento do e-commerce. Anteriormente, era necessário realizar um build para cada restaurante ou empresa, mas agora isso não é mais necessário.

### Configuração do Delivery
Na configuração do Delivery, existe uma variável chamada ID, que é única para cada empresa, além da cor principal e um token que agora é opcional de gerar. A cor principal pode ser alterada e essa mudança já surte efeito na aplicação do Delivery.

### Adição de Itens e Cupons de Desconto
O processo de adição de itens, incluindo adicionais e ingredientes, permanece o mesmo dos vídeos anteriores. É possível adicionar itens ao carrinho e utilizar cupons de desconto durante o pagamento. No pagamento, há a opção de cadastrar novos endereços e escolher a forma de pagamento, que pode ser em dinheiro, cartão ou PIX. O aplicativo gera um QR Code para o pagamento via PIX.

### Opções de Entrega e Finalização do Pedido
Durante o processo de finalização do pedido, é possível observar que o valor de entrega varia de acordo com o bairro. Existem opções para definir o valor de entrega, valor mínimo para entrega, valor padrão e valor para entrega grátis. Após finalizar o pedido, ele entra em estado de aguardando, e ao confirmar, o pedido é aprovado. A confirmação é opcional e pode ser configurada para que os pedidos entrem diretamente aprovados, caso desejado.

---

## 39. Integração Mercado Livre

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre |

### Configuração da Integração com o Mercado Livre
No vídeo, é demonstrada a integração com o Mercado Livre no ERP. O usuário acessa a área de desenvolvedores do Mercado Livre, onde cria uma aplicação que solicita nome, descrição e logotipo. Após isso, são gerados o ID do aplicativo e uma chave secreta, que devem ser inseridos na configuração do Mercado Livre no ERP. A URL deve ser a mesma do sistema, utilizando HTTPS. Após salvar, o sistema solicitará um novo token, que inclui informações como user ID, access token e refresh token, essenciais para consumir dados como perguntas, pedidos e produtos.

### Gerenciamento de Produtos
O usuário pode acessar a seção de produtos do Mercado Livre no ERP, onde verifica se um produto já está cadastrado. Caso não esteja, o sistema traz os dados do produto, incluindo status e nome. É possível marcar a parte de tributação para preenchimento automático. O usuário pode cadastrar um ou mais produtos de uma vez, ativar ou desativar produtos, e criar novos anúncios, inserindo informações como valor, categoria, condição do item, quantidade disponível e descrição.

### Visualização e Gerenciamento de Pedidos
Na seção de pedidos, o usuário visualiza os pedidos realizados na plataforma. É possível acessar informações do pedido, visualizar o chat e enviar mensagens diretamente ao cliente. O sistema permite a impressão e geração da Nota Fiscal Eletrônica (NFE) do pedido, redirecionando para a tela de vendas. Ao cadastrar um novo cliente, o sistema faz o cadastro automático, enquanto atualiza informações de clientes já existentes. O usuário deve informar a natureza da operação e o método de pagamento para finalizar a NFE.

### Respostas a Perguntas
O sistema também permite gerenciar perguntas feitas pelos clientes. O usuário pode responder perguntas diretamente na plataforma, e as notificações de novas perguntas chegam ao sistema. Após responder, a pergunta é removida da lista de pendências. O usuário pode filtrar as perguntas respondidas para facilitar a visualização.

---

## 40. PDV Offline

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV |

### Introdução ao PDV Offline
Neste vídeo, é apresentado um PDV desenvolvido para operar offline em conjunto com o ERP. A aplicação foi criada em Angular com Electron, tornando-se uma aplicação desktop multiplataforma que funciona em Mac, Windows e Linux.

### Funcionamento do PDV Offline
O objetivo do PDV é realizar vendas normalmente. Se houver conexão, as informações são enviadas imediatamente para o servidor. Caso contrário, os dados são armazenados no local Storage. Isso inclui informações sobre produtos, clientes e tipos de pagamento, permitindo que as vendas sejam realizadas mesmo sem conexão.

### Conexão com o Servidor
Para conectar ao servidor, é necessário informar a URL. No teste, foi utilizada a URL local `http://localhost:8000`. Também é possível utilizar um endereço online, como `http://rpev.p.br`, para conectar sem problemas. O login é feito com o mesmo e-mail utilizado no painel.

### Dashboard e Funcionalidades
O dashboard apresenta um totalizador de produtos, clientes, vendas do caixa aberto e vendas pendentes. As vendas pendentes são aquelas realizadas sem conexão, armazenadas no local Storage. O gráfico exibe as vendas do dia, com horários das 00:00 às 23:00. Os cadastros de produtos, clientes e tipos de pagamento são apenas para visualização, sem opção de cadastro.

### Processamento de Vendas
Na tela do PDV, é possível buscar produtos por código de barras ou categorias. As opções de pagamento incluem as quatro principais modalidades. O sistema permite selecionar um cliente e finalizar a venda, gerando um cupom não fiscal. Também é possível realizar pagamentos múltiplos, com a data sendo opcional. O cupom fiscal é gerado com sucesso no ambiente de homologação.

---

## 41. Contas da empresa

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV |

### Funcionalidade de Contas da Empresa
Neste vídeo, é demonstrada a funcionalidade de contas do ERP, que é utilizada para abertura e fechamento de caixa, pagamento de contas a pagar e recebimento de contas a receber, além de sangria e suprimento.

### Campos Obrigatórios
Ao criar uma nova conta, é necessário preencher campos obrigatórios como nome, status, saldo inicial e saldo atual. O plano de contas é definido no menu financeiro, na opção "Plano de Contas", e é criado automaticamente pelo sistema.

### Abertura de Caixa
Para realizar a abertura de caixa, é necessário ter pelo menos uma conta cadastrada no sistema. O sistema solicitará o preenchimento dos campos obrigatórios. Após salvar, é possível acessar o PDV, adicionar itens e finalizar a venda com pagamento múltiplo, como dinheiro e débito.

### Fechamento de Caixa
Ao finalizar o caixa, se houver pelo menos uma conta cadastrada, o sistema apresentará os totais em forma de cards. É necessário escolher a conta para onde o total em dinheiro será direcionado. O botão de finalizar ficará desabilitado se o valor total for zero. Após adicionar os valores, o caixa pode ser fechado.

### Registro de Contas a Pagar e Receber
No módulo de contas a pagar e receber, ao cadastrar uma conta, é necessário selecioná-la para realizar o pagamento. Isso garante que a conta correta seja utilizada para as transações.

---

## 42. Produto tipo combo

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV |

### Criação do Produto Tipo Combo
Neste vídeo, será demonstrada a criação do produto tipo Combo no ERP. Para iniciar, acesse a opção de novo produto. Defina o nome e o valor de compra e venda. Selecione o tipo "combo" e marque a opção "gerenciar estoque". Essa configuração foi criada na configuração geral, onde foi definida a margem percentual sobre o combo, que considera o valor de compra dos itens que compõem o produto.

### Adição de Itens ao Combo
Ao adicionar os itens do combo, é possível alterar a quantidade de cada item. O sistema ajustará automaticamente o valor de compra e o valor de venda. É possível definir a margem sobre o valor de compra dos itens, como 70%, 20% ou 25%, conforme necessário.

### Configuração Fiscal
A parte fiscal já está preenchida com a tributação padrão definida anteriormente. Após configurar todos os detalhes, salve o produto. Ele estará marcado como "gerenciar estoque".

### Venda no PDV
Ao acessar o PDV e tentar adicionar o combo, o sistema informará se algum item está com estoque insuficiente. Por exemplo, se a batata frita estiver com quantidade zero, será necessário editar o estoque e adicionar a quantidade desejada, como 10. Após salvar, será possível vender o produto, e a baixa de estoque ocorrerá nos itens que compõem o combo.

---

## 43. Emissão de boletos

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV |

### Emissão de Boletos
Neste vídeo, é demonstrada a emissão de boletos no sistema, incluindo a criação do PDF, a geração da remessa e o tratamento do retorno. Para iniciar, é necessário criar uma nova conta a receber, selecionando um cliente, um valor e a data de vencimento do boleto. Após salvar, o sistema exibirá as contas criadas.

### Geração de Boletos
Para gerar boletos, é necessário selecionar as contas desejadas. Se uma conta já tiver um boleto vinculado, o sistema informará que já existe um boleto para a conta selecionada. Ao clicar no botão de gerar boletos, o sistema permite a geração de boletos para uma única conta ou para múltiplas contas. É possível adicionar informações adicionais, como o número do boleto e o número do documento.

### Criação de Remessas
O sistema permite a criação de remessas, exibindo todos os boletos que ainda não possuem remessa. Após selecionar os boletos, é possível gerar a remessa e realizar o download. O sistema também oferece a opção de excluir remessas geradas anteriormente.

### Importação de Retorno
A importação de retorno permite que o sistema trate o arquivo de retorno, vinculando os boletos com base no vencimento, valor integral e pagador. Caso o sistema não consiga encontrar uma correspondência, o campo ficará vazio e não será possível salvar a alteração até que uma conta seja vinculada. Após o preenchimento correto, o status da conta será alterado para "receber".

---

## 44. Manifesto de xml de entrada

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV |

### Consulta de Documentos Fiscais
O vídeo demonstra como realizar a consulta de documentos fiscais importando e gerando uma compra no módulo de Compras. A consulta deve ser feita a cada hora e retorna todos os registros disponíveis. Após a consulta, é possível visualizar os registros em várias páginas.

### Manifestação de Documentos
Após realizar a consulta, o usuário pode manifestar um item selecionando a chave do documento. É possível dar ciência, visualizar o XML, imprimir, gerar o DFe manifestar novamente, ou realizar o desconhecimento e confirmação como um segundo evento.

### Conclusão do Processo
Ao clicar em "Completa", o sistema traz o XML como se fosse de uma compra, permitindo que o usuário conclua a operação. Os produtos são cadastrados no sistema e, caso haja fatura, ela também será apresentada. O usuário deve selecionar uma natureza de operação, que pode ser qualquer uma, e a parte de fatura é opcional. Após preencher as informações, é necessário clicar em "Salvar".

### Redirecionamento para Compras
Após salvar, o sistema redireciona o usuário para o módulo de Compras, onde o XML importado estará disponível.

---

## 45. Videos de suporte

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV |

### Cadastro de Vídeos de Suporte
Foi adicionada uma função para cadastrar vídeos de suporte no sistema. É possível registrar vídeos em várias telas. Por exemplo, ao acessar a tela de produtos, o botão de vídeo aparecerá, mas em outras telas que não possuem vídeo, o botão não será exibido.

### Acesso aos Vídeos
Ao clicar no botão de vídeo, uma nova aba será aberta com o link do vídeo, que pode ser hospedado no YouTube, Google Drive ou qualquer outra plataforma. 

### Como Cadastrar um Vídeo
Para cadastrar um novo vídeo, acesse o menu "Super Admin", selecione "Vídeo do Suporte" e clique em "Cadastrar um Novo Vídeo". É necessário copiar a URL completa do vídeo e colar no campo correspondente. O URL pode ser de qualquer servidor de vídeo.

### Atualização e Visualização
Após salvar as informações, é necessário atualizar a tela para visualizar a opção de assistir ao vídeo. Essa funcionalidade ajuda a reduzir a demanda por suporte.

---

## 46. Integração Nuvem Shop

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV, nuvemshop |

### Integração com Nuvem Shop
O sistema agora possui integração com a plataforma Nuvem Shop. Para configurar, é necessário preencher três campos: appid, cli e Sec email. Esses dados podem ser obtidos no painel de desenvolvedor da Nuvem Shop. Após preencher e salvar, é possível acessar as categorias, editar, excluir e adicionar novos produtos.

### Adição de Produtos
Para incluir um novo item, inicie um estoque com 15 unidades. Na aba "Outros", a categoria Nuvem Shop já vem marcada. Ao salvar o produto com imagem, o processo pode demorar um pouco mais do que sem imagem. É possível adicionar mais de uma imagem ao produto. Se um item estiver com estoque zerado, ele não será exibido.

### Gerenciamento de Pedidos
Os pedidos podem ser gerenciados de forma semelhante ao Mercado Livre. É possível filtrar e gerar uma nova Nota Fiscal Eletrônica (NFE) a partir de um pedido. Ao gerar a NFE, os dados do pedido da Nuvem Shop serão preenchidos automaticamente. É necessário selecionar a natureza da operação e o tipo de pagamento, que é opcional.

### Geração de NFE
Após salvar a NFE, o sistema redireciona para a tela de NFE, onde é exibido o prefixo da Nuvem Shop. É possível transmitir a NFE e gerar o XML temporário. Ao clicar no prefixo da Nuvem Shop, o sistema redireciona para o pedido correspondente, permitindo visualizar e imprimir a NFE.

---

## 47. Controle de acesso dos usuários

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV |

### Controle de Acesso de Usuários
Neste vídeo, foi demonstrado como foi desenvolvido o controle de acesso de usuários no ERP GT Sistemas. O usuário logado como admin pode criar novos controles de acesso, como por exemplo, "test 2". É possível filtrar e enviar tudo de uma vez para salvar.

### Super Admin
O super admin tem a capacidade de visualizar todas as atribuições cadastradas, incluindo aquelas que não estão vinculadas a uma empresa, pois foram cadastradas pelo super admin. O gestor da plataforma não pode editar nem excluir essas atribuições. Ao cadastrar uma nova empresa, por padrão, ela herda as atribuições definidas pelo super admin.

### Edição de Usuários
Ao listar os usuários, é possível ver que o usuário "test" tem acesso admin e o usuário "João", que está logado, tem acesso como caixa. No menu de edição de usuário, foi incluída uma nova coluna chamada "controle de acesso", que permite editar as permissões do usuário. O usuário caixa possui permissões limitadas.

### Permissões de Acesso
Ao tentar realizar uma nova compra, o usuário "João" não possui permissão e recebe um erro ao tentar atualizar. Após conceder permissão para criar compras, o acesso é restaurado. O mesmo processo se aplica a outros menus, como agendamentos e NFC-e, onde as permissões podem ser ajustadas conforme necessário.

### Cadastro de Permissões
O super admin também pode cadastrar novas permissões, com um total de 183 registros até o momento. É possível criar novas permissões, definindo um nome e uma descrição para cada uma.

---

## 48. Multi localizações ou filiais

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV, Filial |

### Cadastro de Localizações ou Filiais
No sistema, o cadastro de localizações ou filiais é feito no menu Configuração, no submenu Localizações. A primeira linha é referente ao cadastro da empresa, que é feito automaticamente na localização. É possível editar apenas a descrição, enquanto as outras informações permanecem na configuração do emitente. Não é possível remover, apenas editar a descrição.

### Edição de Filiais e Usuários
Ao abrir uma segunda filial, é possível editar todos os registros e subir o certificado, que é opcional. Quando uma nova localização é cadastrada, todos os usuários da empresa são atribuídos a essa localização. É possível listar os usuários e verificar os locais de acesso de cada um. Ao editar, é possível adicionar ou remover locais de acesso.

### Cadastro de Produtos
No cadastro de produtos, a disponibilidade é mostrada de acordo com a localização. Se a empresa tiver apenas uma localização padrão, alguns campos, como disponibilidade e estoque, não aparecerão. Ao cadastrar um novo produto, é necessário informar o nome e o valor de compra. A disponibilidade do produto é definida conforme o usuário logado.

### Estoque por Localização
Ao definir a disponibilidade de um produto, é possível setar o estoque de cada localidade. O sistema permite colocar valores como zero ou quantidades específicas. Também é possível filtrar a quantidade em estoque por local.

### Integração com Documentos Fiscais
As localizações são integradas em diversos documentos, como abertura de caixa, CTE, MDF-e, pré-venda, NFe e NFC-e. Ao abrir um conta a pagar, o local da conta é exibido. Se a empresa tiver apenas uma localização, esse campo não aparecerá. Na transmissão de NFe, é necessário que a filial tenha um certificado válido; caso contrário, ocorrerá um erro.

---

## 49. Financeiro e gerenciamento de planos SUPERADMIN

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV, Filial |

### Melhoria no Super Admin - Campo de Valor de Implantação
Foi incluído um novo campo chamado "valor de implantação" no Super Admin, que é opcional. Esse campo será utilizado quando a empresa contrata a licença do sistema pela primeira vez. O valor de implantação será somado ao valor da licença, resultando no total a ser pago. Essa informação será utilizada apenas uma vez.

### Tela de Financeiro dos Planos
Foi criada uma nova tela de financeiro dos planos, que exibirá todas as licenças gerenciadas e atribuídas às empresas, seja pelo Super Admin ou através da contratação. Quando o plano expira, a empresa pode gerar um pagamento via PIX utilizando o botão "contratar plano". É possível filtrar por empresa, período e status de pagamento, além de visualizar uma soma geral dos valores recebidos, pendentes e cancelados.

### Inclusão de Planos e Geração de QR Code
Não é possível incluir manualmente planos, mas ao realizar uma contratação, o sistema lista todos os planos disponíveis para o usuário. Se o valor de implantação for diferente de zero, o sistema identificará que é a primeira vez que a empresa está contratando. O formulário requer o preenchimento do nome, sobrenome, e-mail, tipo de documento e número do documento, gerando um QR Code para o pagamento. Após a finalização do pagamento, o sistema atualizará automaticamente o financeiro.

### Gerenciamento e Atribuição de Planos
No gerenciamento, é possível atribuir um plano a uma empresa. Ao identificar a empresa e selecionar o plano, o sistema mostrará o valor do plano. Se for a primeira vez que a empresa está utilizando, o valor da implantação será diferente de zero. Após clicar em salvar, o plano será atribuído à empresa e o financeiro será atualizado, confirmando que a empresa já está com o plano ativo e pode utilizar o sistema.

---

## 50. Gerando etiqueta de produtos

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV, Filial |

### Funcionalidade de Gerar Etiquetas
O sistema permite gerar etiquetas de produtos com diferentes padrões. É possível cadastrar vários modelos de etiqueta, que podem ser importados na tela de modelos de etiqueta. Caso a empresa não importe, ela pode criar novos modelos.

### Edição de Formulário
Ao editar um formulário, existem campos que podem ser selecionados para aparecer na etiqueta. É possível escolher exibir o valor do produto e o nome. O usuário pode optar por não mostrar o nome do produto e, em vez disso, exibir o código de barras numérico.

### Geração de Etiquetas na Lista de Produtos
Para gerar etiquetas na lista de produtos, é necessário escolher um item que tenha um código de barras cadastrado. Após selecionar o modelo, os campos disponíveis serão exibidos e podem ser editados conforme a necessidade.

### Geração de Etiquetas nas Compras
Na área de compras, existe um botão específico para gerar etiquetas. O usuário deve selecionar o modelo desejado e os itens que deseja imprimir, facilitando o processo de geração de etiquetas.

---

## 51. Importação de XML NFe e NFCe arquivo ZIP

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV, Filial |

### Importação de Arquivo XML NFe e NFCe

O vídeo demonstra a funcionalidade de importação de arquivos XML, que pode ser utilizada tanto para vendas quanto para NFCe. Para NFe, é necessário que o arquivo esteja compactado no formato ZIP. O sistema permite a importação de registros de NFe, cadastrando automaticamente clientes e produtos, além de faturas. Caso não deseje importar algum registro, é possível desmarcá-lo.

### Seleção de Local e Geração de Documentos Fiscais

Após selecionar o arquivo ZIP, é obrigatório escolher um local para salvar os registros. O sistema traz os registros disponíveis e permite a geração de Documentos Fiscais (DF), tanto na versão simples quanto na versão padrão A4. Para NFCe, o arquivo ZIP deve conter apenas documentos do modelo 65, caso contrário, ocorrerá um erro.

### Status e Conta a Receber

Após a importação, os registros já vêm com status aprovado. O sistema também gera contas a receber com a data da fatura. Se a data for anterior ao dia atual, o status da fatura será marcado como pago. Essa funcionalidade é considerada uma adição interessante ao sistema.

---

## 52. Módulo reservas   para hoteis e pousadas

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV, Filial, Reservas, Hoteis, Pousadas |

### Módulo de Reservas para Hotéis e Pousadas
O vídeo demonstra um novo módulo de reservas utilizado para hotéis. Este módulo possui uma tela de configuração padrão, semelhante à do card livre, onde é possível realizar diversas configurações e inserir dados importantes para impressão.

### Cadastro de Acomodações
No cadastro da acomodação, é necessário preencher informações como nome, número, capacidade, valor, área, identificação do estacionamento, categoria, status e descrição do quarto. É possível definir um frigobar específico para cada acomodação, que será utilizado durante o check-in do cliente. Os produtos que podem ser utilizados nas reservas devem estar marcados na opção "outros reserva".

### Processo de Reserva
Na tela principal de reservas, é possível criar uma nova reserva selecionando a data e a quantidade de hóspedes. O sistema apresenta os quartos disponíveis com base nas informações fornecidas. Após selecionar o quarto, é possível cadastrar um novo cliente ou escolher um já cadastrado. O valor da estadia é fixo, mas pode ser modificado posteriormente durante a reserva.

### Check-in e Consumo
Após a criação da reserva, é possível iniciar o check-in. O sistema permite que o atendente preencha as informações dos hóspedes ou que um link seja enviado para que o cliente preencha os dados. Durante a estadia, é possível adicionar produtos e serviços consumidos, além de observações. A impressão dos dados da reserva, produtos consumidos e serviços totais também está disponível.

### Geração de Notas Fiscais
O sistema permite gerar uma Nota Fiscal Eletrônica (NFE) de consumo, onde é necessário preencher a natureza da operação e o valor de pagamento. É possível utilizar mais de um tipo de pagamento. Após a finalização, a NFE fica pronta para transmissão, e o estado da reserva pode ser alterado para checkout, permitindo a visualização de dados de serviços e produtos.

---

## 53. Transferência de estoque entre localizações

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV, Filial |

### Configuração de Localizações
No sistema, é necessário que o usuário tenha mais de uma localização atribuída para realizar a transferência de estoque. As localizações devem ser configuradas previamente no sistema.

### Realizando a Transferência de Estoque
Para iniciar a transferência de estoque, acesse o menu lateral, selecione "Produtos" e clique em "Transferência de Estoque" e, em seguida, "Nova Transferência". Escolha a localização de saída e a localização de entrada.

### Adicionando Itens à Transferência
Na tela de transferência, é possível adicionar itens. Selecione o item que deseja transferir, informe a quantidade e clique em "Salvar". É possível transferir mais de um item, bastando preencher os campos de saída, entrada e quantidade para cada item.

### Atualização de Estoque
Após a transferência, o sistema atualiza automaticamente as quantidades nas localizações. Por exemplo, se um item tinha 40 unidades na localização um e foram transferidos 10, a nova quantidade será 30 na localização um e 10 na localização dois. O item também será incluído na nova localização, caso não estivesse previamente atribuído.

---

## 54. Valores de atacado para produtos

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV, Filial |

### Funcionalidade de Valor de Atacado
A nova funcionalidade no sistema permite configurar o valor de atacado para os itens. É possível definir um valor padrão para o item, por exemplo, R$ 3,00. Caso a quantidade de itens seja alterada para três ou mais, o sistema aplicará automaticamente o valor de atacado configurado.

### Cadastro do Produto
O valor de atacado é definido no cadastro do produto. No cadastro, é possível visualizar o valor de venda padrão, o valor de atacado e a quantidade necessária para que o valor de atacado seja aplicado. Para três itens ou mais, o sistema assume o valor de atacado.

### Aplicação no PDV e Vendas
Essa funcionalidade funciona tanto no ponto de venda (PDV) quanto nas vendas que geram a Nota Fiscal Eletrônica (NFE). No menu Vendas, ao selecionar o item e definir uma quantidade maior, o sistema aplicará o valor de atacado conforme configurado.

---

## 55. Manifestação do destinatário   busca de arquivos XML

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, delivery, angular, mercadolivre, Angular, PDV, Filial |

### Funcionalidade de Busca de Arquivos XML
A funcionalidade de busca de arquivos XML permite consultar as compras realizadas para o CNPJ configurado no sistema. Essa opção está disponível no menu "Compras" ou "Compras Manifesto". Ao clicar em "Nova Consulta", é possível iniciar uma nova busca, mas é importante observar que não é permitido realizar consultas em intervalos menores que uma hora.

### Realizando a Ciência de Itens
Após realizar uma consulta, é possível visualizar os itens que ainda não foram manifestados. Para manifestar um item, é necessário selecionar a opção de ciência. O sistema oferece a opção de completar a ciência, que consiste na importação do XML. Ao completar, o sistema traz automaticamente o fornecedor e todos os produtos contidos no XML. Se o fornecedor não estiver cadastrado, ele será adicionado ao sistema.

### Cadastro de Produtos e Dados de Frete
Durante o processo de importação do XML, o sistema identifica os produtos a serem cadastrados e os dados de frete, caso existam. É necessário escolher a natureza da operação para finalizar o cadastro. Após essa etapa, a compra é registrada no sistema.

### Limitações na Importação
Se uma tentativa de completar a importação for feita novamente após já ter sido realizada, o sistema não permitirá a ação. Além disso, é possível visualizar todos os itens e dados do XML, mas não será possível realizar uma nova importação para itens que já foram processados.

---

## 56. Novo template para delivery

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular |

### Novo Template para Delivery
O vídeo apresenta um novo template para o módulo de delivery, que é mais amigável e responsivo. O apresentador menciona que deixará na descrição o link para o primeiro vídeo sobre delivery, que contém mais detalhes sobre o painel e as configurações.

### Demonstração de Compra
O apresentador demonstra uma compra utilizando o novo template. Ele simula o modelo desktop e destaca que a forma de inclusão de itens foi alterada para um formato modal. No dispositivo mobile, é possível adicionar adicionais, quantidade e observações opcionais.

### Identificação do Cliente
O sistema permite a identificação do cliente através do telefone. Se o telefone já estiver cadastrado, o cliente é redirecionado para a tela de pagamento. Caso contrário, o sistema apresenta campos em branco para o preenchimento de CPF e endereço.

### Configuração de Endereço
O usuário pode definir um endereço como padrão em sua conta. Ao retornar ao carrinho, o endereço selecionado já aparece preenchido, juntamente com outras informações relevantes. O sistema também monta um cupom automaticamente caso haja alterações.

### Formas de Pagamento
O sistema está integrado com o Mercado Pago, permitindo pagamentos via Pix pelo aplicativo, além de outras opções. No menu de delivery, é possível configurar todos os tipos de pagamento disponíveis para o usuário escolher. O apresentador finaliza a compra selecionando a opção de pagamento em dinheiro e menciona a possibilidade de inserir um código de desconto.

---

## 57. PDV   Venda suspensa e trocas

**Tags:** Multiempresa, Multifilial, Laravel, PHP, NFe, NFCe, Cte, MDFe, Automacao, ionic, comandas, delivery, angular |

### Funcionalidade de Venda Suspensa
Neste vídeo, são apresentadas duas novas funcionalidades para o PDV: a troca e a venda suspensa. Para realizar uma venda suspensa, o usuário deve adicionar itens à venda e selecionar um tipo de pagamento, que agora é dinâmico nas configurações gerais. Caso não consiga finalizar a venda, é possível suspender a venda. O botão "Vendas Suspensas" abre uma modal com todas as vendas suspensas, permitindo ao usuário remover ou finalizar a venda.

### Funcionalidade de Troca
Para realizar uma troca, o usuário deve informar o código da venda ou o número da NFC-e. O sistema traz os detalhes da venda para efetuar a troca. O cliente e o vendedor não podem ser alterados, pois a venda já foi realizada. Se um cliente devolver um item, como uma Pita Set, o sistema gera um crédito de R$ 44, que pode ser utilizado em uma nova venda. O usuário também pode adicionar um novo item durante a troca, e o sistema calculará o valor a pagar restante.

### Finalização da Troca
Ao finalizar a troca, o sistema gera um comprovante que inclui os itens alterados, o valor da troca e o valor a pagar. Por exemplo, se o usuário adicionar um item de valor semelhante, como R$ 9, o sistema mostrará o valor restante a pagar, que seria R$ 37.

---

## 58. App de controle de comandas

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Demonstração do App de Controle de Comandas
Este vídeo é uma demonstração do aplicativo de controle de comandas, desenvolvido para o módulo de cardápio. Ao acessar, nas configurações, será solicitado uma senha. É necessário inserir a URL do servidor, que pode ser "localhost", o token de configuração do módulo e o código do garçom. Este código deve ser único para cada funcionário, pois é utilizado para identificar quem lançou os itens na comanda. O preenchimento deste campo é opcional, mas é importante para a identificação.

### Abertura de Comandas
Para abrir uma comanda, clique no botão "mais". É necessário inserir o telefone do cliente; se o cliente já estiver cadastrado, o nome será preenchido automaticamente. Caso contrário, preencha com um nome qualquer para habilitar o botão. Insira o número da comanda e o número da mesa (opcional). A comanda ficará aberta na tela de pedidos.

### Adição de Itens na Comanda
Na tela de pedidos, escolha um produto simples para adicionar. Também é possível adicionar produtos com adicionais, se definido no cardápio. Para pizzas, o sistema divide o valor total entre as partes, conforme a configuração do cardápio. Após adicionar os itens, é possível removê-los, se necessário.

### Fechamento da Comanda
Para fechar a comanda, clique na opção correspondente. O sistema solicitará confirmação para fechar a comanda. Após a confirmação, uma mensagem será exibida para o atendente, indicando que a comanda deve ser fechada.

### Registro de Atendimentos
Na seção de atendimento do garçom, serão exibidos todos os atendimentos realizados. É possível filtrar por data, visualizar a comanda atendida, o produto, subtotal, valor e quantidade do item. Todas essas informações ficam registradas no sistema.

---

## 59. TEF para o PDV

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Configuração do TEF no PDV
Neste vídeo, é demonstrada a funcionalidade de TEF no PDV, desenvolvido com a API da Multiplus Card. Para configurar, é necessário inserir o CNPJ do PDV e o token fornecido pela Multiplus Card, vinculando essas informações ao usuário. Cada usuário pode ter um token, PDV ou CNPJ diferente.

### Ativação do TEF
Para que o TEF funcione, é preciso que a configuração esteja ativa para o usuário. Ao acessar o PDV, ele verifica se o TEF está ativo. Se estiver, aparecem as opções de pagamento: cartão de crédito, débito e PIX TEF. Se a configuração não estiver ativa ou se houver algum erro, essas opções não serão exibidas.

### Realização de Vendas com TEF
Ao realizar uma venda, por exemplo, de um item que custa 10 centavos, é possível escolher a opção de débito TEF. O sistema inicia a comunicação com o TEF e solicita que o cartão seja inserido ou aproximado. Após a transação ser aprovada, o usuário pode escolher entre emitir um cupom fiscal ou não fiscal.

### Registros de TEF
No PDV, há uma seção de registros de TEF que mostra todas as transações realizadas. É possível visualizar detalhes como a venda feita, o horário e a opção de cancelamento, caso necessário.

### Desativação do TEF
Se o usuário não quiser utilizar o TEF, é possível editar a configuração e mudar o status para desativado. Com isso, ao acessar o PDV, não haverá requisição ao TEF, permitindo que o sistema inicie normalmente, sem a demora de três a cinco segundos.

---

## 60. Produto tipo único Imei, serial, etc

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Funcionalidade de Produto Tipo Único
Neste vídeo, é demonstrada a funcionalidade de produtos do tipo único, que permite marcar um item como tendo identificação única, como um celular com IMEI. Essa configuração é essencial para rastrear produtos que possuem um código único.

### Cadastro de Produto
Para cadastrar um produto do tipo único, como um celular, é necessário definir um valor de compra e marcar a opção de tipo único. Após salvar, é possível realizar a compra desse item.

### Processo de Compra
Ao realizar a compra de um produto do tipo único, como dois celulares Samsung, o sistema apresenta uma tela onde é possível inserir as identificações. Cada celular terá uma linha correspondente, permitindo o registro dos códigos únicos.

### Pesquisa de Produtos
Após cadastrar os códigos, é possível pesquisar pelo produto no sistema. A pesquisa retornará todos os códigos únicos cadastrados, como 8989 e 8998, que ainda estão disponíveis para venda.

### Venda de Produtos
Na hora de vender, o sistema redireciona para uma tela onde os códigos dos celulares disponíveis são exibidos. Ao digitar parte do código, como 89, o sistema traz os códigos correspondentes. Após selecionar um código e salvar, é possível consultar as informações de compra e venda, mostrando quando cada item foi adquirido e vendido.

---

## 61. API Rest

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Criação de Tokens para API
Neste vídeo, é apresentada a nova funcionalidade de criação de tokens para a API do sistema. O token é gerado através de um botão e deve estar ativo para realizar requisições. Inicialmente, a API oferece acesso a categorias de produtos, produtos, clientes, fornecedores, vendas de PDV, usuários e caixa.

### Estrutura das Requisições
As requisições são organizadas em collections do Postman, com pastas específicas. Por exemplo, para o cadastro de produtos, é necessário passar parâmetros obrigatórios e opcionais. O tipo de requisição pode ser GET ou POST. Para buscar todos os produtos, a requisição retorna um objeto, e para buscar por ID, é necessário passar o parâmetro de autorização com o valor do token.

### Cadastro de Produtos
Para cadastrar um novo produto, é necessário informar o nome e o valor unitário, que são os únicos campos obrigatórios. Outros parâmetros, como valor de compra e categoria, são opcionais. Se não forem fornecidos os parâmetros obrigatórios, a requisição retornará um erro. O sistema também permite a configuração de um padrão fiscal, que deve ser definido na empresa.

### Logs de Requisições
O sistema registra logs das requisições, ordenando-as pela data mais recente. Os logs mostram o tipo de operação (criação, erro, etc.) e o status da requisição. Em caso de erro, a mensagem de erro é exibida em destaque. É possível filtrar os logs por tipo e local, como clientes e fornecedores.

---

## 62. Margem de comissão e outras funções

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Clone das Vendas
No sistema, há uma funcionalidade que permite clonar vendas. Ao clicar no último botão na seção de vendas, a venda será duplicada. É possível adicionar novos itens e alterar a fatura. Além disso, existe a opção de gerar a fatura, que abrirá uma modal onde é possível definir um valor de entrada (opcional), a quantidade de parcelas, o intervalo de vencimento, a data do primeiro vencimento e o tipo de pagamento. Por exemplo, se for definido um valor de entrada de R$ 300, com cinco parcelas, o intervalo de dias padrão é de 30. Caso não seja escolhida uma data de vencimento, o sistema assumirá a data atual. O tipo de pagamento pode ser alterado para crediário ou dinheiro, e as parcelas serão geradas de acordo com as configurações.

### Configuração de Comissão
A configuração de comissão no sistema pode ser ajustada. Anteriormente, a comissão era definida por vendedor, acessando Gestão Pessoal > Funcionários. Agora, é possível mudar para comissão por margem de lucro. Por exemplo, se um item tem uma margem de 50%, o vendedor receberá 10% de comissão. Se a margem for de 75%, a comissão será de 15%. Essa configuração é feita na seção de margem e percentual de comissão. Quando uma venda é realizada no PDV, o sistema verifica a margem de cada item e atribui o percentual de comissão conforme configurado.

---

## 63. Controle de fretes

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Módulo de Frete
Neste vídeo, é demonstrado o módulo de controle de fretes. O usuário pode iniciar um novo frete e lançar despesas. Existe um cadastro para o tipo de despesa, que inclui nome e status, permitindo a geração de relatórios filtrados por período e tipo de despesa.

### Geração de Contas
Após salvar um frete, é possível visualizar opções para gerar a conta a receber. O sistema permite a impressão de documentos em diversos formatos, como imagem e PDF. Caso um fornecedor seja selecionado, também é possível gerar a conta a pagar. Se o fornecedor não for definido, a opção de gerar a conta a pagar não estará disponível.

### Manutenção de Veículos
O módulo também permite a manutenção de veículos. Para editar a manutenção, é necessário informar o fornecedor e o veículo. O sistema oferece opções de desconto e acréscimo, além de permitir a adição de serviços e produtos. Após salvar, é possível visualizar a conta a pagar gerada pela manutenção, realizar upload de documentos e imprimir, além de alterar o estado da manutenção.

---

## 64. Novo layout PDV

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Novo Layout do PDV
Foi desenvolvido um novo template para o PDV, com diferenças principais nas paginações de produtos e categorias de marcas.

### Finalização de Venda
Ao realizar uma venda, é possível buscar o item por código de barras ou nome. A finalização é semelhante à versão anterior, mas nesta nova versão, a finalização requer a abertura de uma modal, ao contrário da versão anterior que tinha a opção de finalizar rapidamente. Na modal, é necessário selecionar o tipo de pagamento, que já apresenta o valor integral da venda. As opções de CPF e CNPJ são opcionais.

### Configuração Geral
Na configuração geral, o layout padrão é o "Light", mas também existe a opção de alerta sonoro (bip) quando um produto é incluído ou quando ocorre um erro, como "estoque insuficiente". Se o layout for alterado para "Pup", a nova versão do PDV é exibida. O bip de erro é acionado em casos de estoque insuficiente. É possível desativar o bip, permitindo apenas o alerta visual.

---

## 65. Melhorias   Configuração de email por empresa e envio de XML para contador

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Configuração de E-mail por Empresa
Neste vídeo, foi demonstrada uma melhoria na configuração de e-mail do sistema. Anteriormente, o sistema utilizava apenas a configuração do e-mail do ENV para o envio de documentos como NFe e cotações. Agora, o usuário pode inserir seu próprio e-mail nas configurações. Há uma opção para ativar ou desativar essa configuração. Se desativada, o sistema voltará a usar o e-mail do ENV. Se ativada, o envio será feito utilizando as informações inseridas pelo usuário.

### Envio Automático de XML para Contador
Outra melhoria apresentada é a funcionalidade de envio automático do XML para o escritório contábil. Ao transmitir uma NFe, se a opção estiver marcada como "sim" e um e-mail estiver configurado, o XML será enviado automaticamente para o e-mail do contador. Isso se aplica a NFe, NFCe, CTe e MDF-e. Além disso, no super admin, será possível visualizar a lista de todos os escritórios contábeis definidos pelas empresas, facilitando o contato com o contador e a gestão das empresas.

### Envio de XML de Forma Simplificada
Foi implementada uma nova funcionalidade que simplifica o envio de XML. Anteriormente, era necessário baixar o XML manualmente para enviá-lo por e-mail. Agora, um botão foi adicionado que abre uma modal com o e-mail do cliente, mas isso só aparece se a NFe estiver aprovada. O usuário pode alterar o e-mail, e as opções de arquivo a serem enviadas já vêm marcadas por padrão. Essa funcionalidade foi implementada tanto para NFe quanto para a lista de NFCe. Se a NFCe não tiver um cliente associado, o usuário precisará digitar manualmente o e-mail para o envio.

---

## 66. Auto Agendamento Marketplace

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Cadastro de Funcionários
No sistema, o primeiro passo para utilizar a funcionalidade de agendamento de serviços é cadastrar os funcionários que irão trabalhar. É necessário que esses funcionários estejam ativos. Após o cadastro, é preciso definir os dias de atendimento de cada funcionário e cadastrar as interrupções, como horários de almoço e café. É possível ter várias interrupções por dia para cada funcionário. As interrupções devem ser ativadas ou desativadas, e apenas as ativas aparecerão nos horários de funcionamento. Caso os horários de funcionamento não estejam cadastrados, o funcionário não aparecerá na hora de escolher o agendamento.

### Configuração do Agendamento
A configuração do agendamento é um passo importante. Um dos elementos essenciais é o token do WhatsApp, que, embora não seja obrigatório, é importante para o envio de mensagens. O sistema permite enviar uma mensagem às 8 horas da manhã para avisar sobre o agendamento e outra mensagem 30 minutos antes do horário agendado. Também é possível definir um tempo de descanso entre um agendamento e outro.

### Agendamento de Serviços
O processo de agendamento de serviços é semelhante ao de produtos. Ao cadastrar um serviço, é necessário preencher campos opcionais, como tributação, e definir se o serviço será listado no Marketplace. Ao adicionar um serviço, como um corte de cabelo, o sistema traz o tempo de execução, que pode ser, por exemplo, 35 minutos. Ao buscar horários disponíveis, o sistema mostrará os horários do atendente selecionado. É possível filtrar por atendente e escolher um horário específico.

### Finalização do Agendamento
Após selecionar o horário, o sistema simula a finalização do agendamento, semelhante ao processo de delivery. O usuário deve escolher uma forma de pagamento, que pode ser configurada previamente no sistema. Após a escolha, o agendamento é criado e aparece tanto no menu de delivery quanto na lista de agendamentos no calendário. O sistema permite alterar o estado do agendamento, finalizar no PDV e imprimir os detalhes do serviço.

---

## 67. Menu horizontal com cores

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Melhorias no Layout do Sistema
Neste vídeo, foram apresentadas duas melhorias no sistema. A primeira é uma atualização no layout, onde agora é possível escolher entre um menu vertical ou horizontal. Além disso, foram incluídas mais duas opções de cores, além do padrão Light: o Dark e uma terceira cor. A escolha de deixar apenas os ícones no menu foi feita para evitar que os nomes, como "ícone de ordem de serviço" e "ícone de agendamento", tornassem a barra de rolagem muito extensa.

### Melhorias no PDV
A segunda melhoria foi implementada no ponto de venda (PDV), tanto no modelo antigo quanto no novo. Foi adicionado um botão chamado "gerar fatura", que permite incluir um valor de entrada opcional. O usuário pode definir um valor de entrada, a quantidade de parcelas e o intervalo de vencimento do primeiro pagamento, além de escolher o tipo de pagamento. Após clicar em "gerar", a fatura é criada e as parcelas são exibidas no cupom.

---

## 68. Metas de vendas e ordem de serviço

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Cadastro de Metas
O sistema agora possui um cadastro de metas, que pode ser configurado por funcionário. É possível definir metas para vendas e ordens de serviço. Por exemplo, para o funcionário Marcos, a meta de vendas é de R$ 20.000. No módulo de vendas, é possível visualizar o período atual, que é o mês 1 de 2025, a meta geral de R$ 25.000 e o total vendido até o momento, que foi de R$ 4. A meta pode ser filtrada por mês e por funcionário.

### Metas de Ordem de Serviço
As metas para ordens de serviço são configuradas da mesma forma que as metas de vendas. Isso permite um acompanhamento mais eficiente do desempenho em relação às metas estabelecidas.

### Importação de XML
O sistema agora permite a importação de XML de compras. Ao importar um XML, todos os produtos já cadastrados no sistema são reconhecidos. Além disso, é possível alterar o cadastro do produto durante a importação. Por exemplo, se o nome ou a categoria de um produto for alterado, essas mudanças serão salvas automaticamente no cadastro. Caso o produto não esteja cadastrado, é possível vinculá-lo, e o sistema trará os dados correspondentes para facilitar o cadastro. Isso agiliza o processo de importação.

---

## 69. Dados do produto por localização

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Funcionalidade de Valores por Localização
Neste vídeo, é demonstrada uma funcionalidade solicitada pelos clientes, que permite alterar os valores dos produtos, como valor de venda, percentual de CMS, PIS, CST e outras variáveis, por localização. 

### Acesso à Tela de Valores por Local
Para acessar essa funcionalidade, é necessário habilitar o botão "Valores por Local" na lista de produtos. Essa tela é opcional e não precisa ser acessada se não houver necessidade de alterar o valor de venda ou outros atributos por localização.

### Alteração de Valores por Localização
No exemplo apresentado, a empresa possui duas localizações ativas. O valor de venda e os CSTs e percentuais de PIS e CMS podem ser alterados conforme a localização. Por exemplo, o valor padrão do produto é R$ 3,51, mas na segunda localização, o valor é R$ 4,30.

### Realização de Vendas com Valores Diferentes
Ao abrir o caixa na segunda localização e selecionar um cliente, o sistema já traz o valor e os percentuais de CMS e CST diferentes, considerando que a segunda localização está sob regime normal e a primeira sob regime simples. Ao salvar a venda, o sistema gera um XML temporário com o valor de R$ 4,30 e os dados de PIS, Cofins e CST definidos para aquela localização.

### Integração com PDV
A funcionalidade também se aplica ao PDV. Ao abrir o caixa na segunda localização, o item já aparece com o valor de R$ 4,30 e os dados de PIS, Cofins e CST são salvos conforme as definições da tela de valores por local.

---

## 70. App força de vendas

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Melhoria no App de Força de Vendas
O vídeo apresenta uma melhoria no aplicativo, que agora inclui uma funcionalidade de força de vendas. Ao abrir o aplicativo pela primeira vez, o usuário é direcionado para o controle de comandas, mas pode mudar para a força de vendas. Essa configuração permite que o menu exiba opções como clientes, produtos e orçamentos.

### Funcionamento Offline
O aplicativo funciona de forma offline, permitindo que o usuário visualize e salve informações sobre clientes e produtos mesmo sem conexão com o servidor. Quando a conexão é restabelecida, os dados, como clientes e orçamentos não cadastrados, são enviados automaticamente para o servidor.

### Cadastro e Filtragem de Clientes
No módulo de clientes, é possível cadastrar novos clientes, que possuem campos idênticos aos da versão web. O usuário também pode filtrar a lista de clientes cadastrados.

### Gerenciamento de Produtos e Orçamentos
No módulo de produtos, o usuário pode filtrar os produtos disponíveis, mas não tem a opção de cadastrar novos produtos. Já no módulo de orçamentos, é possível incluir, editar e remover orçamentos. Os orçamentos são associados ao funcionário que está logado no aplicativo.

### Criação e Edição de Orçamentos
Para criar um novo orçamento, o usuário precisa selecionar um cliente e pelo menos um produto. Há campos opcionais para observações, desconto e fatura. Após preencher as informações, o orçamento pode ser salvo, editado ou removido. O aplicativo também permite imprimir orçamentos, incluindo o nome do funcionário responsável. A conversão de orçamentos em vendas só pode ser realizada na versão web do sistema.

---

## 71. Contrato de lincença

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Funcionalidade do Super Admin
Neste vídeo, é demonstrada a funcionalidade para o super admin criar um contrato que define os limites de dias para assinatura. Quando o cliente acessa o sistema, aparece um botão para assinatura. Se o prazo expirar, o cliente será redirecionado para a tela de assinatura, onde deve concordar com os termos para continuar utilizando o sistema.

### Variáveis do Contrato
O super admin pode utilizar algumas variáveis no contrato, como "%nome%" para substituir pelo nome da empresa e "%nome_fantasia%" para o nome fantasia. É possível adicionar texto estático ao contrato, além de definir o status como ativo ou inativo. Se o contrato estiver inativo, a empresa não precisará concordar novamente.

### Limites de Dias para Assinatura
O super admin pode definir um limite de dias para a assinatura do contrato. Se o limite for definido como zero, a empresa será obrigada a assinar para continuar utilizando o sistema. Caso contrário, mesmo com um alerta na página inicial, a empresa poderá usar o sistema normalmente.

### Processo de Assinatura
Quando o limite de dias é alterado para zero e a página é atualizada, o usuário será redirecionado para a assinatura do contrato. Após aceitar os termos e confirmar, a mensagem de assinatura não aparecerá mais, permitindo o uso contínuo do sistema.

### Lista de Contratos
O sistema possui uma lista de contratos que exibe todos os contratos criados. É possível filtrar os contratos por data, empresa e estado. O contrato é gerado automaticamente quando a empresa faz login, caso ainda não tenha um contrato assinado.

---

## 72. Tributação por cliente

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Funcionalidade de Tributação no Cadastro do Cliente
Neste vídeo, é demonstrada uma funcionalidade no cadastro do cliente relacionada à tributação. Existem campos para ICMS e PIS, que são opcionais e servem para a emissão de Notas Fiscais Eletrônicas (NFe). Ao selecionar um cliente, o sistema avisa se deseja utilizar os dados de percentual de ICMS e PIS definidos para aquele cliente.

### Definição de Tributação Específica
Caso um cliente tenha uma tributação específica, não é necessário alterar as informações na hora de gerar a Nota Fiscal. Ao realizar uma nova venda e selecionar um cliente, o sistema pergunta se deseja utilizar a tributação padrão ou a definida para o cliente. Se a opção "sim" for escolhida, o sistema buscará os dados de tributação do cliente em vez dos dados do produto.

### Comportamento do Sistema em Relação ao CST
Se o CST de Cofins não estiver definido no cadastro do cliente, o sistema utilizará o CST do produto. Por exemplo, se o CST estiver marcado como 10 no cadastro do cliente, essa informação será utilizada. Caso contrário, o sistema buscará a informação do produto.

### Aplicação da Funcionalidade em Vendas e PDV
Essa funcionalidade é aplicável tanto para vendas quanto para o ponto de venda (PDV). Ao selecionar um cliente, na hora de gerar a Nota Fiscal de Consumidor Eletrônica (NFC-e), o sistema perguntará se deseja utilizar a tributação do produto ou a definida para o cliente. A principal aplicação dessa funcionalidade é para a NFe, já que a NFC-e não exige a escolha do cliente.

---

## 73. Impressão sem Janela no PDV e Comandas

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Funcionalidade de Impressão sem Janela
O vídeo demonstra a funcionalidade de impressão sem janela, que foi implementada no PDV e na comanda. Futuramente, a intenção é expandir essa funcionalidade para a cozinha, permitindo que uma impressora conectada a uma máquina busque novos pedidos automaticamente.

### Configuração da Impressão sem Janela
Para ativar a impressão sem janela, é necessário acessar as configurações e marcar a opção "impressão sem janela" como sim. É importante utilizar o navegador Firefox com a propriedade definida como verdadeira ou o Chrome em modo quiosque. No Firefox, a configuração padrão é falsa, e deve ser alterada para true através de um duplo clique.

### Realização de Vendas no PDV
Após a configuração, ao realizar uma venda no PDV, ao clicar para imprimir, não será aberta uma janela. Em vez disso, o sistema emitirá um som de impressão e a impressora conectada realizará a impressão automaticamente. O mesmo processo se aplica à comanda, onde a impressão ocorre diretamente ao clicar na opção de imprimir.

---

## 74. Impressão automatica delivery e comandas

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Configuração da Impressão Automática
O primeiro passo para configurar a impressão automática dos pedidos de cardápio e delivery no sistema é ativar a propriedade no navegador, definindo-a como true. Essa configuração pode ser feita tanto no Firefox quanto no Chrome, utilizando o modo kiosk. Existem diversos tutoriais disponíveis sobre como ativar o modo kiosk.

### Registro de Impressoras
Após ativar a impressão automática, acesse o menu de configuração de impressoras de pedido e registre uma nova impressora. Ao editar uma impressora existente, como a da cozinha, você encontrará campos para a descrição, status ativo e itens a serem impressos. É possível selecionar quais itens serão impressos por cada impressora, permitindo que a cozinha e o bar imprimam itens diferentes, ou até mesmo excluir determinados itens da impressão.

### Controle de Impressão
Dentro do menu cardápio e delivery, há um submenu chamado controle de impressão. Ao clicar nele, será exibida uma tela listando todas as impressoras ativas, como a da cozinha e do bar. É necessário clicar em uma impressora para iniciar a impressão e registrar os logs. A tela de controle de impressão deve estar aberta em uma nova aba para que as requisições ao banco de dados sejam realizadas corretamente.

### Adição de Itens e Impressão
Ao adicionar um item a uma comanda que já está aberta, se o item for da cozinha, a impressão será realizada automaticamente e o log será armazenado. Caso um item que não pertence à cozinha seja adicionado, ele não será impresso. O mesmo processo se aplica ao delivery, onde é necessário confirmar o pedido para que a impressão ocorra. Ao aprovar o pedido, apenas os itens correspondentes à impressora selecionada serão impressos.

---

## 75. Categoria para adicionais de delivery

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Funcionalidade de Categorias para Adicionais de Delivery
O vídeo demonstra uma nova funcionalidade no sistema de delivery que permite separar os adicionais por categoria. É possível definir limites mínimos e máximos para a escolha desses adicionais ao adicionar itens ao carrinho.

### Configuração de Mínimo e Máximo
Ao acessar as categorias de adicionais, é possível editar uma categoria, como "frutas", onde se pode definir o mínimo e o máximo de itens que o cliente pode escolher. Esses campos podem ser deixados em branco caso não se queira trabalhar com limites. No exemplo, o mínimo é definido como 1 e o máximo como 2.

### Adicionando Itens ao Carrinho
Ao tentar adicionar itens ao carrinho, se o cliente não selecionar o número mínimo de itens exigido, uma mensagem de alerta será exibida, como "selecione ao menos um item para adicional frutas". Durante o cadastro dos adicionais para os produtos, é possível buscar os adicionais ou adicionar todos os itens de uma categoria de uma só vez.

### Exemplo de Adição de Itens
No exemplo, ao selecionar a categoria "frutas", o sistema adiciona automaticamente os itens abacaxi, morango, uva e banana. Se o cliente tentar adicionar mais itens do que o máximo permitido, como no caso de abacaxi, morango e uva, o sistema alertará que o máximo é dois. O cliente deve então ajustar a seleção para atender ao limite e prosseguir com a adição ao carrinho.

---

## 76. Cárdapio QR Code

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Introdução ao Cardápio por QR Code
Neste vídeo, é demonstrado um novo modo de utilização do cardápio, que agora pode ser acessado por QR Code. Anteriormente, o cardápio era disponibilizado por meio de tablets, um para cada mesa, utilizando o aplicativo de autoatendimento.

### Cadastro de Mesas e Geração de QR Code
No menu "Cardápio", foi incluído o cadastro de mesas, que é um processo simples. Ao abrir o formulário, é possível gerar o QR Code, que representa um link. Ao escanear o QR Code, é possível imprimir e colocar na mesa, permitindo que o sistema identifique qual mesa está sendo utilizada.

### Configuração do Módulo de Cardápio
Na configuração, existe a opção de ativar o módulo do cardápio e definir o limite de uso do QR Code. É possível ter até duas pessoas utilizando o mesmo QR Code simultaneamente.

### Realização de Pedidos
Ao adicionar um item ao carrinho, é necessário informar o nome e o celular da pessoa. Se um segundo item for adicionado, o envio não será possível até que a mesa seja liberada. No menu "Cardápio", na tela de pedidos, é possível visualizar as comandas pendentes de liberação.

### Notificações e Liberação de Mesas
Caso a notificação por usuário esteja ativada, ao editar o usuário logado, uma modal será exibida quando houver uma nova mesa a ser liberada. Após clicar em "Liberar Mesa", a mesa será liberada e o carrinho poderá ser atualizado para permitir o envio do pedido novamente.

### Finalização de Pedidos
Os pedidos podem ser finalizados separadamente. Ao clicar na comanda de um usuário, como Marcos, o sistema abrirá o PDV apenas com os itens desse usuário. Após a finalização, o sistema redireciona para a tela principal, onde é possível finalizar o pedido de outro usuário, como João. O modelo de visualização no dispositivo móvel é semelhante ao utilizado no delivery.

---

## 77. Configuração numeração e número de serie de NFCe para usuário e Captcha

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Cadastro de Usuário e Configuração Fiscal
No cadastro do usuário, no menu "Usuários" e em "Configuração Fiscal", é possível cadastrar os parâmetros de DNFC, o último número e o número de série por usuário. Ao cadastrar essas informações, o sistema utilizará os dados do usuário logado, em vez de pegar os dados do último número de NFC da configuração do emitente.

### Configuração de Captcha
Outra configuração realizada foi a inclusão do Captcha, que agora está disponível no cadastro da empresa, permitindo a configuração ao cadastrar um novo usuário.

---

## 78. Emissão de NFe no PDV

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Ajuste na Emissão de NFCE no PDV
A partir de novembro de 2025, não será mais permitido a emissão de NFCE para CNPJ. Ao selecionar um cliente que seja CNPJ, o sistema informará automaticamente que será emitida uma NFE em vez de uma NFCE.

### Configuração Geral do Documento no PDV
Na configuração geral, no menu de documentos do PDV, por padrão, está selecionado NFC. Se a opção NFE for marcada, todos os documentos fiscais emitidos passarão a ser NFE, desde que um cliente esteja selecionado. Não é permitido emitir uma NFE sem um cliente definido.

### Comportamento ao Selecionar Clientes
Se um cliente CNPJ for selecionado, independentemente da configuração padrão, o sistema emitirá uma NFE. Caso a opção NFE esteja marcada, ao definir qualquer tipo de cliente, o sistema também emitirá NFE em vez de NFCE no PDV.

---

## 79. PDV para comandas e mesas

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Objetivo do PDV para Comandas
O vídeo demonstra um PDV desenvolvido para comandas, com o objetivo de facilitar a alternância entre as comandas e a adição de novos itens. O sistema permite que o usuário não precise voltar entre as telas, tornando o processo mais ágil.

### Acesso e Adição de Itens
No menu Pedidos, na opção Comandas, é possível abrir uma comanda existente e adicionar novos itens. O usuário pode clicar sobre uma comanda já aberta e incluir itens, como pizzas, mantendo os sabores definidos. Também é possível criar uma nova comanda e adicionar itens rapidamente, incluindo detalhes e adicionais.

### Finalização do Pedido
Para finalizar o pedido, o usuário pode selecionar a mesa e o cliente, além de ter a opção de imprimir o pedido de forma parcial. A finalização do pedido é semelhante ao segundo PDV desenvolvido, permitindo gerar a fatura ou selecionar o tipo de pagamento. O sistema oferece opções de finalização fiscal e não fiscal.

### Impressão e Registro da Venda
Após a finalização, o pedido é impresso e registrado como uma venda no PDV. O usuário pode acessar a lista do PDV para visualizar a venda gerada, que é registrada com a data e hora da transação.

---

## 80. Fatura padrão por cliente

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Funcionalidade de Fatura Padrão no Cadastro do Cliente
Foi desenvolvida uma nova aba chamada "Fatura" no cadastro do cliente. Nessa aba, é possível lançar o tipo de pagamento e os dias para o vencimento.

### Geração de Vendas com Fatura Padrão
Ao criar uma venda e selecionar um cliente, a opção de gerar a fatura conforme definido na aba "Fatura" será exibida. É possível adicionar mais um pagamento, como por exemplo, de 90 dias, e deixar desmarcado o tipo de pagamento. O único campo obrigatório é o número de dias para o vencimento.

### Salvar Configurações de Fatura
Após definir as configurações, como o tipo de pagamento (por exemplo, "dinheiro"), é necessário salvar. Ao realizar uma nova venda para o cliente, o botão "Fatura Padrão por Cliente" será liberado.

### Uso no PDV
No ponto de venda (PDV), ao selecionar um item e buscar o cliente, a funcionalidade se mantém. Clicando no botão, uma modal será aberta com as informações da fatura padrão do cliente.

---

## 81. Módulo contador aprimorando

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas |

### Melhorias no Módulo de Contador
O módulo de contador, disponível há cerca de um ano, recebeu melhorias significativas. Anteriormente, era possível apenas visualizar cadastros de clientes, produtos, fornecedores e documentos, além de filtrar por data e baixar o XML. Agora, é possível gerar Notas Fiscais Eletrônicas (NFE) e Notas Fiscais de Consumidor Eletrônicas (NFC), além de realizar eventos como aprovar, cancelar e corrigir.

### Acesso e Visualização de Documentos
Na home do módulo, é possível visualizar os clientes e empresas disponíveis. O usuário pode selecionar uma empresa para visualizar os documentos. Ao acessar a NFE, é possível ver todos os registros da empresa selecionada e alternar rapidamente entre diferentes empresas. O painel da empresa exibe todas as vendas registradas, permitindo gerar novas vendas e transmiti-las.

### Transmissão e Gerenciamento de Vendas
Após gerar uma venda, ela fica disponível no painel da empresa. O usuário pode transmitir a venda, editar, excluir ou visualizar o XML temporário. O status da venda é atualizado para "aprovado" após a transmissão. Também é possível filtrar vendas por status e baixar todos os XMLs aprovados.

### Cadastro e Edição de Produtos e Fornecedores
O módulo agora permite editar produtos, clientes e fornecedores. O contador pode corrigir informações sem precisar cadastrar novos itens. Além disso, foi implementada a funcionalidade de gerenciar a natureza de operação, permitindo cadastrar, editar e excluir.

### Configurações do Cliente e Conta
O módulo inclui opções para alterar informações do cliente, como certificado e endereço. Também foi adicionada uma seção para gerenciar a conta do contador, onde é possível alterar e-mail, nome, imagem e senha. Essas implementações tornaram o módulo mais funcional e fácil de usar.

---

## 82. App PDV Comandas React Native

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas, Mesas, React Native |

### Desenvolvimento do App PDV com React Native
O vídeo demonstra um aplicativo desenvolvido com React Native para o ERP, com o objetivo de substituir a versão anterior feita em Ionic. O app possui controle de comandas e PDV com emissão de NFC-e.

### Emissão de NFC-e
O usuário pode realizar a emissão de NFC-e através do app. É possível fazer a leitura do código de barras do item, adicionar itens à venda e finalizar a transação. Durante a finalização, há opções para inserir CPF e observações, além de selecionar o tipo de pagamento, como débito ou pagamento múltiplo. Após a finalização, o arquivo PDF da NFC-e pode ser compartilhado e impresso.

### Controle de Adicionais
O app permite o controle de adicionais para itens, como pizzas. O usuário pode adicionar mais sabores clicando sobre o item, que abre uma modal para adicionar ao carrinho. O funcionamento é semelhante à versão anterior do app.

### Cadastro de Produtos e Clientes
No menu lateral, o usuário pode cadastrar e visualizar produtos. O cadastro é simplificado, utilizando o padrão de tributação da parte web. Para alterar informações de tributação, é necessário acessar a parte web. Também é possível cadastrar, editar e excluir clientes.

### Funcionalidades do Caixa e Relatórios
O app oferece funcionalidades de caixa, permitindo visualizar vendas aprovadas, baixar PDFs de comprovantes fiscais e não fiscais, e fechar o caixa. Há também opções para contas a receber, incluindo edição e recebimento de contas. Atualmente, existem dois relatórios disponíveis, com a possibilidade de adicionar mais conforme a necessidade. O acesso ao app requer senha e configuração de URL, token e código do funcionário.

---

## 83. Valor promocional por período

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas, Mesas, React Native |

### Cadastro de Valores Promocionais
O sistema permite o cadastro de valores promocionais dos produtos por período. Para isso, é necessário editar o item desejado, onde são apresentados os campos: produto selecionado, valor original (sem promoção), valor da promoção, status (que deve estar ativo), data de início e data de fim da promoção.

### Visualização de Itens em Promoção
Na tela inicial, é possível visualizar a quantidade de itens em promoção no card. Após atualizar a página, essa informação é exibida de forma clara.

### Cadastro em Grupo com Percentual
Outra forma de cadastrar promoções é em grupo, utilizando um percentual de alteração. É possível selecionar vários produtos ativos do sistema, definir o período da promoção e inserir o percentual de redução sobre o valor de venda, por exemplo, 10%. Após salvar, os produtos são adicionados à tela de promoção.

### Efeitos no App e PDV
As promoções cadastradas têm efeito tanto no aplicativo quanto no ponto de venda (PDV). Ao realizar uma nova venda no PDV, os itens em promoção aparecem com um card indicando a promoção e informando o período em que estão ativos. Os itens que não estão em promoção permanecem inalterados.

---

## 84. Emissão de NFe App React Native

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas, Mesas, React Native |

### Melhorias no App
O vídeo apresenta melhorias no aplicativo, incluindo o cadastro de fornecedor, contas a pagar e a emissão de Nota Fiscal Eletrônica (NFe) pelo app.

### Emissão de NFe
A nova funcionalidade permite a listagem das vendas de NFe, com opções de filtros e a criação de uma nova venda. É obrigatório selecionar um cliente para finalizar a venda, enquanto a parte de fatura é opcional.

### Funcionalidades de Pagamento
Na seção de pagamento, é possível definir a natureza da operação, que já vem com uma opção padrão selecionada, mas pode ser modificada. Também é possível adicionar dados de frete antes de finalizar a operação.

### Impressão de Documentos
Após a emissão da NFe, o usuário pode imprimir o pedido em formato A4 e também tem a opção de imprimir a DAMF. Existe a funcionalidade de cancelamento, que permite remover mensagens padrão para testes.

### Próximos Passos
O próximo passo no desenvolvimento do app será a criação da funcionalidade de pré-venda, que permitirá salvar como orçamento, com o objetivo de aprimorar o aplicativo ao longo do tempo.

---

## 85. Melhorias na responsividade

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas, Mesas, React Native |

### Melhorias na Exibição de Produtos e Clientes
Foi implementada uma nova configuração que permite mudar a forma de visualização dos produtos e clientes de tabela, que é o padrão, para card. Essa opção está disponível tanto para produtos quanto para clientes. Após salvar a configuração, ao atualizar a página de produtos, a exibição mudará conforme a escolha. Essa funcionalidade também se aplica a estoque e promoções. No cadastro de clientes, foi adicionada a opção de incluir uma foto do cliente, que é opcional.

### Paginação de Itens
A paginação dos itens foi aprimorada. Anteriormente, havia um padrão definido na configuração do arquivo ENV. Agora, é possível alterar a quantidade de itens exibidos por página diretamente nas configurações. Por exemplo, se estiver definido para 30, serão listados 30 clientes na página. Se a configuração geral for alterada para 10, serão exibidos 10 cards, aumentando assim a quantidade de páginas.

### Responsividade de Tabelas
Foi desenvolvida uma melhoria na responsividade das tabelas do sistema. Ao acessar a seção de serviços, por exemplo, ao simular um smartphone, a tabela será exibida como um card. Essa funcionalidade foi implementada em todas as telas do sistema que possuem tabelas, garantindo uma melhor experiência de uso em dispositivos móveis.

---

## 86. Garantia para produtos

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas, Mesas, React Native |

### Melhoria no Cadastro de Produtos
Foi desenvolvida uma melhoria no cadastro de produtos relacionada às garantias. Agora, existe um campo chamado "prazo de garantias", que é opcional. Se esse campo for preenchido e uma venda do produto for realizada, a garantia será registrada na lista de garantias.

### Registro e Controle de Garantias
Após a venda, a garantia é lançada com o status "registrado". É possível controlar os estados das garantias registradas, adicionar observações e realizar impressões. Ao registrar a venda, o sistema cria um registro com os dados do cliente, o prazo de garantia e a data de expiração, que é atualizada automaticamente.

### Edição e Filtragem de Garantias
O sistema permite filtrar as garantias para visualizar itens que necessitam de alterações. É possível editar a garantia, informando o valor de reparo, alterando os dados e adicionando descrições de problemas ou observações.

### Lançamento Manual de Garantias
Além do registro automático, também é possível lançar a garantia de forma manual. Para isso, é necessário informar o produto, o cliente e outros registros obrigatórios.

---

## 87. Acessar as empresas através do superadmin

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas, Mesas, React Native |

### Acesso às Empresas pelo Super Admin
A funcionalidade do super admin permite acessar as empresas e usuários sem a necessidade de digitar e-mail e senha. 

### Navegação entre Usuários
No super admin, é possível visualizar a lista de usuários. Ao clicar em um usuário, o acesso é imediato, permitindo realizar cadastros, configurações e outras ações.

### Mudança de Dashboard
Ao acessar uma nova empresa, o dashboard muda automaticamente, refletindo os valores e informações específicas daquela empresa. 

### Listagem de Produtos
A listagem de produtos também é alterada conforme a empresa acessada, facilitando a manutenção e gestão para o cliente.

---

## 88. Mensagens automáticas para pós venda, aniversário e reativação

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas, Mesas, React Native |

### Mensagens Padrões no CRM
Neste vídeo, é demonstrada uma melhoria no CRM relacionada às mensagens padrões. As mensagens disponíveis incluem pós-venda, aniversário, reativação e pós-agendamento. Essas mensagens podem ser configuradas para serem enviadas após a venda ou agendamento.

### Configuração de Mensagens
Para configurar as mensagens, é necessário definir o tempo de envio. Por exemplo, para o pós-venda, é possível programar o envio 30 dias após a venda. Para o aniversário, deve-se definir o horário de envio. Na reativação, informa-se quantos dias após a última compra a mensagem será enviada. O agendamento segue a mesma lógica do pós-venda.

### Métodos de Envio
As mensagens podem ser enviadas através do WhatsApp, utilizando a API da Crew Adsra, ou pelo e-mail padrão do sistema, que pode ser o e-mail configurado no arquivo EV. A mensagem pode incluir variáveis, como o nome do cliente, que será substituído automaticamente.

### Logs de Mensagens
Os logs de mensagens permitem filtrar por data. Caso não haja vendas registradas, não aparecerão logs. Quando uma venda for realizada, um log será criado automaticamente. Por exemplo, se a venda ocorrer e a mensagem estiver programada para 30 dias depois, o sistema verificará a configuração no dia determinado e enviará a mensagem ao cliente.

### Funcionamento Geral
O sistema funciona para as mensagens de aniversário, reativação, pós-venda e pós-agendamento. No dia programado, o Chrome do servidor executará a verificação das mensagens a serem enviadas, substituindo as variáveis e disparando as mensagens conforme configurado.

---

## 89. Ordem de serviço melhorias e assistência técnica

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas, Mesas, React Native |

### Configuração da Ordem de Serviço
Na configuração geral, é necessário escolher o tipo da Ordem de Serviço (OS) como assistência técnica para que apareçam os campos específicos. Os campos a serem informados incluem o tipo de serviço (reparo, manutenção, instalação), o equipamento, número de série, cor e o diagnóstico do cliente.

### Criação de Ordem de Serviço
Uma ordem de serviço pode ser pré-cadastrada com um produto e um serviço. Por exemplo, foi adicionada uma tela de iPhone para o serviço de troca de tela, com o custo de R$ 900. Também foi registrado um serviço adicional com custo de R$ 150.

### Acompanhamento da Ordem de Serviço
Foi acrescentada uma opção de link que pode ser enviado ao cliente para que ele acompanhe o andamento da ordem de serviço. O diagnóstico técnico pode ser preenchido e salvo, e todas as informações são impressas na ordem de serviço.

### Garantias na Ordem de Serviço
A ordem de serviço pode ser atribuída à parte de garantia. Se o serviço ou produto tiver garantia, isso será refletido na ordem. A garantia é atrelada à ordem de serviço e é ativada ao alterar o estado da ordem.

### Faturamento da Ordem de Serviço
Ao finalizar a ordem de serviço, o sistema pergunta se deseja gerar um faturamento. É possível informar a fatura, como R$ 1.000 em dinheiro, e a data. Se a data for posterior ao dia atual, a fatura entrará no contas a receber do cliente. Após salvar, a fatura será gerada corretamente.

---

## 90. Novo PDV Web mobile

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas, Mesas, React Native |

### Introdução ao PDV Web Mobile
O vídeo demonstra o novo PDV para smartphones, que foi desenvolvido para se adaptar melhor a esses dispositivos. O sistema identifica automaticamente quando está sendo acessado por um smartphone e renderiza uma tela otimizada.

### Funcionalidades do PDV
As funcionalidades do PDV mobile são semelhantes às do PDV desenvolvido com React. É possível navegar entre categorias, filtrar produtos e realizar buscas utilizando a câmera para escanear códigos de barras. O sistema foi testado em dispositivos Android e iOS.

### Adição de Itens e Carrinho
Para adicionar um item, caso ele tenha adicionais, é possível selecionar a quantidade. O carrinho exibe os itens selecionados, incluindo opções como pizza, onde é possível escolher o tamanho e os sabores. O valor é calculado com base nas configurações escolhidas.

### Finalização da Venda
Na finalização da venda, é possível selecionar um cliente opcional e inserir o CPF para a nota. O sistema permite aplicar descontos, acréscimos e escolher os tipos de pagamento. Se um único tipo de pagamento for selecionado, o sistema confirma automaticamente. Caso contrário, é possível adicionar diferentes formas de pagamento e o sistema informa o valor restante.

### Comandas e Vendas Suspensas
O PDV mobile também permite trabalhar com comandas, listando as abertas e fechadas. É possível adicionar itens a uma comanda e finalizá-la. O sistema também possui a funcionalidade de vendas suspensas, que podem ser finalizadas posteriormente. Além disso, há opções de modo escuro e claro para melhor usabilidade.

---

## 91. Melhorias no PDV

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas, Mesas, React Native |

### Melhorias no PDV
Foi apresentado um vídeo sobre melhorias no modelo um do PDV do sistema. Foram adicionadas opções de recebimento de caixa diretamente no PDV. O usuário pode filtrar o cliente, que trará as contas a receber pendentes e as que estão em atraso. É possível selecionar essas contas e visualizar os totais, facilitando o processo de recebimento. Após o recebimento, o sistema redireciona para o PDV.

### Alterações na Interface
A interface do PDV foi simplificada, reduzindo os cards e organizando quatro colunas por linha. Agora, há uma opção para visualizar os detalhes do produto ao clicar no ícone de informação. Os produtos mais vendidos nos últimos 30 dias aparecem sempre no topo da lista, facilitando o acesso.

### Tela de Pagamento
A tela de pagamento foi reformulada, abrindo em uma visualização completa. O usuário pode escolher a forma de pagamento, como dinheiro, e inserir um valor. O sistema gera automaticamente o troco. Após finalizar, são exibidas as informações do pagamento registrado, permitindo a finalização de contas fiscais ou não fiscais, gerando o comprovante correspondente.

### Funcionalidades Adicionais
As funcionalidades de sangria e suprimento permanecem inalteradas. A tela para visualizar vendas suspensas também continua da mesma forma, mantendo a usabilidade anterior.

---

## 92. Analise de custos, backup e validação fiscal

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas, Mesas, React Native |

### Configuração de Custos
A configuração de custos permite definir percentuais para imposto, taxa de cartão, outras despesas e margem mínima. No exemplo, foram definidos 10% para imposto, 3,999% para taxa de cartão, 3% para outras despesas e uma margem mínima de 50% para cada item. É possível criar exceções, como no caso da Coca-Cola, onde o imposto é 10%, a taxa de cartão é 4%, outras despesas são 10% e a margem mínima permanece em 50%. Essa configuração ajuda na análise de margem, permitindo identificar produtos com prejuízo, margem baixa ou saudável. É possível filtrar os produtos e ajustar valores de venda diretamente na tela.

### Backup no Super Admin
No módulo Super Admin, foi implementada a funcionalidade de backup, que permite zipar um arquivo com o banco de dados e diretórios essenciais. Ao clicar em "gerar backup", o sistema pode demorar alguns minutos para criar um arquivo zip, que será baixado automaticamente. É importante aguardar o término do processo para garantir que o backup seja concluído corretamente.

### Análise Fiscal Preventiva
A análise fiscal preventiva é realizada ao salvar uma nova venda, seja no módulo de venda pedido ou na tela de PDV. O sistema analisa o CST, CFOP e NSM dos produtos e, caso encontre algum erro, aponta imediatamente. Foi adicionada uma coluna de status fiscal que indica se a venda possui erros. Por exemplo, a venda 859 apresenta um erro relacionado ao CST00 para empresas do Simples Nacional, com uma sugestão de correção. O objetivo dessa funcionalidade é reduzir a necessidade de suporte, permitindo que o usuário edite e salve as informações corretas, atualizando o status para OK.

---

## 93. Score de clientes

**Tags:** Multiempresa, Laravel, PHP, NFe, NFCe, Automacao, ionic, comandas, delivery, autoatendimento, sass, Controle de comandas, Mesas, React Native |

### Configuração do Score de Clientes
No ERP GT Sistemas, a funcionalidade de score permite a configuração de parâmetros para categorizar os clientes em ouro, prata e bronze. Os parâmetros incluem pagamentos em dia e volume de vendas nos últimos 12 meses. Por exemplo, um cliente que vende até R$ 1.000 recebe 400 pontos, enquanto um que vende R$ 500 recebe 200 pontos. Também são considerados o ticket médio e penalidades que podem reduzir o score.

### Atualização Diária do Score
Sempre que um usuário acessa a empresa, o sistema verifica se o score dos clientes já foi atualizado no dia. Caso não tenha sido, o sistema realiza a atualização do score diariamente, garantindo que as informações estejam sempre atualizadas.

### Visualização e Filtragem de Scores
Na tela de score, é possível visualizar a pontuação de cada cliente e filtrar por categoria. Além disso, a tela permite filtrar por data de cadastro e nome, possibilitando a visualização de detalhes e o histórico mensal de cada cliente. Essa funcionalidade auxilia na tomada de decisões, especialmente para vendas no crediário.

### Suporte e Atualizações
O vídeo também menciona um novo número de suporte via WhatsApp, disponível para questões relacionadas ao código fonte ou à compra do mesmo. O número atualizado está disponível na descrição do vídeo.

---

## 94. PDV Integração com TEF Sitef

**Tags:** TEF, Saas, Multiempresa |

### Integração do PDV com TEF Sitef
O vídeo aborda a integração do ponto de venda (PDV) com o sistema de Transferência Eletrônica de Fundos (TEF) da Sitef. Essa integração permite que as transações financeiras sejam realizadas de forma mais eficiente e segura, facilitando o processo de pagamento para os clientes.

### Configuração do TEF no GT Sistemas
Para configurar o TEF no GT Sistemas, é necessário acessar o módulo de configurações do PDV. Dentro desse módulo, deve-se selecionar a opção de integração com TEF e preencher os campos obrigatórios, como o código da máquina e as credenciais de acesso fornecidas pela Sitef.

### Realização de Transações
Após a configuração, o operador do PDV pode realizar transações utilizando o TEF. Durante o processo de venda, ao selecionar a forma de pagamento, o sistema deve direcionar automaticamente para a interface do TEF, onde o cliente pode inserir os dados do cartão e concluir a transação.

### Relatórios de Vendas
O GT Sistemas também permite gerar relatórios de vendas que incluem as transações realizadas via TEF. Esses relatórios podem ser acessados no módulo de relatórios, facilitando o acompanhamento das vendas e a conciliação financeira.

### Suporte e Dúvidas
Caso surjam dúvidas ou problemas durante a integração ou uso do TEF, é recomendado consultar a documentação do GT Sistemas ou entrar em contato com o suporte técnico para obter assistência.

---

## 95. Melhorias PDV Offline

### Melhorias no PDV Offline
O vídeo apresenta melhorias no PDV offline, incluindo a adição de funcionalidades como contas a receber, cadastro de clientes e produtos. Anteriormente, era possível apenas visualizar essas informações. 

### Cadastro de Produtos
Agora é possível cadastrar novos produtos através de um formulário simples. O modal permite inserir nome, valor de compra, valor de venda, código de barras, categoria e o padrão de tributação, que é obrigatório e já está definido na parte web. Ao selecionar o padrão, todas as informações necessárias são preenchidas automaticamente.

### Cadastro de Clientes
O cadastro de clientes também foi simplificado. O formulário é semelhante ao da versão web, mas com alguns campos a menos. É possível digitar o CNPJ, que fará uma busca automática e trará as informações necessárias para o cadastro.

### Contas a Receber
No PDV offline, é possível cadastrar, editar e receber contas a receber de forma simples, utilizando um modal para facilitar o processo.

### Impressão Automática de Cupons
Ao finalizar uma venda, se houver uma impressora padrão definida no sistema operacional, o cupom será impresso automaticamente. Caso contrário, a janela de impressão será aberta. O vídeo também menciona a funcionalidade de operar o PDV sem o mouse, utilizando atalhos de teclado para facilitar a navegação e finalização das vendas.

---

## 96. PDV   venda temporária e logs

### Ajuste no PDV para Vendas Temporárias
Este vídeo aborda um ajuste no PDV relacionado às vendas temporárias. Ao simular uma venda, se o navegador atualizar ou a máquina reiniciar, ao retornar à tela do PDV, será exibida uma mensagem informando que existe uma venda temporária. O usuário pode optar por abandonar a venda ou continuar.

### Continuação da Venda Temporária
Se o usuário optar por continuar, os itens e o cliente (se selecionado) serão recuperados. O usuário pode adicionar outros itens e finalizar a venda normalmente. Existe uma tela no menu PDV, na seção de vendas temporárias, que é visível apenas para administradores.

### Visualização de Vendas Temporárias
Ao atualizar a página, o sistema exibirá a venda temporária, incluindo a data, o usuário, o local da venda e os itens adicionados. Se algum item for removido e a página for atualizada, essa alteração também será refletida.

### Armazenamento de Logs de Vendas
O sistema armazena logs das vendas no PDV. Se a venda for finalizada, o status será alterado para "finalizado". Caso a venda seja abandonada, o status ficará como "abandonada". O usuário pode filtrar as vendas por período, horário e usuário para monitorar as atividades do PDV no dia a dia.

---

## 97. PDV Offline controle de comandas

### Comandas no PDV Offline
O vídeo apresenta a funcionalidade de comandas no PDV offline. Um botão amarelo permite visualizar as comandas em aberto. Na parte web, é possível abrir uma nova comanda, sendo necessário informar pelo menos o nome do cliente.

### Inclusão de Itens na Comanda
Após abrir a comanda, é possível incluir itens. Caso um item esteja sem estoque, a inclusão ainda pode ser realizada. Não é necessário salvar manualmente, pois a inclusão já é registrada automaticamente na comanda.

### Finalização da Comanda
O processo de finalização da comanda é semelhante ao de inclusão. É possível adicionar observações e controlar adicionais. A cada alteração, uma requisição é feita na API para salvar as informações. A finalização pode ser feita diretamente no PDV offline, e a comanda desaparece da tela após ser finalizada.

### Edição de Comandas
Para utilizar uma comanda existente, basta clicar sobre ela, o que traz os itens associados. É possível adicionar novos itens, remover itens ou editar a quantidade. As alterações refletem imediatamente no valor total da comanda.
