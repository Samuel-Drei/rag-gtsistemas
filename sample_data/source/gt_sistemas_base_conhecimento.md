# Base de Conhecimento — GT Sistemas ERP

## Visão Geral do Sistema

### O que é o GT Sistemas
O GT Sistemas é um ERP (sistema de gestão) usado por pequenas e médias empresas para controlar vendas, compras, estoque, produtos, serviços e emissão de documentos fiscais eletrônicos. Ele é organizado em módulos acessados pelo menu lateral, como Produtos, Vendas, Compras, Ordem de Serviço, NFSe, PDV, Financeiro, Locação, Delivery/Marketplace, entre outros. O sistema também tem um painel de "SuperAdmin", usado pela equipe que administra o sistema (não pelo cliente final), para gerenciar empresas, planos, configurações globais e arquivos do servidor.

### Quais documentos fiscais o sistema emite
O GT Sistemas emite os principais documentos fiscais eletrônicos brasileiros: NF-e (Nota Fiscal Eletrônica, para venda de produtos/mercadorias), NFSe (Nota Fiscal de Serviço Eletrônica, para prestação de serviços), NFCe (Nota Fiscal de Consumidor Eletrônica, tipo cupom fiscal para venda direta ao consumidor final), CT-e (Conhecimento de Transporte Eletrônico) e MDF-e (Manifesto Eletrônico de Documentos Fiscais, usado no transporte de cargas).

### Diferença entre nota de produto e nota de serviço
Uma empresa que vende mercadoria (produto físico) emite NF-e; uma empresa que presta serviço (ex.: lavagem, manutenção, consultoria) emite NFSe. Muitas empresas emitem os dois tipos ao mesmo tempo — por exemplo, um lavajato que presta serviço de lavagem (NFSe) e também vende produtos de estética automotiva no balcão (NF-e). Cada tipo de nota tem seu próprio módulo, cadastros e regras fiscais dentro do sistema.

### Diferença entre emitir uma nota e dar entrada em uma nota
"Emitir" uma nota fiscal significa que a própria empresa é quem vende algo (produto ou serviço) para um cliente — ela gera o documento, assina com seu certificado digital e envia para a Receita. "Dar entrada" em uma nota é o processo inverso: quando um fornecedor vende algo para a empresa, é o fornecedor quem emite a nota, e a empresa apenas confirma o recebimento dela no sistema (por meio do Manifesto do Destinatário), para atualizar seu estoque e seu financeiro (contas a pagar).

### O que é uma Ordem de Serviço
Ordem de Serviço (OS) é o registro interno de um serviço a ser (ou já) prestado a um cliente, geralmente vinculado a um veículo ou item específico. É usada para organizar o atendimento antes de gerar a nota fiscal e o financeiro — por exemplo, uma OS de "Polimento" com o veículo do cliente, valor combinado e status de andamento. Depois de aprovada e finalizada, a OS pode ser convertida em faturamento (cobrança) e, idealmente, em uma nota fiscal de serviço.

### O que é o PDV
PDV (Ponto de Venda) é a tela de caixa do sistema, pensada para venda rápida de produtos no balcão: o operador busca o produto, adiciona no carrinho, escolhe a forma de pagamento e finaliza, gerando a nota fiscal correspondente automaticamente ao efetuar o pagamento.

### O que é o Manifesto do Destinatário
Manifesto do Destinatário é a funcionalidade que consulta diretamente na Receita Federal todas as notas fiscais emitidas por outras empresas contra o CNPJ do usuário (ou seja, tudo que foi comprado ou recebido). A partir dessa consulta, é possível dar "ciência" da existência da nota e depois completar sua entrada no sistema, dando baixa fiscal e (se configurado) atualizando o estoque.

### O que é Natureza de Operação
Natureza de Operação é a classificação de cada venda ou compra (ex.: "Venda de mercadoria", "Compra para revenda", "Compra para uso interno"). Ela é obrigatória para emitir qualquer nota fiscal e influencia diretamente o cálculo de impostos, por isso deve ser definida com orientação de um contador.

