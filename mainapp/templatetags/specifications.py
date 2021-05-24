from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Smartphone

register = template.Library()

TABLE_HEAD = """
               <table class="table">
                   <tbody>
             """

TABLE_TAIL = """
                   <tbody>
                </table>   
             """

TABLE_CONTENT = """
                    <tr>
                        <td>{name}</td>
                        <td>{value}</td>
                    </tr>
                    
                """

PRODUCT_SPEC = {
    'notebook': {

        'Diagonal': 'diagonal',
        'Display turi': 'display_type',
        'Chastota': 'processor_freq',
        'Tezkor xotira': 'ram', 
        'Asosiy xotira': 'rom',
        'Videokarta': 'videokart',
        'Akkumulyator avtonomlik vaqti': 'time_without_charge',

    },

    'smartphone': {

        'Diagonal': 'diagonal',
        'Display turi': 'display_type',
        'Ekran o`lchamlari': 'resolution',
        'Tezkor xotira': 'ram', 
        'Asosiy xotira': 'rom',
        'SD karta': 'sd',
        'Maksimal tashqi xotira': 'sd_volume_max',
        'Akkumulyator sig`imi': 'accum_volume',
        'Asosiy kamera': 'main_cam_mp',
        'Frontal kamera': 'front_cam_mp',

    }
}

def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Smartphone):
        if product.sd:
            PRODUCT_SPEC['smartphone']['Maksimal tashqi xotira'] = 'sd_volume_max'
        else:
             PRODUCT_SPEC['smartphone'].pop('Maksimal tashqi xotira')
             


    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)