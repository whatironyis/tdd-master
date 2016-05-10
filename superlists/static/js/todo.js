function edit(id)
{
    $.ajax({
        url: "/edit/",
        type: "POST",
        data: { 'value':id },
        success: function(){
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
        success: function(){
            window.location.reload(true);
            }
    });
}

function inpro(id)
{
    $.ajax({
        url: "/inpro/",
        type: "POST",
        data: { 'value':id },
        success: function(){
            window.location.reload(true);
            }
    });
}

function filter(name)
{
    $.ajax({
        url: "/",
        type: "POST",
        data: { 'name':name },
        success: function(b){
         window.location.reload(true);
         }
    });
}