### O que é CFOP, CST/CSOSN e NCM (em termos simples)
CFOP é um código que identifica o tipo de operação fiscal (por exemplo, venda dentro do estado ou para outro estado). CST/CSOSN identifica como aquele produto é tributado pelo ICMS, variando conforme o regime tributário da empresa (Simples Nacional usa CSOSN; outros regimes usam CST). NCM é o código que classifica a mercadoria em si, conforme uma tabela nacional de produtos. Esses três códigos juntos, definidos no cadastro do produto, são obrigatórios para qualquer nota fiscal de mercadoria.

### Ambiente de Produção x Homologação
O sistema pode operar em dois ambientes: "Homologação" é o ambiente de teste da Receita, onde notas emitidas não têm validade fiscal real. "Produção" é o ambiente real — qualquer nota emitida e autorizada em Produção é um documento fiscal válido de verdade. É importante saber em qual ambiente o sistema está configurado antes de testar qualquer emissão de nota.

## Configuração Fiscal da Empresa (Emitente)

### Onde configurar os dados fiscais da empresa
Os dados fiscais da empresa ficam em Configurações > Emitente. A tela é dividida em abas: Empresa, Endereço, Emissão e Certificado A1. Na aba Empresa ficam CNPJ, Razão Social, Nome Fantasia, Inscrição Estadual e Tipo de Tributação (ex.: Simples Nacional). Na aba Endereço ficam os dados de localização completos, obrigatórios para emissão de nota. Na aba Certificado A1 é feito o upload do arquivo do certificado digital (.pfx ou .p12) e a senha; o sistema mostra a data de início e expiração do certificado carregado.

### Aba Emissão do Emitente e numeração de notas
Na aba Emissão do Emitente ficam os campos de numeração de cada tipo de documento fiscal (NFe, NFCe, CTe, MDFe), cada um com "Número de série", "Número da última (Produção)" e "Número da última (Homologação)". Também ficam nessa aba os campos de NFSe: CSC, CSC ID, Token, Token NFSe, Número da última NFSe, Número de série NFSe e "Tipo de emissão NFSe" (opções: IntegraNotas ou NFSe Nacional).

### Como corrigir número de NF-e duplicado (erro 539)
Se ao transmitir uma NF-e aparecer o erro "[539] Rejeicao: Duplicidade de NF-e", significa que o número da nota já foi usado (mesmo em tentativa rejeitada, o número é consumido na SEFAZ). Para corrigir, vá em Configurações > Emitente > aba Emissão e aumente o valor do campo "Número da última (Produção)" da seção NFe para um número maior do que o já utilizado. Esse ajuste é manual: o sistema não sincroniza esse número sozinho após uma rejeição, então pode ser necessário repetir esse ajuste sempre que uma nota for rejeitada.

### Tipo de emissão NFSe: IntegraNotas x NFSe Nacional
O campo "Tipo de emissão NFSe" (em Emitente > Emissão) define qual caminho técnico o sistema usa para emitir nota de serviço. "IntegraNotas" depende de uma credencial (usuário/senha ou token) de um serviço intermediário terceirizado, cadastrada na tela NFSe > Emitente Integranotas — se essa credencial não existir, a emissão de NFSe fica bloqueada e a tela mostra erro de configuração ausente. "NFSe Nacional" é o sistema oficial do governo federal, não depende de credencial de terceiro, só do certificado digital já configurado. Trocar de IntegraNotas para NFSe Nacional destrava a emissão quando não há credencial do Integranotas disponível.

### Onde configurar a numeração da NFSe
Além da numeração dentro do Emitente, existe uma tela dedicada em NFSe > Configuração (rota `/nota-servico-config-nacional`), com os campos: Número da última, Número de série, Ambiente (Produção/Homologação), Versão, Versão da aplicação e Modelo nacional (Sim/Não). O campo "Modelo nacional" deve ser marcado como "Sim" quando o sistema estiver configurado para usar NFSe Nacional (coerente com o campo equivalente no Emitente); deixá-lo em "Não" enquanto se usa o modelo nacional é uma inconsistência de configuração.

