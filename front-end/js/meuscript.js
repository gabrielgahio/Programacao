$(function() { // quando o documento estiver pronto/carregado
    
    // função para exibir pessoas na tabela
    function exibir_esportes() {
        $.ajax({
            url: 'http://localhost:5000/listar_modalidades',
            method: 'GET',
            dataType: 'json',
            success: listar, 
            error: function() {
            alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar (esportes) {
            // Limpa a tabela
            $('#corpoTabelaEsportes').empty();

            console.log(esportes);

            // Percorre a lista
            for (var i in esportes) { //i vale a posição no vetor
                lin = '<tr>' + 
                '<td>' + esportes[i].id + '</td>' + 
                '<td>' + esportes[i].nome + '</td>' + 
                '<td>' + esportes[i].modalidade + '</td>' +
                '<td>' + esportes[i].pais_favorito + '</td>' +
                '<td>' + esportes[i].atleta + '</td>' +
                '<td>' + esportes[i].nivel_de_dificuldade + '</td>' +
                '</tr>';
                // adiciona a linha no corpo da tabela
                $('#corpoTabelaEsportes').append(lin);
            }
            
            }
        };
    
    exibir_esportes();

    
});

