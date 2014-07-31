/**
 * Created by xhermit on 31.07.14.
 */

function on_search_click()
{
    var search_txt = $('#searchedit').val().trim();

    //Переход по url
    location.assign('?search='+search_txt);
    console.log('Search '+search_txt);
}