## Cadastro de Produto

### Como cadastrar um produto com dados fiscais
O cadastro de produto (Produtos > Novo Produto) tem três abas: Identificação, Fiscal e Outros/Integrações. Na aba Identificação ficam nome, valor de venda, valor de compra, gerenciamento de estoque (Sim/Não) e estoque inicial, unidade de medida, categoria, entre outros. Na aba Fiscal ficam os campos exigidos pela Receita para gerar NF-e: NCM, Origem, CST/CSOSN, CFOP Estadual, CFOP Inter Estadual, CFOP Entrada Estadual, CFOP Entrada Inter Estadual, e percentuais de ICMS, PIS, COFINS e IPI (podem ser preenchidos com 0 quando o regime é Simples Nacional com CSOSN que não destaca imposto na nota).

### CFOP e CSOSN para empresa do Simples Nacional
Para uma empresa optante pelo Simples Nacional vendendo mercadoria, os valores mais comuns são: CST/CSOSN "102 - Tributada pelo Simples Nacional sem permissão de crédito"; CFOP Estadual "5102" (venda dentro do mesmo estado); CFOP Inter Estadual "6102" (venda para outro estado); CFOP Entrada Estadual "1102" e CFOP Entrada Inter Estadual "2102" (para quando esse mesmo produto for objeto de uma entrada/compra). Esses são valores de referência genéricos; a confirmação final da tributação correta deve vir de um contador.

### Campos obrigatórios de imposto no cadastro fiscal do produto
Mesmo quando o CSOSN não destaca valor de imposto na nota (ex.: código 102, típico do Simples Nacional), os campos percentuais (% ICMS, % PIS, % COFINS, % IPI) são obrigatórios para salvar o cadastro do produto — nesses casos, preencher com 0 é aceito pelo sistema.

## Emissão de NF-e (Venda de Produto)

### Como emitir uma NF-e de venda
O caminho é Vendas > Nova, que abre um formulário em abas: Cliente, Produtos, Frete e Fatura. Na aba Cliente é feita a busca/cadastro do destinatário; na aba Produtos são adicionados os itens vendidos; na aba Fatura ficam Natureza de Operação, dados de pagamento e o campo "Gerar conta a receber". Depois de salvar a venda, ela aparece com estado "Novo" em Vendas > Todas as Vendas (ou Vendas Pedido), e precisa ser transmitida clicando no ícone verde de "enviar" na linha correspondente para ser efetivamente autorizada pela SEFAZ.

### Campo Consumidor Final e erro de rejeição 696
Se ao transmitir uma NF-e aparecer o erro "[696] Rejeicao: Operacao com nao contribuinte deve indicar operacao com consumidor final", significa que o cadastro do cliente está com "Contribuinte: Não" mas "Consumidor Final: Não" ao mesmo tempo — uma combinação inconsistente para a SEFAZ. A correção é editar o cadastro do cliente (na aba Cliente da venda) e mudar "Consumidor Final" para "Sim".

### Como cancelar uma NF-e emitida
Na listagem de vendas (Vendas > Vendas Pedido ou Todas as Vendas), a linha de uma nota autorizada tem vários ícones de ação; o ícone vermelho (círculo com X) abre a tela "Cancelar NF-e". É preciso preencher o campo "Motivo do Cancelamento" (mínimo de caracteres exigido pela SEFAZ) e clicar em "Transmitir Cancelamento". O cancelamento é irreversível depois de autorizado e deve respeitar o prazo permitido pela SEFAZ (normalmente até 24h da emissão).

### Erro de cancelamento por acentuação (erro 402)
Se ao transmitir um cancelamento de NF-e aparecer o erro "[402] Rejeicao: XML da area de dados com codificacao diferente de UTF-8", a causa provável é o uso de acentos ou caracteres especiais no campo "Motivo do Cancelamento". Escrever o motivo apenas com letras sem acento resolve o problema.

## Módulo Compras / Entrada de Nota Fiscal

