from bojango.action.screen import ActionScreen, ActionButton, ScreenType
from bojango.core.routing import callback
import asyncio




@callback('s_start')
async def s_start(update, context):
    yield ActionScreen(
        text='Здравствуйте, что бы вы хотели узнать?',
        buttons=[
            [ActionButton(text='1С', action_name='s_1C')],
            [ActionButton(text='Рекламации', action_name='s_complaints')],
            [ActionButton(text='База знаний', action_name='s_knowledge_base')],
            [ActionButton(text='Сервисное обслуживание оборудования', action_name='s_select_subcategory')],
            [ActionButton(text='О компании', action_name='s_select_subcategory')],
            [ActionButton(text='Проверка вложенности', action_name='s_checking_nesting')],
            [ActionButton(text='Техническая поддержка', action_name='s_select_subcategory')]])




@callback('s_1C')
async def s_1c(update, context):
    yield ActionScreen(
        text='Выберите подкатегорию',
        buttons=[
            [ActionButton(text='Создание Заказа Покупателя и выставление счёта.', action_name='s_creating_order')],
            [ActionButton(text='Создание отгрузочной накладной', action_name='s_creating_invoice')],
            [ActionButton(text='Возврат от покупателя', action_name='s_return')],
            [ActionButton(text='Создание контрагента', action_name='s_creating_counterparty')],
            [ActionButton(text='Создание номенклатуры', action_name='s_creating_nomenclature')],
            [ActionButton(text='<< Назад', action_name='s_start')],
            [ActionButton(text='В меню ↩️', action_name='s_start')]])

@callback('s_creating_order')
async def s_creating_order(update, context):
    yield ActionScreen(text='Ожидайте... 😊')
    yield ActionScreen(
        text='Вот документ для изучения Создание Заказа Покупателя и выставление счёта.',
        file='files/Создание_Заказа_Покупателя_и_выставление_счёта.pdf',
        buttons=[[ActionButton(text='В меню ↩️', action_name='s_start')]])

@callback('s_creating_invoice')
async def s_creating_invoice(update, context):
    yield ActionScreen(text='Ожидайте... 😊')
    yield ActionScreen(
        text='Вот документ для изучения Создание отгрузочной накладной',
        file='files/Создание отгрузочной накладной.pdf',
        buttons=[[ActionButton(text='В меню ↩️', action_name='s_start')]])

@callback('s_return')
async def s_return(update, context):
    yield ActionScreen(text='Ожидайте... 😊')
    await asyncio.sleep(0.5)
    yield ActionScreen(
        text='Вот документ для изучения Возврат от покупателя',
        file='files/Возврат от покупателя.pdf',
        buttons=[[ActionButton(text='В меню ↩️', action_name='s_start')]])

@callback('s_creating_counterparty')
async def s_creating_counterparty(update, context):
    yield ActionScreen(text='Ожидайте... 😊')
    yield ActionScreen(
        text='Вот документ для изучения Создание контрагента',
        file='files/Создание контрагента.pdf',
        buttons=[[ActionButton(text='В меню ↩️', action_name='s_start')]])

@callback('s_creating_nomenclature')
async def s_creating_nomenclature(update, context):
    yield ActionScreen(text='Ожидайте... 😊')
    yield ActionScreen(
        text='Вот документ для изучения Создание номенклатуры',
        file='files/Создание номенклатуры.pdf',
        buttons=[[ActionButton(text='В меню ↩️', action_name='s_start')]])




@callback('s_complaints')
async def s_complaints(update, context):
    yield ActionScreen(
        text='Выберите подкатегорию',
        buttons=[
            [ActionButton(text='Клён', action_name='s_speach')],
            [ActionButton(text='Рестинтернешнл', action_name='s_restinternational')],
            [ActionButton(text='Мастергласс', action_name='s_speach')],
            [ActionButton(text='Регион 50 (Проект 2015)', action_name='s_speach')],
            [ActionButton(text='Русский проект (Метроном)', action_name='s_metronome')],
            [ActionButton(text='<< Назад', action_name='s_start')],
            [ActionButton(text='В меню ↩️', action_name='s_start')]])

