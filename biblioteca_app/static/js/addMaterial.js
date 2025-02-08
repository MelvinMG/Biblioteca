$(document).ready(function() {
    $("#guardarMaterial").click(function() {
        let formData = new FormData($("#formAgregarMaterial")[0]); 

        $.ajax({
            url: "/admin_material/agregar/", 
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            headers: {
                "X-CSRFToken": $("input[name=csrfmiddlewaretoken]").val() 
            },
            success: function(response) {
                alert("Material añadido con éxito");
                location.reload();  
            },
            error: function(xhr) {
                alert("Error al añadir el material.");
            }
        });
    });

    // ✅ Validación dinámica: Oculta/Activa campos según el tipo de material seleccionado
    $("#tipo").change(function() {
        let tipo = $(this).val();
        
        if (tipo === "L") {  // Libro
            $("#editorial").parent().show();
            $("#genero").parent().show();
        } else {
            $("#editorial").parent().hide();
            $("#genero").parent().hide();
        }

        if (tipo === "R") {  // Revista
            $("#volumen").parent().show();
        } else {
            $("#volumen").parent().hide();
        }
    });


    $("#tipo").trigger("change");
});
