

var links = document.getElementsByClassName("chaptergroup");

for(var i = 0; i < links.length; i++){

    if (!links[i].hasAttribute("href")){
        links[i].setAttribute("data-toggle", "modal");
        links[i].setAttribute("href", "#");
    }

    if (links[i].getAttribute("href").localeCompare("#") == 0)
    {
        var value = links[i].getAttribute("data-chpmodalcode");
        links[i].setAttribute("href", "#"+value);
        var chapspan = links[i].getElementsByClassName("chapterspan");

        for(var k = 0; k < chapspan.length; k++)
        {
            chapspan[k].setAttribute("class", "chapterspan p-2 mt-2 badge badge-white text-black rounded-5 border border-warning");
        }

        $(document).on("click", ".chaptergroup", function () {
            var myChapterId = $(this).data('chapterid');
            var cid = document.getElementsByName("chapterId");
            for(var i = 0; i < cid.length; i++){
                cid[i].setAttribute("value", myChapterId);
            }
            var myProductId = $(this).data('productid');
            var pid = document.getElementsByName("productId");
            for(var i = 0; i < pid.length; i++){
                pid[i].setAttribute("value", myProductId);
            }
        });
    }
}

