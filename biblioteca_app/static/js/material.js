$(document).ready(function() {
    // Cargar datos en el modal de edición
    $(".edit-btn").click(function() {
        let materialId = $(this).data("id");
        $("#edit_id").val(materialId);
        $("#edit_titulo").val($(this).data("titulo"));
        $("#edit_autor").val($(this).data("autor"));
        $("#edit_editorial").val($(this).data("editorial"));
        $("#edit_genero").val($(this).data("genero"));
        $("#edit_tipo").val($(this).data("tipo"));
        $("#edit_fecha").val($(this).data("fecha"));
    });

    // Guardar cambios en la edición
    $("#guardarEdicion").click(function() {
        let formData = new FormData($("#formEditarMaterial")[0]);
    
        $.ajax({
            url: "/admin_material/editar/", 
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            headers: {
                "X-CSRFToken": $("input[name=csrfmiddlewaretoken]").val()  
            },
            success: function(response) {
                alert("Material actualizado con éxito");
                location.reload();
            },
            error: function(xhr) {
                alert("Error al actualizar el material.");
            }
        });
    });
    

    // Cargar ID en el modal de eliminación
    $(".delete-btn").click(function() {
        let materialId = $(this).data("id");
        $("#delete_id").val(materialId);
    });

    // Confirmar eliminación
    $("#confirmarEliminar").click(function() {
        $.ajax({
            url: "/admin_material/eliminar/", 
            type: "POST",
            data: {
                id: $("#delete_id").val(),
                tipo: $("#edit_tipo").val(),  // ✅ Enviar el tipo de material
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(response) {
                alert("Material eliminado con éxito");
                location.reload();
            },
            error: function(xhr) {
                alert("Error al eliminar el material.");
            }
        });
    });
    
});
