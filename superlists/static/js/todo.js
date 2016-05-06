function edit(id)
{
    $.ajax({
        url: "/edit/",
        type: "POST",
        data: { 'value':id },
        success: function(data){
            window.location.reload(true);
        }
    });
}
function todo(id)
{
    $.ajax({
        url: "/todo/",
        type: "POST",
        data: { 'value':id },
        success: function(data){
            window.location.reload(true);
            }
    });
}