### Como consultar notas de compra pendentes (Manifesto do Destinatário)
O caminho é Compras > Manifesto. O botão "Nova Consulta de Documentos" busca diretamente na SEFAZ, usando o certificado digital da empresa, todas as notas fiscais emitidas por terceiros contra o CNPJ da empresa (compras, devoluções, transferências), independentemente de já terem sido processadas no sistema. A lista retornada tem abas por status (ex.: pendentes, já manifestadas).

### Como dar entrada em uma nota de compra (fluxo completo)
Depois de localizar a nota no Manifesto, primeiro clique em "Manifestar" e escolha "Ciência da Operação" — isso registra na SEFAZ que a empresa está ciente da existência da nota, sem confirmar nem recusar o recebimento ainda. Após a ciência ser aceita (status muda para "Ciência" na listagem), aparece um botão verde "Completa", que abre a tela de conferência da entrada, com abas Fornecedor, Produtos, Frete e Fatura. Na aba Produtos, produtos que ainda não existem no cadastro aparecem com o aviso "Produto será cadastrado no sistema" e são criados automaticamente ao salvar. É necessário selecionar uma Natureza de Operação de entrada (ex.: "Compra de mercadoria para revenda tributada") para conseguir salvar essa entrada — sem isso, o processo não fecha.

### Campo "Gerenciar estoque" na tela de entrada de compra
Na aba Produtos da tela de conferência de entrada (Compras > Manifesto > Completa), existe o seletor "Gerenciar estoque" (Sim/Não) por produto. Se marcado como "Sim", a entrada deve subir o saldo de estoque do produto ao ser salva; se "Não", a nota fica registrada como recebida para fins fiscais, mas não afeta nenhum saldo de estoque — útil quando o item comprado não é destinado à revenda (ex.: material de uso interno).

### Limite de eventos de manifesto (erro 594) e duplicidade (erro 573)
A SEFAZ limita quantos eventos de manifestação podem ser registrados para uma mesma chave de acesso de NF-e. Se uma nota já foi manifestada antes (mesmo em tentativa anterior ou em dias diferentes), tentar manifestar de novo pode gerar "[573] Rejeicao: Duplicidade de evento" ou, após reiterar, "[594] Rejeicao: O numero de sequencia do evento informado e maior que o permitido". Esse não é um erro do sistema GT Sistemas, é uma regra da própria Receita aplicada àquela chave específica; não há correção técnica possível pelo painel. Quando isso acontece com uma nota real que precisa ser lançada, a orientação de como registrar essa entrada de forma alternativa (por exemplo, lançamento manual sem depender do manifesto eletrônico) deve vir do contador responsável.

## Natureza de Operação

### O que é e por que é obrigatória
Natureza de Operação é um cadastro (Configurações > Natureza de operação) que classifica o tipo de operação fiscal de cada venda ou entrada (ex.: "Venda de mercadoria tributada", "Compra de mercadoria para revenda tributada"). É um campo obrigatório tanto na emissão de NF-e de venda quanto na entrada de nota de compra, e também aparece na tela de NFSe. Sem pelo menos uma natureza real cadastrada, apenas eventuais registros de teste (ex.: um item chamado "AMAROK" cadastrado por padrão) ficam disponíveis, o que impede o fechamento de vendas e entradas reais.

### Exemplos de naturezas de operação recomendadas por um contador
Para uma empresa que compra e vende mercadoria, um contador pode recomendar cadastrar naturezas específicas como: "Compra de mercadoria para revenda tributada", "Compra de mercadoria para revenda substituto tributária", "Compra de mercadoria de uso ou consumo", "Venda de mercadoria tributada", "Venda de mercadoria substituto tributária" (também chamada de "Venda ST"). Quanto mais específica a natureza cadastrada, melhor a classificação fiscal — a escolha de quais naturezas realmente se aplicam depende da finalidade real de cada compra ou venda no negócio (revenda, uso interno, etc.), então essa decisão deve ser validada com o contador.