@callback('s_restinternational')
async def s_restinternational(update, context):
    yield ActionScreen(text='Ожидайте... 😊')
    yield ActionScreen(
        text='Вот документ для изучения Рестинтернешнл',
        file='files/Рестинтернешнл.docx',
        buttons=[[ActionButton(text='В меню ↩️', action_name='s_start')]])

@callback('s_speach')
async def s_maple(update, context):
    yield ActionScreen(text='Ожидайте... 😊')
    yield ActionScreen(
        text='''1. В процессе принятия поставки склад выписывает недостающие/лишние/ бракованные товары и записывает его в Яндекс документах https://clck.ru/3GMy82 во вкладке «Клён», сообщает о необходимости в написании рекламации в отдельном чате «Рекламации» в WhatsApp (если есть фото отправляет их в тот же чат).
     2. Рекламационист исходя из этого списка по шаблону предыдущих рекламаций \\srv\Документы\Челны Хорека флешка\Рекламации\Клен путём копирования создает документ в Word, корректирует и сохраняет его в папке со следующим порядковым номером рекламации. Если есть фото, то вставляет их в папку. 
     3. Рекламационист отправляет в рекламационный отдел Поставщика по почте vellhelp@yandex.ru Wordовский документ и имеющиеся фото. В теме письма указывается «Рекламация №». Делаем пометку строки в Яндекс таблице https://clck.ru/3GMy82 оранжевым цветом (Ждём ответа).
     4. Ждём ответа от Поставщика не более 5 дней. По истечению 5-ти дней, напоминаем отделу рекламаций vellhelp@yandex.ru
5. При Отказе - статус рекламации меняется на Отказ и дополняется Яндекс таблица (Цвет всей строки - красный, В столбце комментарий указываем причину отказа). Просим согласовать руководителя добавить товар в Списание в 1С либо продолжаем доказывать свою точку зрения.
6. При Одобрении - статус рекламации меняется на Согласовано и дополняется Яндекс таблица (Цвет всей строки – желтый, в столбце комментарий указываем необходимый комментарий. Например: должны отправить со следующей поставкой. Предупредить коллег, и проследить, чтобы вложили в следующую отгрузку.
7. При поступлении товара на склад - статус рекламации меняется на Поступило и дополняется Яндекс таблица (Цвет всей строки – зелёный, в столбце комментарий пишем «Поступило» с указанием даты поступления).''',
        buttons=[[ActionButton(text='В меню ↩️', action_name='s_start')]])

@callback('s_metronome')
async def s_metronome(update, context):
    yield ActionScreen(text='Ожидайте... 😊')
    yield ActionScreen(
        text='''В процессе принятия поставки склад выписывает недостающие/лишние/ бракованные товары и записывает его в Яндекс документах https://clck.ru/3GMy82 во вкладке «Метроном посуда», сообщает о необходимости в написании рекламации в отдельном чате «Рекламации» в WhatsApp (если есть фото отправляет их в тот же чат).
Рекламационист исходя из этого списка по шаблону предыдущих рекламаций \\Srv\документы\Челны Хорека флешка\Рекламации\РП Метроном путём копирования создает документ новую папку для данной рекламации, убирает лишние файлы, редактирует в Word (Например: Рекламация №139), корректирует и сохраняет его. Если есть фото, то вставляет их в папку. 
Рекламационист отправляет менеджеру Поставщика по почте Мельниковой Оксане melnikova-o@rp.ru Wordовский документ и имеющиеся фото. В теме письма указывается «Рекламация №, дата, артикул». Делаем пометку строки в Яндекс таблице https://clck.ru/3GMy82 оранжевым цветом (Ждём ответа).
Ждём ответа от Поставщика не более 5 дней. По истечению 5-ти дней, напоминаем отделу рекламаций melnikova-o@rp.ru 
При Отказе - статус рекламации меняется на Отказ и дополняется Яндекс таблица (Цвет всей строки - красный, В столбце комментарий указываем причину отказа).
При Одобрении - статус рекламации меняется на Согласовано и дополняется Яндекс таблица (Цвет всей строки – желтый, в столбце комментарий указываем необходимый комментарий. Например: должны отправить со следующей поставкой). Предупредить коллег, и проследить, чтобы вложили в следующую отгрузку).
При поступлении товара на склад - статус рекламации меняется на Поступило и дополняется Яндекс таблица (Цвет всей строки – зелёный, в столбце комментарий пишем «Поступило» с указанием даты поступления).''',
        buttons=[[ActionButton(text='В меню ↩️', action_name='s_start')]])




