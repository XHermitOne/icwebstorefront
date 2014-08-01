/**
 * Created by xhermit on 01.08.14.
 */

function on_order_button_click(ware_uuid)
{
    ajax_add_order(ware_uuid);
}

var CUR_ORDER_UUID=null;

function on_show_order_click()
{
    if(CUR_ORDER_UUID==null) {
        alert("Заказ не определен");
    }
    else
    {
        //Переход по url
        location.assign("/order/"+CUR_ORDER_UUID+"/");
    }
}

function on_perform_order_click(order_uuid)
{
        $.get("/ajaxperformorder/" + order_uuid + "/")
            .done(function (msg) {
                //Получение ответа от сервера
                if( msg=="OK") {
                    CUR_ORDER_UUID = null;
                    alert("Данные вашего заказа отправлены исполнителю");
                }
                else
                {
                    alert(msg);
                }
                //Переход по url
                location.assign("/");
            });

}

function ajax_add_order(ware_uuid)
{
    //Добавить товар в заказ
    //Отправка Ajax запроса
    if(CUR_ORDER_UUID==null) {
        $.get("/ajaxneworder/" + ware_uuid + "/")
            .done(function (uuid) {
                //Получение ответа от сервера
                console.log("New UUID " + uuid);
                CUR_ORDER_UUID = uuid;
            });
    }
    else
    {
        $.get("/ajaxaddorder/" + ware_uuid + "/" + CUR_ORDER_UUID + "/")
            .done(function (uuid) {
                //Получение ответа от сервера
                console.log("UUID " + uuid);
            });

    }

}