### Campos do cadastro de Nova Natureza de Operação
A tela de cadastro (Configurações > Natureza de operação > Nova) tem os campos obrigatórios: Descrição, Padrão (Sim/Não — se essa natureza deve vir pré-selecionada), Sobrescrever CFOP (Sim/Não), Movimentar Estoque (Sim/Não) e Indicador de presença. Tem também o campo Tipo de operação (Entrada ou Saída). Abaixo, uma seção opcional de "Dados Para Emissão" (CST/CSOSN, CST PIS, CST COFINS, CST IPI, percentuais de imposto, CFOPs) que, se preenchida, sobrescreve os dados já cadastrados no produto ao gerar o XML da nota — se deixada em branco, o sistema usa os dados do cadastro do produto normalmente.

## NFSe (Nota Fiscal de Serviço)

### Como emitir uma NFSe
O caminho é NFSe > Nova, com abas Tomador (dados do cliente) e Serviço. Na aba Serviço, é preciso buscar e selecionar um serviço já cadastrado (em Serviços), o que preenche automaticamente descrição e valor. Depois é obrigatório preencher: Código do serviço (conforme a Lista de Serviços da LC 116), Código NBS, UF do local de prestação, Cidade do local de prestação e Natureza de Operação (campo de texto livre nessa tela, diferente do campo de seleção usado na NF-e de produto).

### Código NBS vazio impede toda emissão de NFSe
Se o campo "Código NBS" aparecer como um dropdown vazio, sem nenhuma opção para selecionar, a causa é a ausência de um arquivo `nbs.txt` no servidor, no caminho esperado pela aplicação (ex.: `/public_html/public/nbs.txt`). O sistema tenta carregar a lista de códigos NBS a partir desse arquivo via `file_get_contents`, e sem ele a lista fica vazia e a nota não pode ser salva, mesmo com todos os outros campos preenchidos corretamente. A correção é técnica: subir o arquivo `nbs.txt` na pasta correta do servidor (via FTP, SSH ou gerenciador de arquivos do cPanel — ferramentas de upload internas do painel administrativo do sistema podem bloquear esse destino por segurança).

### O que é o código NBS
NBS (Nomenclatura Brasileira de Serviços) é uma classificação oficial nacional de serviços, exigida como campo obrigatório na emissão de NFSe pelo modelo Nacional. Cada código representa um tipo específico de serviço reconhecido pela Receita Federal, e impacta a forma como a nota é validada e tributada. O código correto deve ser escolhido de acordo com a atividade real prestada; não deve ser preenchido de forma arbitrária em notas reais.

### Código de serviço (LC 116) e tributação municipal
Além do NBS, a NFSe exige um "Código do serviço", referente à Lista de Serviços da Lei Complementar 116, e opcionalmente um "Código de tributação do município". Esses códigos variam conforme o município e a atividade prestada, e definem a base de cálculo do ISS. A confirmação desses códigos para uma atividade específica (ex.: lavagem/estética automotiva) deve ser feita com um contador antes de qualquer nota real ser emitida.

## Ordem de Serviço

### Estrutura da tela de Ordem de Serviço
Uma Ordem de Serviço (Ordem de Serviço > Nova OS / Listar) tem cabeçalho com estado (ex.: Aprovado), total, funcionário e técnico responsável, veículo vinculado, e uma seção de Serviços onde é possível adicionar múltiplos itens de serviço com quantidade, valor unitário e status (ex.: Pendente, Finalizado). A OS pode ser impressa (gera um recibo interno com todos os dados: empresa, cliente, veículo, serviços e valores), mas esse documento impresso não tem validade fiscal — não substitui uma NFSe.

### Botão "Gerar Venda" na Ordem de Serviço
Dentro de uma Ordem de Serviço aprovada existe um botão "Gerar Venda", que abre um modal com duas opções: "Finalizar pedido" e "Finalizar no PDV". Nenhuma delas gera diretamente uma NFSe: "Finalizar pedido" abre a tela "Nova Venda - NFe" (fluxo de venda de produto/mercadoria, não de serviço), com Natureza de Operação e Tipo de Nota configurados para mercadoria; "Finalizar no PDV" abre o PDV (tela de caixa) totalmente vazio, sem os dados da OS carregados (nem cliente, nem serviços), mesmo a URL de navegação conter o identificador da OS de origem. Esse comportamento foi reproduzido em mais de uma OS diferente e corresponde a um problema real relatado por usuários ao tentar lançar um serviço (ex.: funilaria e pintura) no caixa a partir de uma OS.