@callback('s_knowledge_base')
async def s_knowledge_base(update, context):
    yield ActionScreen(
        text='Выберите подкатегорию',
        buttons=[
            [ActionButton(text='Барный инвентарь', action_name='s_bar_inventory')],
            [ActionButton(text='Сиропы, топинги, пюре', action_name='s_syrups_toppings_purees')],
            [ActionButton(text='Оборудование', action_name='s_equipment')],
            [ActionButton(text='<< Назад', action_name='s_start')],
            [ActionButton(text='В меню ↩️', action_name='s_start')]])

@callback('s_bar_inventory')
async def s_bar_inventory(update, context):
    yield ActionScreen(text='Ожидайте... 😊')
    yield ActionScreen(
        text='Вот документ для изучения Барный инвентарь',
        file='files/Барный инвентарь.pdf',
        buttons=[[ActionButton(text='В меню ↩️', action_name='s_start')]])

@callback('s_syrups_toppings_purees')
async def s_syrups_toppings_purees(update, context):
    yield ActionScreen(text='Ожидайте... 😊')
    yield ActionScreen(
        text='Вот документ для изучения Сиропы, топинги, пюре',
        file='files/Сиропы, топинги, пюре.pdf',
        buttons=[[ActionButton(text='В меню ↩️', action_name='s_start')]])

@callback('s_equipment')
async def s_equipment(update, context):
    yield ActionScreen(text='Ожидайте... 😊')




@callback('s_checking_nesting')
async def s_checking_nesting(update, context):
    yield ActionScreen(
        text='Выберите подкатегорию',
        buttons=[
            [ActionButton(text='Первый', action_name='s_one_nesting')],
            [ActionButton(text='Второй', action_name='s_examination')],
            [ActionButton(text='третий', action_name='s_equipment')],
            [ActionButton(text='<< Назад', action_name='s_start')],
            [ActionButton(text='В меню ↩️', action_name='s_start')]])

@callback('s_one_nesting')
async def s_one_nesting(update, context):
    yield ActionScreen(
        text='Выберите подподкатегорию',
        buttons=[
            [ActionButton(text='ПодПодКатегория', action_name='s_sub_subcategory')],
            [ActionButton(text='2 ПодПодКатегория', action_name='s_examination')],
            [ActionButton(text='<< Назад', action_name='s_start')],
            [ActionButton(text='В меню ↩️', action_name='s_start')]])

@callback('s_sub_subcategory')
async def s_sub_subcategory(update, context):
    yield ActionScreen(
        text='Выберите подподкатегорию',
        buttons=[
        [ActionButton(text='Ещё вложеннее', action_name='s_examination')],
        [ActionButton(text='<< Назад', action_name='s_start')],
        [ActionButton(text='В меню ↩️', action_name='s_start')]])


@callback('s_examination')
async def s_examination(update, context):
    yield ActionScreen(
        text='Просто проверка, ничего важного',
        buttons=[[ActionButton(text='В меню ↩️', action_name='s_start')]])


@callback('s_select_subcategory')
async def s_select_subcategory(update, context):
    yield ActionScreen(
        text='Выберите подкатегорию',
        buttons=[
            [ActionButton(text='<< Назад', action_name='s_start')],
            [ActionButton(text='В меню ↩️', action_name='s_start')]])