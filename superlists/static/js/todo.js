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
function post_delete(pk)
{
    $.ajax({
        url: "/delete/",
        type: "POST",
        data: { 'value': pk },
        success: function(){
            console.log(window.location.host)
            console.log(window.location.hostname)
            http = window.location.services
            document.location.href="/";
        }
    });
}