### Como faturar uma Ordem de Serviço pelo caminho alternativo (Alterar Estado)
Existe um caminho funcional para gerar o faturamento de uma OS sem depender do botão "Gerar Venda": o botão "Alterar Estado" na tela da OS abre um formulário com os campos Estado (ex.: Finalizado), "Gerar faturamento" (Sim/Não) e, quando "Gerar faturamento" está em Sim, uma seção de lançamento de pagamento com Tipo de Pagamento, Data de Vencimento e Valor, um botão "Adicionar parcela" e um total ("Soma") que deve bater com o total da Ordem de Serviço antes de salvar. Esse caminho permite registrar o faturamento/financeiro da OS mesmo com o bug do botão "Gerar Venda" ainda não corrigido.

## PDV (Ponto de Venda)

### Estrutura da tela do PDV
O PDV (menu PDV) é uma tela de caixa com busca de produto por código de barras ou nome, campos de quantidade e valor unitário, um carrinho com colunas Produto, Quantidade, Valor e Subtotal, seleção de cliente, e um painel de "Ações do Caixa" (Recebimento, Sangria, Suprimento) e "Ações do PDV" (Lista de Preços, Frete, Vendas Suspensas, Orçamentos). O botão "Efetuar Pagamento" finaliza a venda e é o passo que efetivamente gera e tenta transmitir a nota fiscal correspondente — antes de clicar nele nenhuma nota é emitida.

## Central de Faturamento (NF-e)

### O que é e como acessar
Vendas > Faturamento (NF-e) abre a "Central de Faturamento", um painel com indicadores (Pedidos Pendentes, Prontos para Faturar, NFes Emitidas Hoje, NFes Canceladas, Valor Faturado Hoje, Aguardando SEFAZ) e abas de listagem (Pendentes de Faturamento, NFes Emitidas, Rejeições SEFAZ, Canceladas, Carta de Correção). Cada pedido pendente mostra um fluxo visual do faturamento (Pedido → Fiscal → NF-e → Enviado) com as datas de cada etapa.

### Erro de coluna ausente no banco de dados (data_faturamento)
Se ao abrir a Central de Faturamento aparecer um erro do tipo "SQLSTATE[42S22]: Column not found: 1054 Unknown column 'data_faturamento'", a causa é uma migration de banco de dados pendente naquele ambiente específico — a coluna usada pelo código para filtrar notas emitidas no dia não existe na tabela. A correção é executar o comando SQL `ALTER TABLE nves ADD COLUMN data_faturamento timestamp null default null;` diretamente no banco de dados (via ferramenta de administração de banco do painel SuperAdmin, ou por quem tiver acesso direto ao banco).

## Boas práticas de teste no ambiente de Produção

### Risco de usar dados reais/pessoais em notas de teste
Ao testar emissão de nota fiscal em ambiente de Produção (não Homologação), qualquer nota transmitida com sucesso é um documento fiscal real e válido perante a SEFAZ. Usar CPF ou CNPJ de uma pessoa real (inclusive o próprio CPF de quem está testando) como destinatário de uma nota de teste gera um documento fiscal real vinculado a essa pessoa, que pode precisar ser cancelado formalmente depois. Recomenda-se sempre usar um cliente cadastrado especificamente para testes, com CPF genérico, e revisar esse cadastro antes de reutilizá-lo.

### Cuidado ao manifestar repetidamente a mesma nota real durante testes
Usar uma nota fiscal real (de um fornecedor de verdade) repetidamente como "cobaia" de teste de manifesto pode esgotar o limite de eventos permitido pela SEFAZ para aquela chave de acesso específica, impedindo que a entrada real dessa nota seja processada normalmente no futuro. Para testes de manifesto, é preferível escolher uma nota de baixo valor e evitar repetir a operação nela desnecessariamente.
