/**
 * Created by xhermit on 29.07.14.
 */

function on_catalog_click(catalog_uuid)
{
    //Обработчик клика на категории товара
    ajax_get_content_data(catalog_uuid);
}

function ajax_get_content_data(catalog_uuid)
{
    //Получить данные по каталогу
    //Отправка Ajax запроса
    $.get("/ajaxgetcontent/"+catalog_uuid+"/")
        .done(function(data){
            //Получение ответа от сервера
            create_content_html(data);
            });

}

function create_content_html(content_data)
{
    //Очистить предыдущие данные
    $('#mainContent').empty();
    $('#mainContent').append("<h2>Витрина</h2>");

    for (var i=0; i < content_data.length; i++)
    {
        var label = content_data[i].label;
        var price = content_data[i].price;
        var img = content_data[i].img;
        var uuid = content_data[i].uuid;

        var wareHTML = $('<div class=\"shopId\"><div class=\"shopIdHeader\"></div></div>');
        var priceHTML = $('<div class=\"shopIdPrice\">'+price+'</div>');
        var buttonBuyHTML = $('<div><input type=\"button\" value=\"Заказать\" class=\"buttonbuy\" onclick=\"on_order_button_click(\''+uuid+'\')\"/></div>');
        var imgHTML = $('<div><img src=\"/media/images/'+img+'\" width=183 height=113 alt=\"\" /></div>');
        var labelHTML = $('<div class=\"shopIdTitle\">'+label+'</div>');

        wareHTML.children('.shopIdHeader').append(priceHTML);
        wareHTML.children('.shopIdHeader').append(buttonBuyHTML);
        wareHTML.append(imgHTML);
        wareHTML.append(labelHTML);
        $('#mainContent').append(wareHTML);
    }

}
